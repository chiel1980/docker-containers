FROM alpine:latest
MAINTAINER MvE
RUN apk add --update --update-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ prosody shadow 
ADD prosody.cfg.lua /etc/prosody/
ADD sharedgroups.txt /etc/prosody/
RUN groupmod -g 118 prosody
RUN usermod -u 111 prosody
RUN chown -R prosody /etc/prosody/ /var/lib/prosody/ /var/log/prosody/ /var/run/prosody/
EXPOSE 5222 
CMD ["prosodyctl", "start"]
