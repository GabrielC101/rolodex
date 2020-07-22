FROM ubuntu:18.04

# Install Python and Package Libraries
RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean
RUN apt-get install -y \
    build-essential \
    libffi-dev \
    libssl-dev \
    libmysqlclient-dev \
    libxml2-dev \
    libxslt-dev \
    libjpeg-dev \
    libfreetype6-dev \
    zlib1g-dev \
    net-tools \
    vim \
    python3.6 \
    python3-pip \
    python3.6-venv

COPY ./requirements/requirements.txt /app/requirements/requirements.txt

WORKDIR /app

RUN pip3 install -U pip
RUN pip3 install -r requirements/requirements.txt

COPY . /app

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

CMD ["/usr/bin/make", "run-no-venv"]

