compose:
	docker-compose up --build

docker-api:
	docker build -t our-dns-api -f dockerfile.api .
	docker run -p 5000:5000 our-dns-api

test:
	python -m pytest api/tests