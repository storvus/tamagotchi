import logging
from os.path import abspath, dirname, join

DEBUG = True


logging.basicConfig(level=logging.DEBUG if DEBUG else logging.INFO)


REPO_DIR = abspath(dirname(__file__))
RESOURCES_DIR = join(REPO_DIR, "resources")
