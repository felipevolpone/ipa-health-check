
import sys
import logging
import subprocess
from subprocess import Popen


def create_logger():
    root = logging.getLogger('ipa-hc')
    root.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s \
- %(message)s')
    console_handler.setFormatter(formatter)

    root.addHandler(console_handler)


def get_logger():
    return logging.getLogger('ipa-hc')


def execute(command):
    processor = Popen(command, stderr=None, stdout=subprocess.PIPE, shell=True)
    return processor.communicate()