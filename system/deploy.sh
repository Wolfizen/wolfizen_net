#!/bin/sh
# Deploy the wolfizen_net website

# Script setup
alias source=.


## Stop website service
systemctl stop wolfizen_net


## Clean old files and get new version
cd /srv
rm -rf ./wolfizen_net
git clone https://github.com/Wolfizen/wolfizen_net.git ./wolfizen_net


## Production setup
cd wolfizen_net/
python3 -m virtualenv --python=python3 ./env
source ./env/bin/activate
python3 -m pip install -r ./requirements.txt
./manage.py collectstatic
chown -R http:http .

## Start website service
systemctl start wolfizen_net
