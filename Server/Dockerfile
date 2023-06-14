
FROM gcc:latest

WORKDIR /usr/src/app

COPY b.c /usr/src/app/

RUN gcc -o b b.c

CMD ["sudo ./b"]
