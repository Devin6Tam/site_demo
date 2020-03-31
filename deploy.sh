#!/bin/bash

# 将windows下的文件转成unix格式
sed -i 's/\r//' *.sh

# 环境安装
if [ "$IS_DEPLOY" != "1" ]; then
  sh install.sh
fi

######################################应用部署############################################
# 应用部署目录，解压应用包，进入部署目录，以进入下一步操作
mkdir -p /var/www/log && \
  cd /var/www/  && \
  cp ~/site_demo-1.0.tar.gz ./ && \
  tar -xvf site_demo-1.0.tar.gz && \
  mv site_demo-1.0 site_demo && \
  cd site_demo  && \
  cp -r nginx.conf /usr/local/nginx/conf/nginx.conf
  pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

source ~/.bash_profile
# 静态文件访问调整（一般使用内置的admin，静态文件资源访问有异常，需要调整访问）
python manage.py collectstatic && \
    cp -r /static/* /var/www/site_demo/static/