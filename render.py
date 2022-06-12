import os
import time
from bs4 import BeautifulSoup
import urllib.request
import re
from datetime import datetime

from numpy import datetime_as_string
from jinja2 import Environment, FileSystemLoader

import logging
fmt="%(asctime)s - %(levelname)-s - %(message)s"
logging.basicConfig(level=logging.INFO, format=fmt)
log = logging.getLogger(__name__)

issues_link = "https://github.com/TheCase/roland-firmware/issues" 
models = os.getenv('MODELS',"juno-x").split(',')

def get_content(url):    
   html_page = urllib.request.urlopen(url)
   return BeautifulSoup(html_page, "html.parser")

def firmware_link(url):
  soup = get_content(url)
  drivers = soup.find("section", {"id": "dl-drivers"})

  for item in drivers.findAll('h5'):
    for link in item.findAll('a'):
      if 'System Program' in link.string:
        return link.get('href')
  log.error("no link found.  Abort.")
  exit

def firmware_info(url):
  soup = get_content(url)
  content = soup.text
  for line in content.split('\n'):
    log.debug(line)
    regex = r"^\[ Ver\.([0-9\.]+) \]\s?(.*)$"
    match = re.match(regex, line)
    if match:
      return url, match
  log.error("no match found.  Abort.")
  exit
      
def get_latest(model):
  support_url = "https://www.roland.com/global/support/by_product/{0}/updates_drivers".format(model)
  firmware_url = "https://www.roland.com{0}".format(firmware_link(support_url))
  log.info("{} fw url: {}".format(model, firmware_url))
  return firmware_info(firmware_url)

def write_content(content):
  directory = './content'
  if not os.path.exists(directory):
    os.mkdir(directory) 
  f = open(os.path.join(directory,"index.html"), "w")
  f.write(content)
  f.close()
  log.info("wrote out html file")

def render(data):
  log.info("starting html render")
  file_loader = FileSystemLoader('.')
  env = Environment(loader=file_loader)
  template = env.get_template('template.jinja')
  today = datetime.utcnow().strftime("%B %d %Y %H:%M:%S UTC")
  content = template.render(data=data, today=today, issues_link=issues_link)
  write_content(content)
  log.info("completed html render")

def main(models):
  log.info("starting data fetch.")
  data = dict()
  models.sort()
  for model in models:
    label = model.upper()
    log.info("fetching info for {}".format(label))
    url, info = get_latest(model)
    version = "{} {}".format(info[1], info[2])
    log.info("latest for {0}: {1}".format(label, version))
    data[model] = { "url": url, "version": info[1], "date": info[2] }
  log.info("data fetch complete.")
  # data['ob-1'] = { "url": 'foo.com', "version": '1.10', "date": 'SEP 1970' }
  render(data)

if __name__ == "__main__":
  main(models)
