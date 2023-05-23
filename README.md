# our-dns

## Dependencies

- Docker
- Python with the dependencies listed on the `api/requirements.txt` file (if you want to run the project locally)

## Running the project

1. Use the Makefile to build and run the project
   - `make compose` runs docker compose up
   - `make docker-api` runs docker image build for the api
   - `make test` runs all unit tests

## API

To access the API documentation go to:
[http://localhost:5000/apidocs/#/](http://localhost:5000/apidocs/#/)

## Firebase

To see an example of the realtime DB semi-structured data go to the next [file](/firebasedb/our-dns-default-rtdb-export.json)

## Sample packages

This directory contains code that helps testing the API component, like:

- Creating DNS packages in binary files
- Creating encoded b64 files to use as HTML bodies

### Creating a DNS bin file

Run the **server.py** app, its a DNS interceptor that writes DNS packages to an binary file `./out/package.bin`, to inject data into the package use the command `nslookup [domain_name] 127.0.0.1`, for example:

```
nslookup example.com 127.0.0.1
```

To see the resulting package use an hex reader like `hexyl ./out/package.bin`

### Testing in Postman using the encoded file

To encode a file run the **convert.py** file, this will create a b64.txt that can be use as raw body in postman to test the API in the HTML POST `/api/dns_resolver/`

## References

- [Build your Python image](https://docs.docker.com/language/python/build-images/)
- [Python | Reading .ini Configuration Files](https://www.geeksforgeeks.org/python-reading-ini-configuration-files/)
- [dnspython](https://www.dnspython.org/)
- [IP Geolocation by DB-IP](https://db-ip.com)
- [What does a DNS request look like?](https://serverfault.com/questions/173187/what-does-a-dns-request-look-like)
