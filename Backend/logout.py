import requests

def logout(url, APIKey):
    logoutURL = url + "logout"
    response = requests.get(logoutURL, json={}, headers={'X-Auth-Token':APIKey})
    return print(f"Logout Error Code: {response.status_code}\nLogout JSON: {response.json()}")