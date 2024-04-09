from endpoints.base_endpoint_class import Endpoint
from secret_tokens import bot_token
from logger import log
import requests
from json_schemas.get_bot_name_schema import valid_schema
from jsonschema import validate


class GetBotName(Endpoint):
    """Получение и проверка текущего имени бота """
    resource = '/getMyName'
    url_endpoint = Endpoint.base_url + bot_token + resource
    name = None

    def get_bot_name(self):
        response = requests.get(self.url_endpoint)
        validate(instance=response.json(), schema=valid_schema)
        self.status = response.status_code
        self.name = response.json()['result']['name']
        log(response=response)
        return response

    def check_name_as_sent(self, test_name):
        assert self.name == test_name, f"Expected name: {test_name}, actual name: {self.name}"
