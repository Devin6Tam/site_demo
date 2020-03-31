#!/bin/bash

# 更新镜像源，安装依赖库
yum --disablerepo="epel" update ca-certificates && \
    yum install -y epel-release && \
    yum makecache && \
    yum -y install gcc gcc-c++ make patch gdbm-devel openssl-devel gcc-devel python-devel \
        sqlite-devel readline-devel zlib-devel bzip2-devel pcre-devel gd-devel mysql-devel \
        ncurses xz libffi-devel iproute net-tools telnet wget curl

# 安装git，下载pyenv(pyenv 下载比较慢，建议网速慢可以使用已经下载好的包)
yum -y install git && \
   git clone https://github.com/pyenv/pyenv.git ~/.pyenv && \
   echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile && \
   echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile && \
   echo 'export IS_DEPLOY="1"' >> ~/.bash_profile && \
   echo 'eval "$(pyenv init -)"' >> ~/.bash_profile

# 设置环境变量，安装python
source ~/.bash_profile && \
    v=3.7.2;wget http://mirrors.sohu.com/python/$v/Python-$v.tar.xz -P $(pyenv root)/cache/; pyenv install $v  && \
    pyenv global $v

# 配置pip并升级
 echo '[global]' >> ~/.pip/pip.conf && \
    echo 'index-url=https://mirrors.aliyun.com/pypi/simple/' >> ~/.pip/pip.conf && \
    echo 'trusted-host=mirrors.aliyun.com' >> ~/.pip/pip.conf && \
    pip install --upgrade pip && \
    pip install uwsgi

# 下载并安装nginx
wget https://mirrors.sohu.com/nginx/nginx-1.17.9.tar.gz && \
    tar zxf nginx-1.17.9.tar.gz && \
    cd nginx-1.17.9 && \
    ./configure --prefix=/usr/local/nginx \
    --with-http_ssl_module \
    --with-http_stub_status_module && \
    make -j 4 && make install && \
    rm -rf /usr/local/nginx/html/* && \
    echo "ok" >> /usr/local/nginx/html/status.html && \
    cd / && rm -rf nginx-1.17.9*
