Tecnológico de Costa Rica.

Escuela de Ingeniería en Computación.

IC: 7602-Redes - 2 Semestre 2022.

2018086509 - Jocxan Sandi Batista.

2018145020 - José Daniel Acuña.

---


## Índice

- DNS Interceptor
- DNS Resolver 
- WEB
- Referencias


## DNS Interceptor 

Espera las solicitudes y guarda los datos en el archivo. 

Se obtiene el OPCODE y el QR en la función **saveDataToFile** y lo guarda en diferentes archivos, en esa misma función obtiene el URL y se envía a la función de **encodeBase64** que devuelve el string listo para poder enviarlo al API pero esto no se implemento. 


```
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
```


## Referencias 

https://www.educative.io/answers/how-to-implement-udp-sockets-in-c
https://stackoverflow.com/questions/342409/how-do-i-base64-encode-decode-in-c
https://askubuntu.com/questions/907246/how-to-disable-systemd-resolved-in-ubuntu