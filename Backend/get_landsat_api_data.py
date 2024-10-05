import requests

url = "https://m2m.cr.usgs.gov/api/api/json/stable/login-token"
data = {
    "username": "hoadi",
    "token": "yiea2@Hc5cteIRHycnd@DpicT8o_HwEROuSf0Qj66BJ6uRPRzJXKJl9WAGTD@FmM"
}
response = requests.post(url, json=data)
auth_url = ""
print(response.status_code)

print(response.json())