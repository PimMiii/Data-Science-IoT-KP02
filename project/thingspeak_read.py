import time
import datetime
import requests

from config import read_api_key, channel_id, read_url, update_interval

data = None
last_update = time.time()


def read_httprequest(results_count=1, minutes=1):
    # Format the GET parameters
    params = {'api_key': read_api_key, 'results': results_count,
              'minutes': minutes}


    r = requests.get(url=read_url, params=params)  # request the results data
    print(r.url)
    if r.status_code == 200:  # 200: all is well
        print(r.status_code)
        if r is not None:
            req_data = r.json()
            print(req_data)
            return req_data
    else:  # something went wrong
        print(r.status_code)


def update_data(data=None):
    global last_update

    # check if last update was longer ago than the update interval
    if (time.time() - last_update) >= update_interval or data is None:
        # update data from thingspeak
        updated_data = read_httprequest()
        updated_data = updated_data['feeds']
        updated_data = updated_data[0]
        if updated_data is not None:
            last_update = time.time()
        return updated_data
    else:
        # return data as it was before updating
        return data

