from behave import given, when, then
import requests
import json

# Store the request data in a variable to pass it to the POST request
request_data = {}

@given('I have the following request data:')
def step_given_have_request_data(context):
    for row in context.table:
        request_data[row['name']] = row['value']

@when('I send a POST request to "{url}"')
def step_when_send_post_request(context, url):
    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=json.dumps(request_data))
    context.response = response

@then('the response should be JSON:')
def step_then_response_should_be_json(context):
    expected_json = json.loads(context.text)
    actual_json = context.response.json()
    assert actual_json == expected_json, f"Expected JSON: {expected_json}, Actual JSON: {actual_json}"
