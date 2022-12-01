FROM    debian:buster

RUN     apt-get update && apt-get -y upgrade && apt-get -y install \
	    vim \
	    nginx \
	    openssl 

COPY    ./tools/start.sh ./

COPY    ./conf/nginx.conf ./

RUN     chmod 777 start.sh nginx.conf && \
        mv ./nginx.conf /etc/nginx/sites-enabled/default

EXPOSE  443

CMD     [ "bash", "./start.sh" ]