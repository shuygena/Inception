all: mkdir up

mkdir:
	sudo mkdir -p ~/data/wordpress && \
	mkdir -p ~/data/mariadb

up:
	sudo docker-compose -f srcs/docker-compose.yml up -d -V --build --force-recreate

down:
	sudo docker-compose -f srcs/docker-compose.yml down

ps:
	sudo docker-compose -f srcs/docker-compose.yml ps

info:
	@echo "**** IMAGES **** "
	@sudo docker images 
	@echo ""
	@echo "**** DOCKER PS **** "
	@cd ./srcs/ &&  sudo docker-compose ps -a
	@echo ""
	@echo "**** VOLUMES **** " 
	@sudo docker volume ls
	@echo ""
	@echo "**** NETWORKS **** " 
	@sudo docker network ls

logs:
	sudo docker-compose -f srcs/docker-compose.yml logs

wordpress:
	sudo docker exec -it wordpress bash

mariadb:
	sudo docker exec -it mariadb bash

nginx:
	sudo docker exec -it nginx bash

clean: down
	sudo docker volume rm db && \
	sudo docker volume rm wp

fclean: clean
	sudo docker rmi -f $$(sudo docker images -q)
	sudo docker network rm $$(docker network ls -q)

re: fclean mkdir up