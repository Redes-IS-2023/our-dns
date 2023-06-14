#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
//#include "b64/cencode.h"
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>

#define PORT 53
#define MAXLINE 4096

void handleMessage(){};

int main(){
    char *ip = "127.0.0.1";
    int sockfd;
	unsigned char buffer[MAXLINE]= "";
	char *hello = "Hello from server";
	struct sockaddr_in servaddr, cliaddr;
		
	// Creating socket file descriptor
	if ( (sockfd = socket(AF_INET, SOCK_DGRAM, 0)) < 0 ) {
		perror("socket creation failed");
		exit(EXIT_FAILURE);
	}
		
	memset(&servaddr, 0, sizeof(servaddr));
	memset(&cliaddr, 0, sizeof(cliaddr));
		
	// Filling server information
	servaddr.sin_family = AF_INET; // IPv4
	//servaddr.sin_addr.s_addr = INADDR_ANY;
	servaddr.sin_port = htons(PORT);
    servaddr.sin_addr.s_addr = inet_addr(ip);

    // Bind the socket with the server address
	if ( bind(sockfd, (const struct sockaddr *)&servaddr,
			sizeof(servaddr)) < 0 )
	{
		perror("bind failed");
		exit(EXIT_FAILURE);
	}
    FILE* log_file, *log_file2;

    int len, n;
    len = sizeof(cliaddr); //len is value/result

    while (1){
        n = recvfrom(sockfd, (char *)buffer, MAXLINE,
				MSG_WAITALL, ( struct sockaddr *) &cliaddr,
				&len);

        unsigned int number = (unsigned int) buffer[2];
        number = number <<24;
        number = number >>31;
        printf("QR: %u \n", number);
        number = (unsigned int) buffer[2];
        number = number << 25;
        number = number >>28;
        printf("OPCODE: %u \n", number);

        log_file= fopen("log2.txt","wb");
        fwrite(buffer,1,n,log_file);

        //gcc server.c -o dns -lb64
    }
    

}