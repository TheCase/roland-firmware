FROM python:alpine3.17

COPY requirements.txt main.py / 
COPY roland_firmware/ /roland_firmware/
RUN pip install -r /requirements.txt 

# sample defaults for models to track
ENV MODELS='juno-x'
VOLUME /content

CMD [ "python", "main.py" ]
