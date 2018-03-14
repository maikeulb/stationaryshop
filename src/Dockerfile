FROM ubuntu:latest

COPY . /app
WORKDIR /app

RUN apt-get update  \
  && apt-get install -y curl  \
  && curl -sL https://deb.nodesource.com/setup_8.x | bash -  \
  && apt-get install -y nodejs 

RUN npm install --unsafe-perm -g webpack@3.9.1
RUN npm install --silent
RUN npm run build

RUN apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

RUN pip3 install gunicorn
RUN pip3 install -r requirements.txt

RUN chmod +x entrypoint.sh

ENV FLASK_APP=stationaryshop.py
ENV FLASK_APP_CONFIG=config.ProductionConfig
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

EXPOSE 5000
ENTRYPOINT ["./entrypoint.sh"]
