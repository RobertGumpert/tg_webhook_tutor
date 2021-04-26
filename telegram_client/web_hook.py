import json
import logging
import os
import requests

from telegram_client.configs import ApplicationConfigs


def set_follow_updates_by_web_hook(configs: ApplicationConfigs, endpoint: str):
    tg_api_url = create_telegram_url(configs, configs.tg_api_endpoints['set_follow_for_updates'])
    service_update_url = f'{configs.deploy_service_domain}/{endpoint}'
    response = requests.post(tg_api_url, data={
        'url': service_update_url
    })
    json_body_response = response.json()
    if response.status_code != 200:
        logging.error(json)
        os._exit(1)
    logging.info(json_body_response)
    return


def response_to_user(configs: ApplicationConfigs, user_request):
    tg_api_url = create_telegram_url(configs, configs.tg_api_endpoints['send_message_to_client'])
    user_message = user_request['message']['text']
    response_data = {
        "chat_id": user_request['message']['chat']['id'],
        "text": f'"{user_message}", ага ну сам туда иди...'
    }
    response = requests.post(tg_api_url, data=response_data)
    if response.status_code != 200:
        logging.error(response.json())
        return
    logging.info(response.json())
    return


def create_telegram_url(configs: ApplicationConfigs, endpoint: str):
    return f'{configs.tg_url}{configs.tg_token}/{endpoint}'
