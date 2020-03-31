FROM ubuntu:16.04

MAINTAINER Wilf

# Install required packages and remove the apt packages cache when done.

RUN apt-get -qq update && DEBIAN_FRONTEND=noninteractive apt-get -y \
    install sudo xvfb \
    git wget virtualenv python3-numpy python3-scipy netpbm \
    python3-pyqt5 ghostscript libffi-dev libjpeg-turbo-progs \
    python3-setuptools \
    python3-dev cmake  \
    python3-pip \
    nginx \
    wget \
    libmysqlclient-dev libtiff5-dev libjpeg8-dev libopenjp2-7-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev \
    libharfbuzz-dev libfribidi-dev && apt-get clean

RUN v=3.7.2 && \
    wget https://mirrors.sohu.com/python/$v/Python-$v.tar.xz && \
    tar -xvf Python-$v.tar.xz && \
    cd Python-$v && \
    ./configure && make && sudo make altinstall && \
    rm -rf /usr/bin/python3 && \
    rm -rf /usr/bin/pip3 && \
    ln -s /usr/local/python3/bin/python3.7 /usr/bin/python3 && \
    ln -s /usr/local/python3/bin/pip3.7 /usr/bin/pip3

RUN virtualenv -p /usr/bin/python3 --system-site-packages /vpy3 && \
    /vpy3/bin/pip install --upgrade pip && \
    /vpy3/bin/pip install cffi olefile pytest pytest-cov && \
    /vpy3/bin/pip install numpy --only-binary=:all: || true

# install uwsgi now because it takes a little while
RUN /vpy3/bin/pip install uwsgi

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY nginx-app.conf /etc/nginx/sites-available/default

# 创建工作路径
RUN mkdir -p /var/www

COPY site_demo-1.2.tar.gz /var/www

RUN cd /var/www && \
    tar -xvf site_demo-1.2.tar.gz && \
    mv site_demo-1.2 site_demo

# 指定容器启动时执行的命令都在/var/www/site_demo目录下执行
WORKDIR /var/www/site_demo

RUN /vpy3/bin/pip install -r /home/docker/code/app/requirements.txt -i  https://pypi.tuna.tsinghua.edu.cn/simple some-package --no-cache-dir

EXPOSE 80

CMD ["/bin/bash","start.sh"]