# Puppet code for tasks0: servers set up

exec { 'running my shell code':
  command  => 'sudo apt -y update;
              sudo apt -y install nginx;
              sudo mkdir -p /data/web_static/releases/test/;
              sudo mkdir -p /data/web_static/shared/;
              echo "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body\n</html>" \
              > /data/web_static/releases/test/index.html;
              sudo ln -sf /data/web_static/releases/test/ /data/web_static/current;
              sudo chown -R ubuntu:ubuntu /data/;
              sed -i "/listen 80 default_server;/a location /hbnb_static {alias /data/web_static/current/;}" \
              /etc/nginx/sites-available/default;
              sudo service nginx restart',
  provider => shell
}
