from secret_tokens import my_user_id
import allure


@allure.feature('Send Message')
@allure.story('POST')
def test_send_message(send_message_endpoint):
    text_message = "This is a test message from python autotest"
    with allure.step(f'Send message "{text_message}" without formatting'):
        send_message_endpoint.send_simple_message(my_user_id, text_message)
    with allure.step('Check that status is OK'):
        send_message_endpoint.check_response_status_is_ok()
    with allure.step('Check that message_id is not empty'):
        send_message_endpoint.check_message_id_is_not_empty()
    with allure.step('Check that text is same as sent'):
        send_message_endpoint.check_text_same_as_sent(text_message)


@allure.feature('Send Message')
@allure.story('POST')
def test_send_formatted_message(send_message_endpoint):
    font_styles_dict = {"bold": '*', "italic": '_', "strikethrough": '~', "spoiler": '||'}
    test_text = 'This is a formatted test message from python autotest'

    for font_style in font_styles_dict:
        with allure.step(f'Send message with {font_style} style'):
            send_message_endpoint.send_simple_message(my_user_id, test_text, font_style, font_styles_dict)
        with allure.step('Check that status is OK'):
            send_message_endpoint.check_response_status_is_ok()
        with allure.step('Check that message_id is not empty'):
            send_message_endpoint.check_message_id_is_not_empty()
        with allure.step('Check that text is same as sent'):
            send_message_endpoint.check_text_same_as_sent(test_text)
        with allure.step(f'Check that parse_mode in response = {font_style}'):
            send_message_endpoint.check_type_of_parse_mode(font_style)
