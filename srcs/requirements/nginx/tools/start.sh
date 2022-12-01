#!/bin/bash

mkdir -p /etc/nginx/ssl

openssl req -newkey rsa:2048 -nodes \
	-subj /C=RU/ST=Tatarstan/L=Kazan/O=School21/CN=mskeleto \
	-keyout /etc/nginx/ssl/cert.key -x509 \
	-days 365 -out /etc/nginx/ssl/cert.crt

exec nginx -g 'daemon off;'