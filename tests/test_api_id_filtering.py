"""API Tests for get correct id"""
import pytest


@pytest.mark.parametrize('id', [5], ids=['id: 5'])
def test_api_id_filtering(api_client, id):
    """Test for getting resources with id"""
    response = api_client.get(params={'id': id})
    json_data = response.json()

    assert json_data[0]["id"] == 5

@pytest.mark.parametrize('id', [-1, 0, 'a'])
def test_api_invalid_id_filtering(api_client, id):
    """Test for no getting resources with invalid id"""
    response = api_client.get(params={'id': id})
    json_data = response.json()

    assert json_data == []