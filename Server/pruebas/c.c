#include <stdio.h>
#include <curl/curl.h>

int main(void)
{
    CURL *curl;
    CURLcode res;

    curl_global_init(CURL_GLOBAL_DEFAULT);
    curl = curl_easy_init();
    if(curl) {
        // Configurar la URL de la API
        curl_easy_setopt(curl, CURLOPT_URL, "http://localhost:5000/api/endpoint");

        // Establecer el cuerpo de la solicitud como JSON
        curl_easy_setopt(curl, CURLOPT_POSTFIELDS, "{\"key\": \"value\"}");
        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, "Content-Type: application/json");

        // Configurar una función para recibir la respuesta
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, fwrite);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, stdout);

        // Enviar la solicitud POST
        res = curl_easy_perform(curl);

        // Verificar si la solicitud fue exitosa
        if(res != CURLE_OK)
            fprintf(stderr, "Error al enviar la solicitud: %s\n", curl_easy_strerror(res));

        // Limpiar
        curl_easy_cleanup(curl);
    }
    curl_global_cleanup();

    return 0;
}
