FROM 	debian:buster

RUN 	apt-get update && apt-get -y upgrade && apt-get -y install \
		vim \
		default-mysql-server

COPY 	./tools/start.sh ./

RUN 	chmod 777 start.sh

CMD 	[ "bash", "./start.sh" ]