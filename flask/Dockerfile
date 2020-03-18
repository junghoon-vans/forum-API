FROM python:3.7.6


ADD . /www
WORKDIR /www

RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip3 install uwsgi

CMD uwsgi uwsgi.ini
