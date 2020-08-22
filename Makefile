dev:
	docker-compose build
	docker-compose up -d

dev/stop:
	docker-compose stop

prod:
	docker-compose -f docker-compose.prod.yaml build
	docker-compose -f docker-compose.prod.yaml up -d

prod/stop:
	docker-compose -f docker-compose.prod.yaml stop

exec:
	docker-compose exec app bash
