import os
from roland_firmware.render import create_html


if __name__ == "__main__":
    models = os.getenv('MODELS', "juno-x").split(',')
    create_html(models, 'content/index.html')
