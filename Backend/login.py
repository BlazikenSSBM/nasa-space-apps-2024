import requests
import json


def login(url, username, token):
    loginURL = url + "login-token"
    loginData = {
        "username": username,
        "token": token
    }
    response = requests.get(loginURL, json=loginData)
    print(f"Login Error Code: {response.status_code}")
    print(f"Login JSON: {response.json()}")
    responseStr = json.dumps(response.json())
    jsonDict = json.loads(f"{responseStr}")
    APIKey = jsonDict['data']
    print(f"API KEY: {APIKey}\n")
    return APIKey