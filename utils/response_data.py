import requests
from fastapi import HTTPException


def json_response(url: str) -> list:
    page_number = 1
    response = requests.get(f"{url}?page={page_number}&per_page=100").json()
    # We hit the rate API limit
    if isinstance(response, dict) and response.get("message"):
        raise HTTPException(status_code=403, detail="Too many requests")
    total_response: list = []
    while response:
        total_response.extend(response)
        page_number += 1
        response = requests.get(f"{url}?page={page_number}&per_page=100").json()
    return total_response
