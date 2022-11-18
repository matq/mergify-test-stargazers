from fastapi import FastAPI, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from core.authentication.login import login_check
from core.schemas.repository import Repository
from utils.response_data import json_response


app = FastAPI()
security = HTTPBasic()


@app.get("/repos/{user}/{repo_name}/starneighbours", response_model=list[Repository])
def read_starneighbours(
    user: str, repo_name: str, credentials: HTTPBasicCredentials = Depends(security)
):
    login_check(credentials)
    repos = list_repos(user, repo_name)
    return [Repository(**repo) for repo in repos]


def list_repos(user: str, repo_name: str) -> list[dict]:
    url = f"https://api.github.com/users/{user}/starred"
    response_data = json_response(url)
    repos: list = []
    main_stargazers: set = set()
    for repo in response_data:
        name = repo["name"]
        owner = repo["owner"]["login"]
        stargazers = set(list_stargazers_from_repo(owner, name))
        # Assign the stargazers for the repo we use in the endpoint since we can get a repo just from its name
        # without its owner
        if name == repo_name:
            main_stargazers = stargazers
        repos.append(dict(repo=repo["name"], stargazers=stargazers))
    for repo in repos:
        repo["stargazers"] = list(set(main_stargazers) & set(repo["stargazers"]))
    return repos


def list_stargazers_from_repo(owner: str, name: str) -> list:
    stargazers = json_response(
        f"https://api.github.com/repos/{owner}/{name}/stargazers"
    )
    return [user["login"] for user in stargazers]
