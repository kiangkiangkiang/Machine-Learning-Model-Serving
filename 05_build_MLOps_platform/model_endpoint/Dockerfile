FROM nvidia/cuda:12.4.1-devel-ubuntu22.04

COPY ./ /app
WORKDIR /app

RUN apt-get update && apt-get -y install python3.10 python3-pip git gettext
RUN pip install -r requirements.txt

CMD ["uwsgi", "--ini", "uwsgi_config.ini"]

