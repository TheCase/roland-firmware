FROM python:3

COPY requirements.txt template.jinja render.py / 
RUN pip install -r /requirements.txt

# sample defaults for models to track
ENV MODELS='juno-x'

CMD [ "python", "/render.py" ]
