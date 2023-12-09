#!/usr/bin/env bash
# Install Nginx and set up the file system

# Install nginx if not  installed
apt-get update
apt-get -y install nginx

# Set up the file system
DIRS=("/data/web_static/shared/" "/data/web_static/releases/test/")
for dir in "${DIRS[@]}"; do
    if [ ! -d "$dir" ]; then
        mkdir -p "$dir"
    fi
done

link_path="/data/web_static/current"
target_path="/data/web_static/releases/test"
ln -sf "$target_path" "$link_path"

# Set up file permissions
chown -R ubuntu /data/
chgrp -R ubuntu /data/

echo "Go tell to Sparta, thou who passest by, that here, obedient to her laws, we lie" > /data/web_static/releases/test/index.html

# Create file to be served in case of an error 404
echo "Ceci n'est pas une page" > /etc/nginx/html/404.html

# Create the default index page
echo "Hello World!" > /etc/nginx/html/index.html;

echo "server {
    listen 80;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root /etc/nginx/html;

    

    index index.html index.htm index.nginx-debian.html;

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=lBP7QQYN1IU;
    }

    error_page 404 /404.html;
    location /404 {
      root /etc/nginx/html;
      internal;
    }

    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html index.htm;
    }
}" > /etc/nginx/sites-available/default

service nginx restart

