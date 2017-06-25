import yaml

with open("config.yml") as file:
    config = yaml.load(file)

DEFAULT_REPLY = "default reply"
API_TOKEN = config["bot_api_token"]
PLUGINS = ['plugins']