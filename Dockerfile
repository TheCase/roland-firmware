FROM python:3.12-rc-slim-buster

COPY requirements.txt template.jinja render.py / 

RUN apt-get update && \
    apt-get -y install g++ && \
    pip install -r /requirements.txt && \
    apt-get -y remove g++ && \
    apt-get -y autoremove && \
    rm -rf /var/apt/cache

# sample defaults for models to track
ENV MODELS='juno-x'

VOLUME /content

CMD [ "python", "/render.py" ]
