from bs4 import BeautifulSoup
import urllib.request
import re

import logging
fmt = "%(asctime)s - %(levelname)-s - %(message)s"
logging.basicConfig(level=logging.INFO, format=fmt)
log = logging.getLogger(__name__)


def get_content(url):
    try:
        html_page = urllib.request.urlopen(url)
    except Exception as e:
        raise SystemExit(e)
    try:
        soup = BeautifulSoup(html_page, "html.parser")
    except Exception as e:
        raise SystemExit(e)
    return soup


def firmware_link(model, url):
    soup = get_content(url)
    drivers = soup.find("section", {"id": "dl-drivers"})
    if not drivers:
        log.error(f"No drivers section found for: '{model}' url: {url}")
        raise SystemExit("Abort")
    for item in drivers.findAll('h5'):
        for link in item.findAll('a'):
            if 'System Program' in link.string:
                return link.get('href')


def firmware_info(url):
    soup = get_content(url)
    content = soup.text
    for line in content.split('\n'):
        log.debug(line)
        regex = r"^\s*?\[\s?Ver\.([0-9\.]+)\s?\]\s?(.*)$"
        match = re.match(regex, line)
        if match:
            return url, match
    log.error("no match found.  Abort.")
    exit


def get_latest(model):
    support_base = "https://www.roland.com/global/support/by_product"
    support_url = "{0}/{1}/updates_drivers".format(support_base, model)
    firmware_url = "https://www.roland.com{0}".format(
        firmware_link(model, support_url))
    log.info("{} fw url: {}".format(model, firmware_url))
    return firmware_info(firmware_url)
