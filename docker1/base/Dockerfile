# 配置基础镜像
FROM alpine:3.11

# 添加标签说明
LABEL author="txtxw" email="devin7tan@163.com"  purpose="nginx+uwsgi+Python3基础镜像"

# 配置阿里云像地址
RUN echo "https://mirrors.aliyun.com/alpine/v3.11/main/" > /etc/apk/repositories

# 更新升级软件
RUN apk add --update --upgrade

# 安装软件
RUN apk add --no-cache nginx python3 uwsgi uwsgi-python3 mariadb-dev py3-pip gcc python3-dev musl-dev

# 更新时区
RUN apk add --update --no-cache tzdata && \
    cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

# 升级pip，这一步同时会在/usr/bin/目录下生成pip可执行文件
RUN pip3 install --no-cache-dir --upgrade pip -i https://mirrors.aliyun.com/pypi/simple/

# 建立软链接
RUN ln -s /usr/bin/python3 /usr/bin/python