import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
import urllib.request, requests
import json
from flask_cors import CORS, cross_origin
import base64
import time
import backoff

application = Flask(__name__)

cors = CORS(application)
application.config['CORS_HEADERS'] = 'Content-Type'
load_dotenv()

data = {
        'username': f'' + os.getenv('USER'),
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:'+ os.getenv('PASSWORD'),
        'queryParams': '{}',
        'optIntoOneTap': 'false'
} 

headers = {
    'authority': 'www.instagram.com',
    'method': 'POST',
    "path": "/api/v1/web/accounts/login/ajax/",
    'scheme': 'https',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'content-length': '308',
    'content-type': 'application/x-www-form-urlencoded',
    "cookie" : 'fbm_124024574287414=base_domain=.instagram.com; mid=Ykx7ZgALAAEuA5ym-037fLHn17yE; ig_did=1878DCE3-1DD2-4E8A-AEBF-F030FB4E39C5; ig_nrcb=1; datr=QDcAY3K6EgsSgRBNdwVvBkB-; csrftoken=mpjOcrli9drmkNGKr9STmDuBsXJcAyv4; ds_user_id=57399500417; dpr=2; fbsr_124024574287414=2sxr7TpnSPlaESFLRQkp66111ajkGOusM-NKrzV4dU4.eyJ1c2VyX2lkIjoiMTAwMDE0MjI4OTgzMDMzIiwiY29kZSI6IkFRQk5hQUZZTl9LVGVlWE5VdFZxdUVGdHlRUUtkckxjREFabDFGeWtCbVRKT2lqQzhKLV9PRWxrd2dIdG1qUEFLXzVBd1dVYV94UmNCU0stMlFWamN3VkFnWGxjckk3RjVuOUtNc25oU3ZUaHVLVFdycHYtWUVocUgyRkEzYUVXTEZ1LUFLVlEyVzlTLUR5c296enpsdTVUZ3hRTm5tdlk4dXFwejhiNnhSSzIwajJkUWJCMzFCbWw0QWJteGtkSktwTWdUWHhzMlQ4SnhxNUlMQWNUaFpkUXBvVkpJMkpwUUFmLWxQakZjX3dURGZmX2dBaWtaUmlabGNYMVhRNllhdUNORkhaSnp3Z21DNmJndjhpdE5faldBcXVjQldqRDNZSlhENGlEdjZIeVJpelpxNnYycndjNHExQmtLQlh0b01DdTB6d3YyM2h6NUdjdWVOMDFNdlRnSXdtempNVWpFamdDM2NLM19sdWxRdyIsIm9hdXRoX3Rva2VuIjoiRUFBQnd6TGl4bmpZQkFLb29aQjVUTHBCZmZ3NVpCdWQ5VkpwRVFEOVluTm9OdkpMb293a1lwUHdkdWdKbVR4bjNDa1RHSWN6azBZdkxTRmVWcldxbVBjMU9rd3BzZEY4czhtdWJWZ3BKcWVON3lBOVc0WkE3cFNmUnZZa0Z1VmdQeGhYamVsb2NTUFFCSlJUdEU1SThrTVJxQTh1bHRhVWlNS2czTW9Hb3dWTnBDazhSeGpIZWRTWkFxREo2TEMwWkQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY3ODIxMjk4NH0',
    "origin": 'https://www.instagram.com',
    "referer" : "https://www.instagram.com/",
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest' : 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36',
    'viewport-width': '425',
    'x-asbd-id': '198387',
    'x-csrftoken' : 'mpjOcrli9drmkNGKr9STmDuBsXJcAyv4',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '1007064846',
    'x-requested-with' : 'XMLHttpRequest',
}

s = requests.Session()
r = s.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', data=data, headers=headers)
print(r.content)


@backoff.on_exception(backoff.expo, requests.exceptions.ConnectionError)
def getJSON(url):
    r = s.get(url)
    return r

@application.route('/', methods = ['POST', 'GET'])
@cross_origin()
def index():

    all_links = []

    if(request.method == 'POST'):

        req = request.json
        download_url = req['url']

        #If link is reel or mobile version
        if 'reel' in download_url:
            download_url = download_url[0:43]
        else:
            download_url = download_url[0:40]

        r = getJSON(download_url + '?__a=1&__d=dis')

        media = r.json()
        mediaArray = []

        try:
            #Checks to see if post is a reel
            responseImg = requests.get(media['items'][0]['image_versions2']['candidates'][0]['url'])
            responseVid = requests.get(media['items'][0]['video_versions'][0]['url'])
            all_links.append({'url': media['items'][0]['video_versions'][0]['url'], 'base64': "data:" + responseImg.headers['Content-Type'] + ";" + "base64," + base64.b64encode(responseImg.content).decode("utf-8"), 'base64Vid': "data:" + responseVid.headers['Content-Type'] + ";" + "base64," + base64.b64encode(responseVid.content).decode("utf-8")})
        except:
            mediaArray = media['items'][0]

        if len(mediaArray):
            try:
                for items in mediaArray['carousel_media']:  
                    response = requests.get(items['image_versions2']['candidates'][0]['url'])
                    try:
                        #Checks to see if carousel media is a video
                        all_links.append({'url': items['video_versions'][0]['url'], 'base64': "data:" + response.headers['Content-Type'] + ";" + "base64," + base64.b64encode(response.content).decode("utf-8")})
                    except:
                        #If not video, carousel media is an image
                        all_links.append({'url': items['image_versions2']['candidates'][0]['url'], 'base64' : "data:" + response.headers['Content-Type'] + ";" + "base64," + base64.b64encode(response.content).decode("utf-8")})
            except:
                #If the post is only a single image
                response = requests.get(mediaArray['image_versions2']['candidates'][0]['url'])
                all_links.append({'url': mediaArray['image_versions2']['candidates'][0]['url'], 'base64': "data:" + response.headers['Content-Type'] + ";" + "base64," + base64.b64encode(response.content).decode("utf-8")})
        
        return {'links' : all_links}
    
    else:
        return {'links' : all_links}

if __name__ == "__main__":
    application.run()