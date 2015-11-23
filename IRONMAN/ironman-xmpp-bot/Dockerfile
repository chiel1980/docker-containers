FROM alpine:latest
MAINTAINER Michiel van Es <mve@pragmasec.nl>

RUN apk add --update \
    ca-certificates \
    python \
    python-dev \
    py-pip \
    musl-dev \
    libffi-dev \
    openssl-dev \
    build-base 

RUN rm -rf /var/cache/apk/*
RUN pip install errbot sleekxmpp pyasn1 pyasn1-modules dnspython feedparser beautifulsoup json urllib2
VOLUME /etc/err-plugins
VOLUME /var/lib/err
VOLUME /var/log/err

RUN addgroup -g 1003 err 
RUN adduser -h /home/err -s /bin/sh -u 1002 -G err -D err err
WORKDIR /home/err
RUN chown -R err /home/err /var/lib/err /var/log/err
RUN chmod 750 /var/lib/err /var/log/err

ADD config.py /home/err
USER err

CMD "errbot"
