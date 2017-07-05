from logging import getLogger
from logging import basicConfig
from logging import INFO
import yaml
import os

class Command:
    def __init__(self):
        with open("config.yml") as file:
            log_path = yaml.load(file)['log_path']

        basicConfig(filename=log_path + "info.log", level=INFO)
        self.logger = getLogger(__name__)

    def run(self, cmd):
        self.logger.info("start : " + cmd)
        try:
            result = os.system(cmd)
            self.logger.info(result)
            self.logger.info("finish successfully")
        except:
            self.logger.info("failed")
        finally:
            print("command finish")
