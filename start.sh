#!/bin/bash

source ~/.bash_profile
/usr/local/nginx/sbin/nginx -g "daemon off;" && $HOME/.pyenv/shims/uwsgi --ini uwsgi.ini