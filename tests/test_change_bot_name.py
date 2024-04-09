import allure


@allure.feature('Change bot name')
@allure.story('POST')
def test_set_bot_name(set_bot_name_endpoint):
    new_test_name = "test bot name"
    with allure.step(f'Set name = {new_test_name}'):
        set_bot_name_endpoint.set_bot_name(new_test_name)
    with allure.step('Check that response status is OK'):
        set_bot_name_endpoint.check_response_status_is_ok()
    with allure.step('Check that result in response is true'):
        set_bot_name_endpoint.check_response_result_is_true()


@allure.feature('Change bot name')
@allure.story('GET')
def test_get_bot_name(get_bot_name_endpoint, set_bot_name_for_get_name):
    test_name = set_bot_name_for_get_name
    with allure.step(f'Get name, expected result = {test_name}'):
        get_bot_name_endpoint.get_bot_name()
    with allure.step('Check that response status is OK'):
        get_bot_name_endpoint.check_response_status_is_ok()
    with allure.step(f'Check that name in response is as sent name {test_name}'):
        get_bot_name_endpoint.check_name_as_sent(test_name)
