build:
	docker build -t our-dns-api .
	docker run -p 5000:5000 our-dns-api