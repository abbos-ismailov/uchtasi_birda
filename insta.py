import requests
import json


def instadownloader_func(link):
    import requests

    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {"url": link}

    headers = {
        "X-RapidAPI-Key": "166dbbdddemsh19c386e1d2d8066p100816jsnc5126b1f27a5",
        "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=querystring)
    rest = json.loads(response.text)
    print(rest, "------------------------>")
    dict = {}
    if "error" in rest:
        return "Bad error"
    else:
        if rest["Type"] == "Post-Image":
            dict["type"] = "image"
            dict["media"] = rest["media"]
            return dict
        
        elif rest["Type"] == "Post-Video":
            dict["type"] = "video"
            dict["media"] = rest["media"]
            return dict
    
        elif rest["Type"] == "Carousel":
            dict["type"] = "carousel"
            dict["media"] = rest["media"]
            return dict
        else:
            return "Bad"
