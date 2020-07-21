"""API Tests for get correct user ID"""
import pytest


@pytest.mark.parametrize('valid_userId', [10], ids=['UserID: 10'])
def test_api_user_id_filtering(api_client, valid_userId):
    """Test for getting resources with correct ID"""
    response = api_client.get(params={'userId': valid_userId})
    data = response.json()
    for number, item in enumerate(data):
        assert item['userId'] == valid_userId, f'Something trouble with object {number}'


