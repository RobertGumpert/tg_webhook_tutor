import json


class ApplicationConfigs(object):
    tg_url: str
    tg_token: str
    deploy_service_domain: str
    deploy_service_webhook_api: str
    tg_api_endpoints: dict

    def __init__(self, data):
        self.__dict__ = json.loads(data)
