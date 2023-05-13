# our-dns

## Dependencies

- Docker
- Python with the _requirements.txt_ (if you want to run the project locally)

## Running the project

1. By running Docker compose `docker compose up`

2. Run an specific component

   1. API
      1. Build the image `docker build -t our-dns-api .`
      2. Run the image `docker run -p 5000:5000 our-dns-api`

3. By using VSCode, the .vscode/launch.json is configure to run the currently open file, open api/main.py and just run it.

## API

To access the API documentation go to:
[http://localhost:5000/apidocs/#/](http://localhost:5000/apidocs/#/)

## References

[Build your Python image](https://docs.docker.com/language/python/build-images/)

[Python | Reading .ini Configuration Files](https://www.geeksforgeeks.org/python-reading-ini-configuration-files/)
