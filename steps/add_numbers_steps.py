from behave import given, when, then
import requests

@given('tôi truy cập vào API cộng số')
def step_given_api(context):
    context.url = 'http://localhost:5000/add'

@when('tôi gửi yêu cầu GET tới "{endpoint}"')
def step_when_send_request(context, endpoint):
    context.response = requests.get(f"{context.url}{endpoint}")

@then('tôi nhận được kết quả "{expected_result}"')
def step_then_check_result(context, expected_result):
    assert context.response.json()['result'] == int(expected_result)
