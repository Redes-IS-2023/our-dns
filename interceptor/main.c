#include <bits/stdc++.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>

#define PORT 53
#define MAXLINE 1024

int isStandardQuery(buffer);

// Driver code
int main() {

    // --- Socket Config ---

    int sockfd;
    char buffer[MAXLINE];
    const char* hello = "Hello from server";
    struct sockaddr_in servaddr, cliaddr;

    // Creating socket file descriptor
    if ((sockfd = socket(AF_INET, SOCK_DGRAM, 0)) < 0) {
        perror("socket creation failed");
        exit(EXIT_FAILURE);
    }

    memset(&servaddr, 0, sizeof(servaddr));
    memset(&cliaddr, 0, sizeof(cliaddr));

    // Filling server information
    servaddr.sin_family = AF_INET; // IPv4
    servaddr.sin_addr.s_addr = INADDR_ANY;
    servaddr.sin_port = htons(PORT);

    // Bind the socket with the server address
    if (bind(sockfd, (const struct sockaddr*)&servaddr,
        sizeof(servaddr)) < 0)
    {
        perror("bind failed");
        exit(EXIT_FAILURE);
    }

    // --- ---

    // ??? Thread para recibir multiples solicitudes ???

    // --- Receive DNS protocol pack ---

    socklen_t len;
    int n;

    len = sizeof(cliaddr);  //len is value/result

    n = recvfrom(sockfd, (char*)buffer, MAXLINE,
        MSG_WAITALL, (struct sockaddr*)&cliaddr,
        &len);
    buffer[n] = '\0';

    printf("DNS Pack Received : %s\n", buffer);

    // --- ---

    if (isStandardQuery(buffer)) {

        // Identificar Host
        // Buscar Host a traves del API

        // Si existe
            // Extraer info y retornarla
            // - RFC2929 -
            // - RFC1035 -
    
        // Si no existe
            // Codificar solicitud a BASE64 y enviarla al API
            // via dns_resolver

    }
    else {
        // Codificar solicitud a BASE64 y enviarla al API
        // via dns_resolver
    }

    //sendto(sockfd, (const char*)hello, strlen(hello),
        //MSG_CONFIRM, (const struct sockaddr*)&cliaddr,
        //len);
    //std::cout << "Hello message sent." << std::endl;

    return 0;
}


// Returns true if the pack received is "standard query"
// - RFC2929 -
bool isStandardQuery(char buffer[MAXLINE]) {



    return true;
}

