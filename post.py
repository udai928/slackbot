import urllib3
import json
import yaml


urllib3.disable_warnings()


with open("config.yml") as file:
    config = yaml.load(file)


body = {
    "token": config["token"],
    "channel": "C5Z78S9DK",
    "text": "hello",
    "username": "angel",
    "icon_url": config["icon"]
}

# url = "https://slack.com/api/chat.postMessage"

jb = json.dumps(body).encode("utf-8")
http = urllib3.PoolManager(num_pools=10)
res = http.request(
    method='POST',
    url=config["hookurl"],
    body=jb,
    headers={"Content-Type": "application/x-www-form-urlencoded"}
)