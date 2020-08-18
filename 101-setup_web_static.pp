#!/usr/bin/env bash
#puppet script

exec { 'Nginx setup':
command  => 'sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '29i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\$
sudo service nginx restart',
provider => shell,
}
