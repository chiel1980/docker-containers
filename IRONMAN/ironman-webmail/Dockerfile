FROM alpine:latest
MAINTAINER Michiel van Es <mve@pragmasec.nl>

# 1 - install packages
RUN apk add --update \
    php-fpm \
    php-curl \
    php-json \
    php-dom \
    php-zlib \
    php-iconv \
    php-imap \
    php-openssl \
    php-xml \
    php-mcrypt \
    unzip \
    nginx 

# 2 - download rainloop latest
RUN mkdir -p /usr/share/rainloop
WORKDIR /usr/share/rainloop 
RUN cd /usr/share/rainloop
RUN wget http://repository.rainloop.net/v2/webmail/rainloop-community-latest.zip
RUN unzip rainloop-community-latest.zip

# 3 - configure php-fpm
ADD php-fpm.conf /etc/php/php-fpm.conf
ADD php.ini /etc/php/php.ini

# 4 - configure nginx
ADD nginx.conf /etc/nginx/
ADD webmail.conf /etc/nginx/conf.d/
RUN chown -R nobody /var/lib/nginx

# 5 - copy startup script
ADD startup.sh /root/startup.sh
RUN chmod 755 /root/startup.sh

# 6 - start php-fpm and nginx
ENTRYPOINT ["/root/startup.sh"]
