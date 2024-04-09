import requests
from endpoints.base_endpoint_class import Endpoint
from secret_tokens import bot_token
from logger import log
from json_schemas.send_message_schema import valid_schema
from jsonschema import validate


class SendMessageEndpoint(Endpoint):
    """ Отправка простого и форматированного сообщения"""
    resource = '/sendMessage'
    url_endpoint = Endpoint.base_url + bot_token + resource
    message_id = None
    sent_text_message = None
    sent_parse_mode = None

    def send_simple_message(self, user_id, text_message, font_style=None, font_styles_dict=None):
        if font_style:
            json_body = {
                "chat_id": user_id,
                "text": self.create_formatted_text(text_message,
                                                   symbol=self.get_symbol_from_font_style(font_styles_dict,
                                                                                          font_style)),
                "disable_notification": "true",
                "parse_mode": "MarkdownV2"
            }
            response = requests.post(self.url_endpoint, json=json_body)
            self.sent_parse_mode = response.json()['result']['entities'][0]['type']
        else:
            json_body = {
                "chat_id": user_id,
                "text": text_message,
                "disable_notification": "true"
            }
            response = requests.post(self.url_endpoint, json=json_body)
        validate(instance=response.json(), schema=valid_schema)
        self.status = response.status_code
        self.message_id = response.json()['result']['message_id']
        self.sent_text_message = response.json()['result']['text']
        log(response=response, request_body=json_body)
        return response

    def check_message_id_is_not_empty(self):
        assert self.message_id is not None, "Expected that message_id is not empty"

    def check_text_same_as_sent(self, text_message):
        assert self.sent_text_message == text_message, (f"Expected text : {text_message}, "
                                                        f"actual text: {self.sent_text_message}")

    def check_type_of_parse_mode(self, font_style):
        assert self.sent_parse_mode == font_style, (f"Expected parse_mode : {font_style}, "
                                                    f"actual parse_mode: {self.sent_parse_mode}")

    @staticmethod
    def create_formatted_text(text, symbol):
        return symbol + text + symbol

    @staticmethod
    def get_symbol_from_font_style(font_styles_dict, font_style):
        return font_styles_dict.get(font_style)
