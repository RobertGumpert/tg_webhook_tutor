import logging
from flask import Flask, request
import telegram_client.web_hook as webHookClient
from telegram_client.configs import ApplicationConfigs

logging.getLogger().setLevel(logging.INFO)
with open("C:/github-repos/tg_webhook_tutor/configs/tg-webhook-configs.json", 'r') as read_file:
    configs = ApplicationConfigs(read_file.read())
webHookClient.set_follow_updates_by_web_hook(configs, 'api/tg/bot/webhook/updates')
app = Flask(__name__)


@app.route('/api/tg/bot/webhook/updates', methods=["GET", "POST"])
def update():
    webHookClient.response_to_user(configs, user_request=request.json)
    return {"ok": True}


logging.info(app.url_map)
if __name__ == '__main__':
    app.run()
