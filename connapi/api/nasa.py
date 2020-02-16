import requests
import json
from connapi.data import Linker

class Nasa():
    def get_apod(api_key=None, date=None, hd=False, save=True):
        url = ""
        if(api_key is not None):
            url += Linker.url_apod + "api_key=" + api_key
        if(api_key is None):
            url += Linker.url_apod + "api_key=DEMO_KEY"
        if(date is not None):
            url += "&date=" + date
        if(hd is True):
            url += "&hd=True"
        print(url)
        resp = requests.get(url)
        new_resp = json.loads(resp.content)
        if(save == True):
            url = new_resp['url']
            response = requests.get(url)
            if response.status_code == 200:
                with open("sample.jpeg", 'wb') as f:
                    f.write(response.content)
            return "Image saved in Current Directory 'sample.jpeg'"
        else:
            return new_resp