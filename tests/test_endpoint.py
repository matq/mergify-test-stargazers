from fastapi.testclient import TestClient
from main import app
from fixtures import (
    endpoint_url,
    request_mock_all_api_calls,
    request_mock_user_starred,
    request_mock_repos,
    request_mock_user_starred_api_rate_limit,
)

client = TestClient(app)


def test_ReadStarneighboursEndpoint_ReturnsStatusCode200():
    response = client.get(endpoint_url, auth=("mathieu", "quilliec"))
    assert response.status_code == 200


def test_ReadStarneighboursEndpoint_ReturnsListOfRepos(request_mock_all_api_calls):
    response = client.get(endpoint_url, auth=("mathieu", "quilliec"))
    assert isinstance(response.json(), list) is True


def test_ReadStarneighboursEndpoint_ReturnsStatusCode403(
    request_mock_user_starred_api_rate_limit,
):
    response = client.get(endpoint_url, auth=("mathieu", "quilliec"))
    assert response.status_code == 403
