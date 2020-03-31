#!/bin/bash

SIGN_NUM_LIST=$(ps -ef | grep uwsgi | grep pyenv | awk '{print $2}')
for SIGN_NUM in $SIGN_NUM_LIST; do
    kill -9 $SIGN_NUM
done
/usr/local/nginx/sbin/nginx -s stop