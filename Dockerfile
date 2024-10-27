FROM ubuntu:22.04

USER root
ARG DEBIAN_FRONTEND=noninteractive
ARG GID=1000
ARG UID=1000
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV SHELL="/bin/bash"
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt update -y > /dev/null && \
    apt install -y bzip2 ca-certificates curl expect ftp git gnupg iptables && \
    apt install -y libgomp1 libpopt0 libxml2-dev libxslt1-dev && \
    apt install -y pandoc psmisc python3 python3-dev python3-pip python3-venv && \
    apt install -y sudo unzip vim xz-utils zip zlib1g
RUN apt autoremove --purge -y > /dev/null && \
    apt autoclean -y > /dev/null && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/log/* && \
    rm -rf /tmp/*
RUN echo "alias pip=pip3" | tee --append /etc/bash.bashrc && \
    echo "alias python=python3" | tee --append /etc/bash.bashrc && \
    echo "StrictHostKeyChecking no" | tee --append /etc/ssh/ssh_config && \
    echo "craftslab ALL=(ALL) NOPASSWD: ALL" | tee --append /etc/sudoers && \
    echo "dash dash/sh boolean false" | debconf-set-selections && \
    DEBIAN_FRONTEND=noninteractive dpkg-reconfigure dash && \
    groupadd -g $GID craftslab && \
    useradd -d /home/craftslab -ms /bin/bash -g craftslab -u $UID craftslab
RUN pip install -U pyinstaller

USER craftslab
WORKDIR /home/craftslab
RUN curl -L https://github.com/ai-shflow/shcache/archive/refs/heads/main.zip -o shcache.zip && \
    unzip shcache.zip && \
    mv shcache-main src && \
    cd src; make install; cd .. && \
    cp src/dist/* . && \
    cp src/shcache/config/*.yml . && \
    sudo rm -rf src *.zip
