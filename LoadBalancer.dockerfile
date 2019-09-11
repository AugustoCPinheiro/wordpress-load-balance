FROM nginx

ENV CONF_PATH /etc/nginx/conf.d

COPY ./config/load-balancer.conf ${CONF_PATH}/

RUN mv ${CONF_PATH}/default.conf ${CONF_PATH}/default.conf.disabled