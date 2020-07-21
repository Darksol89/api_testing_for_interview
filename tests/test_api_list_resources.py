"""API test for get list all resources"""
from support.assertions import assert_valid_schema


def test_api_list_all_resources(api_client):
    response = api_client.get()
    json_data = response.json()

    assert_valid_schema(json_data)
