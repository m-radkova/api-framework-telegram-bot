from endpoints.base_endpoint_class import Endpoint
from secret_tokens import bot_token
import requests
from logger import log
from json_schemas.set_bot_name_schema import valid_schema
from jsonschema import validate


class SetBotName(Endpoint):
    """Изменение имени бота"""
    resource = '/setMyName'
    url_endpoint = Endpoint.base_url + bot_token + resource
    result = None

    def set_bot_name(self, new_name):
        json_body = {"name": new_name}
        response = requests.post(
            self.url_endpoint,
            json=json_body
        )
        validate(instance=response.json(), schema=valid_schema)
        self.status = response.status_code
        self.result = response.json()['result']
        log(response=response, request_body=json_body)
        return response

    def check_response_result_is_true(self):
        assert self.result, f"Expected that result is true, actual result = {self.result}"
