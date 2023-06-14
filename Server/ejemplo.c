#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <arpa/inet.h>

#define MAX_BUFFER_SIZE 4096
#define DNS_PORT 53

int main() {
    char *ip = "127.0.0.1";
    int sockfd;
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

    printf("Servidor DNS iniciado en el puerto %d\n", DNS_PORT);

    while (1) {
        socklen_t clientLen = sizeof(clientAddr);

        // Recibir paquetes DNS
        int bytesRead = recvfrom(sockfd, buffer, MAX_BUFFER_SIZE, 0, (struct sockaddr*)&clientAddr, &clientLen);
        if (bytesRead < 0) {
            perror("Error al recibir paquete");
            continue;
        }

        // Guardar el paquete DNS en un archivo de texto
        FILE* file = fopen("dns_packets.txt", "a");
        if (file == NULL) {
            perror("Error al abrir el archivo");
            continue;
        }

        fwrite(buffer, 1, bytesRead, file);
        fclose(file);

        printf("Paquete DNS recibido y guardado en dns_packets.txt\n");
    }

  

    return 0;
}
