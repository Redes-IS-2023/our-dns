compose:
	docker-compose up --build

docker-api:
	docker build -t our-dns-api -f dockerfile.api .
	docker run -p 5000:5000 our-dns-api

docker-web:
	docker build -t our-dns-web -f dockerfile.web .
	docker run -p 3000:3000 our-dns-web

test:
	python -m pytest api/tests