FROM ubuntu:latest

WORKDIR /application

ARG PYTHON_VERSION
#COPY sample_python .

#RUN apt-get update -y && \
 #   apt-get install -y python3-pip python3-dev

RUN set -x \
    && pythonVersions=python$PYTHON_VERSION \
    && apt-get update \
    && apt-get install -y --no-install-recommends software-properties-common \
    && apt-get update \
    && add-apt-repository universe \
    && apt-get install -y --no-install-recommends $pythonVersions \
    && apt-get install -y python3-pip python3-dev \
    && apt-get install -y curl \
    && curl https://bootstrap.pypa.io/get-pip.py --output get-pip.py \
    && python3 get-pip.py \
    && pip3 install pylint \
    && pip3 install pytest \
    && pip3 install --ignore-installed six \
    && apt-get purge -y --auto-remove software-properties-common \
    && rm -rf /var/lib/apt/lists/*  

