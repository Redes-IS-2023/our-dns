#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <arpa/inet.h>

#define MAX_BUFFER_SIZE 4096
#define DNS_PORT 53


char* encodeBase64(const char* data, int length) {
    const char base64chars[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
    int encodedLength = 4 * ((length + 2) / 3);
    char* encodedData = (char*)malloc(encodedLength + 1);

    int i, j;
    for (i = 0, j = 0; i < length; i += 3, j += 4) {
        unsigned char byte1 = data[i];
        unsigned char byte2 = (i + 1 < length) ? data[i + 1] : 0;
        unsigned char byte3 = (i + 2 < length) ? data[i + 2] : 0;

        unsigned char b64byte1 = byte1 >> 2;
        unsigned char b64byte2 = ((byte1 & 0x03) << 4) | (byte2 >> 4);
        unsigned char b64byte3 = ((byte2 & 0x0F) << 2) | (byte3 >> 6);
        unsigned char b64byte4 = byte3 & 0x3F;

        encodedData[j] = base64chars[b64byte1];
        encodedData[j + 1] = base64chars[b64byte2];
        encodedData[j + 2] = (i + 1 < length) ? base64chars[b64byte3] : '=';
        encodedData[j + 3] = (i + 2 < length) ? base64chars[b64byte4] : '=';
    }

    encodedData[encodedLength] = '\0';

    return encodedData;
}


void saveQRToFile(int qr) {
    FILE* file = fopen("./docs/qr.txt", "w");
    if (file == NULL) {
        perror("Error al abrir el archivo qr.txt");
        return;
    }

    fprintf(file, "%d\n", qr);
    fclose(file);
}

void saveOPCODEToFile(int opcode) {
    FILE* file = fopen("./docs/opcode.txt", "w");
    if (file == NULL) {
        perror("Error al abrir el archivo opcode.txt");
        return;
    }

    fprintf(file, "%d\n", opcode);
    fclose(file);
}

void saveURLToFile(const char* url) {
    FILE* file = fopen("./docs/url.txt", "w");
    if (file == NULL) {
        perror("Error al abrir el archivo url.txt");
        return;
    }

    fprintf(file, "%s\n", url);
    fclose(file);
}

void saveDataToFile(const char* data, int length) {
    FILE* file = fopen("./docs/data.txt", "w");
    if (file == NULL) {
        perror("Error al abrir el archivo");
        return;
    }

    fwrite(data, sizeof(char), length, file);

    fclose(file);
}

void processDNSPacket(const char* buffer, int bytesRead) {
    // Verificar el formato del paquete DNS según el estándar RFC2929
    // Obtener el QR y el OPCODE del paquete DNS

    //unsigned char qr = (buffer[2] >> 7) & 0x01;
    //unsigned char opcode = (buffer[2] >> 3) & 0x0F;

    unsigned int qr = (unsigned int) buffer[2];
    qr = qr <<7;
    qr = qr >>7;

    unsigned int opcode = (unsigned int) buffer[2];
    opcode = opcode <<3;
    opcode = opcode >>4;

    // Guardar el QR y el OPCODE en archivos separados
    saveQRToFile(qr);
    saveOPCODEToFile(opcode);

    // Obtener la dirección URL del paquete DNS
    char url[256];
    int urlLength = 0;

    // Leer la sección de preguntas del paquete DNS
    int questionSectionPos = 12;
    while (buffer[questionSectionPos] != 0x00) {
        int labelLength = buffer[questionSectionPos];
        strncpy(url + urlLength, buffer + questionSectionPos + 1, labelLength);
        urlLength += labelLength;
        url[urlLength++] = '.';

        questionSectionPos += labelLength + 1;
    }
    url[urlLength - 1] = '\0';

    // Guardar la dirección URL en un archivo
    saveURLToFile(url);


    // Codificar la dirección URL en Base64
    char* base64URL = encodeBase64(url, urlLength);
    printf("URL codificada en Base64: %s\n", base64URL);
    // Enviar la dirección URL codificada a otro método
    //sendBase64URL(base64URL);

    // Liberar memoria
    free(base64URL);
}
int main() {
     // Crear la carpeta "docs" si no existe
    int result = mkdir("./docs", 0777);
    if (result != 0) {
        printf("Error al crear la carpeta.\n");
        return 1;
    }


    int sockfd;
    char *ip = "127.0.0.1";
    struct sockaddr_in serverAddr, clientAddr;
    char buffer[MAX_BUFFER_SIZE];

    // Crear el socket UDP
    if ((sockfd = socket(AF_INET, SOCK_DGRAM, 0)) < 0) {
        perror("Error al crear el socket");
        exit(EXIT_FAILURE);
    }

    memset(&serverAddr, 0, sizeof(serverAddr));
    memset(&clientAddr, 0, sizeof(clientAddr));

    // Configurar la dirección del servidor
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_port = htons(DNS_PORT);
    serverAddr.sin_addr.s_addr = inet_addr(ip);

    // Asociar el socket a la dirección del servidor
    if (bind(sockfd, (struct sockaddr*)&serverAddr, sizeof(serverAddr)) < 0) {
        perror("Error al asociar el socket");
        exit(EXIT_FAILURE);
    }

    while (1) {
        printf("Server recibiendo información.\n");
        socklen_t clientLen = sizeof(clientAddr);

        // Recibir paquetes DNS
        int bytesRead = recvfrom(sockfd, buffer, sizeof(buffer), 0, (struct sockaddr*)&clientAddr, &clientLen);
        if (bytesRead < 0) {
            perror("Error al recibir paquete");
            continue;
        }

        // Guardar los datos en un archivo
        saveDataToFile(buffer, bytesRead);

        // Procesar el paquete DNS
        processDNSPacket(buffer, bytesRead);
    }

    // Cerrar el socket

    return 0;
}