import requests
import json
from hidden_vars import *
from login import login
from logout import logout



def datasetSearch(coordinate: list, startTime: str, endTime: str, maxCloudCover: int, minCloudCover: int, maxResults: int):
    APIKey = login(URL, USERNAME, TOKEN)
    # Inputs:
    # lowerLeft: [lat, long]
    # upperRight: [lat, long]
    # startTime: "yyyy-mm-dd"
    # endTime: "yyyy-mm-dd"
    # maxCloudCover: int
    # minCloudCover: int
    # maxResults: int
    lowerLeft = [coordinate[0] - 0.01, coordinate[1] - 0.01]
    upperRight = [coordinate[0] + 0.01, coordinate[1] + 0.01]
    datasetURL = URL + f"scene-search"
    datasetData = {
    "maxResults": maxResults,
    "datasetName": "landsat_ot_c2_l1",
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
    #print(f"Dataset Error Code: {response.status_code}")
    #print(f"Dataset JSON: {response.json()}\n\n\n")
    #print(f"Data: {json.loads(f'{json.dumps(response.json())}')['data']}\n\n\n")
    images = []
    index = 0

    while index < 10:
        image = str(json.loads(f'{json.dumps(response.json())}')['data']['results'][index]['browse'][0]['browsePath'])
        images.insert(-1, image)
        index += 1

    logout(url=URL, APIKey=APIKey)
    return images



# datasetSearch(coordinate=[lat, long], startTime='YYYY-MM-DD', endTime='YYYY-MM-DD', minCloudCover=int, maxCloudCover=int, maxResults=int)



