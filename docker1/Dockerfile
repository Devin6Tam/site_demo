FROM registry.cn-hangzhou.aliyuncs.com/txtxw/alpine-python:v3

RUN apk --no-cache add python3 \
       build-base \
       python3-dev \
       # wget dependency
       openssl \
       # dev dependencies
       git \
       bash \
       sudo \
       py3-pip \
       # Pillow dependencies
       jpeg-dev \
       zlib-dev \
       freetype-dev \
       lcms2-dev \
       openjpeg-dev \
       tiff-dev \
       tk-dev \
       tcl-dev \
       harfbuzz-dev \
       fribidi-dev

# 创建工作路径
RUN mkdir -p /var/www

COPY site_demo-1.1.tar.gz /var/www

RUN cd /var/www && \
    tar -xvf site_demo-1.1.tar.gz && \
    mv site_demo-1.1 site_demo

# 指定容器启动时执行的命令都在/var/www/site_demo目录下执行
WORKDIR /var/www/site_demo

# 替换nginx的配置
RUN cp -r nginx.conf /etc/nginx/nginx.conf


# pip读取requirements.txt内容安装所需的库
RUN pip3 install -r requirements.txt -i  https://mirrors.aliyun.com/pypi/simple/ --no-cache-dir

EXPOSE 80

# 启动nginx和uwsgi
ENTRYPOINT ["/bin/bash","start.sh"]