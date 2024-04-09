import pytest
from endpoints.send_message_endpoint import SendMessageEndpoint
from endpoints.set_bot_name import SetBotName
from endpoints.get_bot_name import GetBotName
import random
import string


@pytest.fixture
def send_message_endpoint():
    return SendMessageEndpoint()


@pytest.fixture
def set_bot_name_endpoint():
    return SetBotName()


@pytest.fixture
def get_bot_name_endpoint():
    return GetBotName()


@pytest.fixture
def random_string():
    return "".join(random.choice(string.ascii_lowercase) for _ in range(5))


@pytest.fixture
def set_bot_name_for_get_name(set_bot_name_endpoint, random_string):
    new_test_name = f"new_test_name_{random_string}"
    set_bot_name_endpoint.set_bot_name(new_test_name)
    return new_test_name
