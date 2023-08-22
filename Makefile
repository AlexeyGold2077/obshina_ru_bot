run:
	docker run -d --rm --name obshina_ru_bot -v data:/app/data obshina_ru_bot:v1.2
stop:
	docker stop obshina_ru_bot