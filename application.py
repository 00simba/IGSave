import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
import urllib.request, requests
import json
from flask_cors import CORS, cross_origin
import base64
import time
import re

application = Flask(__name__)

cors = CORS(application)
application.config['CORS_HEADERS'] = 'Content-Type'
load_dotenv()

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

        data = {
                'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:'+ os.getenv('PASSWORD'),
                'username': f'' + os.getenv('USER'),
                'queryParams': '{}',
                'optIntoOneTap': 'false',
                'trustedDeviceRecords': '{}',
        } 

        headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
            "x-requested-with": "XMLHttpRequest",
            "referer": "https://www.instagram.com/accounts/login/",
            "x-csrftoken":'IbEsGeeenFTtKHolyV0q9kT3feMosvvW'
        }

        userAgent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36'

        with requests.Session() as s:

            s.headers = {'userAgent' : userAgent}
            s.headers.update({'Referer': 'https://www.instagram.com/accounts/login/'})

            r = s.get('https://www.instagram.com/accounts/login/')
            r = s.post('https://www.instagram.com/accounts/login/ajax/', data=data, headers=headers)
            r = s.get(download_url + '?__a=1&__d=dis')     

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