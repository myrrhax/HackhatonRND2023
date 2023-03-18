FROM python:latest

WORKDIR /src
COPY requirements.txt /src
RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y cmake
RUN pip install --upgrade setuptools
RUN python setup.py install --no DLIB_GIF_SUPPORT
RUN pip install -r requirements.txt
COPY . /src

RUN python main.py