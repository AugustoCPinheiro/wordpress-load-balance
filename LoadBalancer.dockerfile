FROM nginx

ENV CONF_PATH /etc/nginx

COPY ./config/nginx.conf ${CONF_PATH}/

