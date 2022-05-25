FROM python:3

COPY requirements.txt template.jinja render.py / 
RUN pip install -r /requirements.txt

# sample defaults for models to track
ENV MODELS='jd-08,jx-08'

CMD [ "python", "/render.py" ]
