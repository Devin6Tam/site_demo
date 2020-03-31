#!/bin/bash

source ~/.bash_profile
nginx -g "daemon off;"
$HOME/.pyenv/shims/uwsgi -d --ini uwsgi.ini