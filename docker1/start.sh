#!/bin/bash

nginx -g "daemon off;"
uwsgi -d --ini uwsgi.ini