import requests
import json

url = "https://m2m.cr.usgs.gov/api/api/json/stable/"
loginURL = url + "login-token"
loginData = {
    "username": "hoadi",
    "token": "yiea2@Hc5cteIRHycnd@DpicT8o_HwEROuSf0Qj66BJ6uRPRzJXKJl9WAGTD@FmM"
}
response = requests.get(loginURL, json=loginData)
print(f"Login Error Code: {response.status_code}")
print(f"Login JSON: {response.json()}")
responseStr = json.dumps(response.json())
jsonDict = json.loads(f"{responseStr}")
APIKey = jsonDict['data']
print(f"API KEY: {APIKey}\n")


def datasetSearch(APIKey, lowerLeft: list, upperRight: list, startTime: str, endTime: str, maxCloudCover: int, minCloudCover: int):
    # Inputs:
    # lowerLeft: [lat, long]
    # upperRight: [lat, long]
    # startTime: "yyyy-mm-dd"
    # endTime: "yyyy-mm-dd"
    datasetURL = url + f"scene-search"
    datasetData = {
    "maxResults": 1,
    "datasetName": "gls_all",
    "sceneFilter": {
        "ingestFilter": None,
        "spatialFilter": {
            "filterType": "mbr",
            "lowerLeft": {
                    "latitude": lowerLeft[0],
                    "longitude": lowerLeft[1]
            },
            "upperRight": {
                    "latitude": upperRight[0],
                    "longitude": upperRight[1]
            }
        },
        "metadataFilter": None,
        "cloudCoverFilter": {
            "max": minCloudCover,
            "min": maxCloudCover,
            "includeUnknown": False
        },
        "acquisitionFilter": None
    },
    "bulkListName": "my_bulk_list",
    "metadataType": "summary",
    "orderListName": "my_order_list",
    "startingNumber": 1,
    "compareListName": "my_comparison_list",
    "excludeListName": "my_exclusion_list"
}
    response = requests.get(datasetURL, json=datasetData, headers={'X-Auth-Token':APIKey})
    print(f"Dataset Error Code: {response.status_code}")
    print(f"Dataset JSON: {response.json()}\n\n\n")
    print(f"Data: {json.loads(f'{json.dumps(response.json())}')['data']}\n\n\n")

datasetSearch(APIKey=APIKey, lowerLeft=[44.60847, -99.69639], upperRight=[44.60847, -99.69639], startTime="2012-01-01", endTime="2012-12-01", minCloudCover=0, maxCloudCover=100)

logoutURL = url + "logout"
response = requests.get(logoutURL, json={})
print(f"Logout Error Code: {response.status_code}")
print(f"Logout JSON: {response.json()}")