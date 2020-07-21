"""API Tests for get status code"""


def test_api_status_code(api_client):
    response = api_client.get()
    assert response.ok
