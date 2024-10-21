#!/usr/bin/env python

from datetime import datetime
from roland_firmware.parse import get_latest
from jinja2 import Environment, FileSystemLoader
import os

import logging
fmt = "%(asctime)s - %(levelname)-s - %(message)s"
logging.basicConfig(level=logging.INFO, format=fmt)
log = logging.getLogger(__name__)

issues_link = "https://github.com/TheCase/roland-firmware/issues"


def fetch_data(models):
    log.info("starting data fetch.")
    data = dict()
    models.sort()
    for model in models:
        label = model.upper()
        log.info("fetching info for {}".format(label))
        url, info = get_latest(model)
        version = "{} {}".format(info[1], info[2])
        log.info("latest for {0}: {1}".format(label, version))
        data[model] = {"url": url, "version": info[1], "date": info[2]}
    log.info("data fetch complete.")
    return (data)


def template(data):
    log.info("starting html render")
    file_loader = FileSystemLoader('.')
    env = Environment(loader=file_loader, autoescape=True)
    template = env.get_template('roland_firmware/templates/index_html.jinja')
    today = datetime.utcnow().strftime("%B %d %Y %H:%M:%S UTC")
    content = template.render(data=data, today=today, issues_link=issues_link)
    return (content)


def write_content(location, content):
    directory = os.path.dirname(location)
    if not os.path.exists(directory):
        os.mkdir(directory)
    f = open(os.path.join(location), "w")
    f.write(content)
    f.close()
    log.info("wrote out html file")


def create_html(models, filename):
    data = fetch_data(models)
    content = template(data)
    write_content(filename, content)
