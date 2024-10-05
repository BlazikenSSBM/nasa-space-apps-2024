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

def datasetSearch(coordinate: list, startTime: str, endTime: str, maxCloudCover: int, minCloudCover: int, maxResults: int):
    # Inputs:
    # lowerLeft: [lat, long]
    # upperRight: [lat, long]
    # startTime: "yyyy-mm-dd"
    # endTime: "yyyy-mm-dd"
    # maxCloudCover: int
    # minCloudCover: int
    # maxResults: int
    lowerLeft = [coordinate[0] - 5, coordinate[1] - 5]
    upperRight = [coordinate[0] + 5, coordinate[1] + 5]
    datasetURL = url + f"scene-search"
    datasetData = {
    "maxResults": maxResults,
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
            "max": maxCloudCover,
            "min": minCloudCover,
            "includeUnknown": True
        },
        "acquisitionFilter": {
            "end": endTime,
            "start": startTime
        }
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
    images = []
    index = 0
    try:
        while index < maxResults:
            image = str(json.loads(f'{json.dumps(response.json())}')['data']['results'][index]['browse'][0]['browsePath'])
            images.insert(-1, image)
            index += 1
    except:
        return images
    return images
        


print(f"{datasetSearch(coordinate=[0, 0], startTime='2010-01-01', endTime='2011-01-31', maxCloudCover=100, minCloudCover=0, maxResults=10)}")

logoutURL = url + "logout"
response = requests.get(logoutURL, json={}, headers={'X-Auth-Token':APIKey})
print(f"Logout Error Code: {response.status_code}")
print(f"Logout JSON: {response.json()}")
    