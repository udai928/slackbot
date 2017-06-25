from slackbot.bot import respond_to
from slackbot.bot import default_reply
import os

# respond_to
# botに向けた投稿で引数の文字列が含まれる時に反応する
#
# listen_to
# 参加しているチャネルでbot以外に向けた投稿以外で引数の文字列が含まれる時に反応する


@default_reply()
def default_reply(message):
    text = message.body['text']
    message.reply('```' + text + '```')


@respond_to('こんにちは')
def reply_hello(message):
    message.reply("こんにちは!!!!")


@respond_to('^deploy\s\d{2}')
def deploy(message):
    tag = message.body['text'].split(' ')[1]
    message.send("START DEPLOY. Tag is " + tag)
    result = __deploy__(tag)
    message.send("FINISH DEPLOY. result = " + result)


def __deploy__(tag):
    deploy_cmd = ""  # Todo
    result = "success"
    try:
        os.system(deploy_cmd)
    except Exception:
        print("command failed :" + deploy_cmd)
        result = "failed"
    return result

