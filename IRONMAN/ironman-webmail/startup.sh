#!/bin/sh

# 1 start up php-fpm
/usr/bin/php-fpm -c /etc/php/php.ini -y /etc/php/php-fpm.conf

# 2 fix permissions
cd /usr/share/rainloop
find . -type d -exec chmod 755 {} \;
find . -type f -exec chmod 644 {} \;
chown -R nobody:nogroup /usr/share/rainloop

# 3 start up nginx
nginx -g 'daemon off;'
