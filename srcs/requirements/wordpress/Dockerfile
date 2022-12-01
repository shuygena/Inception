FROM    debian:buster

RUN apt-get update && apt-get -y upgrade && apt-get -y install \
	vim \
	php7.3 \
	php7.3-fpm \
	php7.3-mysql \
	php7.3-xml \
	wget

COPY    ./tools/start.sh ./

COPY    ./conf/wp-config.php ./

RUN     chmod 777 wp-config.php start.sh

CMD [ "bash", "./start.sh" ]