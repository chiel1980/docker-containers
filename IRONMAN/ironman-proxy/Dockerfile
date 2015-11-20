FROM alpine:latest
MAINTAINER MvE
RUN apk --update add ca-certificates nginx 
# Create a self signed cert for Nginx - replace with valid cert later on
VOLUME /etc/ssl/
#ADD certs/*.pragmasec.nl-bundle.crt /etc/ssl/certs/
#ADD certs/*.pragmasec.nl.key /etc/ssl/private/

# LETS config nginx in front of Django as a proxy
ADD ironman.conf /etc/nginx/conf.d/
ADD nginx.conf /etc/nginx/

# Fix ugly proxy bug
RUN chown -R nobody.nobody /var/lib/nginx

# EXPOSE our PORTS
EXPOSE 80 443 
# Run the service
CMD ["nginx", "-g", "daemon off;"]
