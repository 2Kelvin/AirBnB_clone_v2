#!/usr/bin/env bash
# Sets up web-servers for web_static deployment
sudo apt -y update
sudo apt -y install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sed -i "/listen 80 default_server;/a location /hbnb_static {alias /data/web_static/current/;}" /etc/nginx/sites-available/default
sudo service nginx restart
