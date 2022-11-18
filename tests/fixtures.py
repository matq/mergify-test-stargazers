import pytest
from sample_data import user_starred, repo_1, repo_2, repo_3

user = "matq"
repo = "sahabatfb"
endpoint_url = f"/repos/{user}/{repo}/starneighbours"


@pytest.fixture
def request_mock_all_api_calls(request_mock_user_starred, request_mock_repos):
    pass


@pytest.fixture
def request_mock_user_starred(requests_mock):
    requests_mock.get(
        f"https://api.github.com/users/{user}/starred?page=1&per_page=100",
        json=user_starred,
    )
    requests_mock.get(
        f"https://api.github.com/users/{user}/starred?page=2&per_page=100", json={}
    )


@pytest.fixture
def request_mock_repos(requests_mock):
    requests_mock.get(
        "https://api.github.com/repos/mgmacleod/endysi/stargazers", json=repo_1
    )
    requests_mock.get(
        "https://api.github.com/repos/mgmacleod/endysi/stargazers", json={}
    )
    requests_mock.get(
        "https://api.github.com/repos/mustakimali/wiremock-grpc-rs/stargazers",
        json=repo_2,
    )
    requests_mock.get(
        "https://api.github.com/repos/mustakimali/wiremock-grpc-rs/stargazers", json={}
    )
    requests_mock.get(
        "https://api.github.com/repos/ephendyy/sahabatfb/stargazers", json=repo_3
    )
    requests_mock.get(
        "https://api.github.com/repos/ephendyy/sahabatfb/stargazers", json={}
    )


@pytest.fixture
def request_mock_user_starred_api_rate_limit(requests_mock):
    api_limit_response = {
        "message": "API rate limit exceeded.",
        "documentation_url": "https://docs.github.com/rest/overview/resources-in-the-rest-api#rate-limiting",
    }
    requests_mock.get(
        f"https://api.github.com/users/{user}/starred?page=1&per_page=100",
        json=api_limit_response,
    )
