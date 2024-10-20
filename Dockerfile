FROM python:alpine3.17

COPY requirements.txt main.py roland_firmware / 

RUN apk --no-cache add g++ && \
    pip install -r /requirements.txt && \
    apk del g++

# sample defaults for models to track
ENV MODELS='juno-x'

VOLUME /content

CMD [ "python", "main.py" ]
