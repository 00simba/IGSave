import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
import urllib.request, requests
import json
from flask_cors import CORS, cross_origin
import base64
import time

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

        headers = {
            'authority': 'www.instagram.com',
            'method': 'POST',
            'path': '/ajax/bz?__d=dis',
            'scheme': 'https',
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'content-length': '468',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'fbm_124024574287414=base_domain=.instagram.com; mid=Ykx7ZgALAAEuA5ym-037fLHn17yE; ig_did=1878DCE3-1DD2-4E8A-AEBF-F030FB4E39C5; ig_nrcb=1; datr=QDcAY3K6EgsSgRBNdwVvBkB-; csrftoken=mpjOcrli9drmkNGKr9STmDuBsXJcAyv4; ds_user_id=57399500417; dpr=2; fbsr_124024574287414=vOmiy2H1dIn83Dhw7SAoEcfTEkihCJvFN7yTUpEEpeY.eyJ1c2VyX2lkIjoiMTAwMDE0MjI4OTgzMDMzIiwiY29kZSI6IkFRQVp2YlhTbzJkNWZJYlI2am16YlN0Xzh6T1VrTlZDamtPOGZQeUV1RC02YjktV3VXMnVsdzBkaWFIY1hMZ19jVGhOdk9nckdjVHJXS01hU09FVWpUVk82LWc4bGZLeGU3OFVpSkcyenpfNUdoUzQ3SG9ucGRxd2Jla1A5b1h1aDNVUU1QcXp3STdPS0RyTDBjNnlPam5iTlJqNkpIb2h6X1NrVmtoWWhTa3MtUERWZm5EUVBFNENoTEIyS2ttNEhBWFlLXzNRTVU1Q0xPbmoteTN4TEtvY01kOUpybkNsOGRHcmxYQzBUaldCY2ZPVGJBeHBWVXIxdVNEdWFGQnhUS0hNdm9OSHZqTklUX1JtVnlNOVhfckVQNWhSOFFFN3NBUUFmUGlfOUR2eklQT0FKMmlNdVFlVF9fQ2xYajJBeXl1bDZIWW9MMGh2ckNYWWJRMDBYS1ctWUhuZTMydGpwQUNLelBXN3dJRnN0ZyIsIm9hdXRoX3Rva2VuIjoiRUFBQnd6TGl4bmpZQkFHTjRXWERydnpvTlQ0TFRXNGJ6WkNZRnQxbjN3RTk2RmU3ckV3czJVOERMOTdNeW5ER3VaQ0FkOVYxWkNqUktYWkFqbVhkYzdHc1BXNWVZbHhWTWZobHBoR3RSU01YRWRkVnVCWEJzbnZMQnhId0ZxT1VjejRaQmhFYXVIbUZDa0lmdGNHcEdOTnlyemtqWkNXQW4zUGU1ZlAzWkN3OWdmTG45SWhTSnY4VlFYWkM3RHVhY0Jja1pEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2NzgxNjE4ODF9; fbsr_124024574287414=LUHNdTeAGc4NoPyq3IsZbPhb1WO-hYqeyrKas2NApgo.eyJ1c2VyX2lkIjoiMTAwMDE0MjI4OTgzMDMzIiwiY29kZSI6IkFRQ0otWTR1WVFxVWtNNTljWW4wMV9adzQ3N1FhS3UyYjYzdmxBZ3liUWVSZmtpN1dqWFM3dUFTSWJYdENWN2EzVU9FYUtwNmlPZ3lJd2dHREFvZHlybDdjSVFpSEtzY29ma2tSRjVOZFBJS1RUeERtclczQU90ZFNtN3FpUXVBVjRzSVJDTllQbGEtN3Y4QXplREJ2V1MwTTk3cmJoNW93V0I1N0pGbkxJSHk3N0RMYWs0aFlPakVwbXBueFF1Q2JrWjRDWEJpbm9XY2J1QjJ3N1lncUd0bmxvV1RTMzBnaDNmeHh1MUN4RnN3eklsdncyUWloOEF0ZU40Mk9iV1IzNXp4RDZCTEtXUlMxT2lndEk3dGZHWlhpT2stcEQxdEk3UXZHblZZNUxKRWNldkJtWExUN0Q4aHh5MkNlbV9KSmoyQ29rTEtmVEh2V0xGVXpGZ0w5dlJ0WHNtXzN0dERPQW9QQ0pMSDJuYm52USIsIm9hdXRoX3Rva2VuIjoiRUFBQnd6TGl4bmpZQkFFc1ZmV0FFQURjck02MWl4dzlHMWdEbFVCc0lneTFJQ25qNnhSZWlzNDFzcHZUN1F0VUx0SFdoa3dZWkNmSVUwUHFkWkFjekg3aFNSdkpoZFMxUjJaQkFXY1V3b1pBc1ZhMVdTeDRaQkhMTXNnV3hmTFFhTFpDeUllbUxUSVJ4S044b01HOFpDMGFwVVpCbUdZZTJjWkNJUHVHeDVMb3FYWUxTZnBiclE1YmdkR2E0MGdheW1RY2taRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjc4MTYzNjAyfQ', 
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/accounts/login/',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36',
            'viewport-width': '425',
            'x-asbd-id': '198387',
            'x-csrftoken': 'mpjOcrli9drmkNGKr9STmDuBsXJcAyv4',
            'x-ig-app-id': '1217981644879628',
            'x-ig-www-claim': '0',
            'x-requested-with': 'XMLHttpRequest'
        }

        getHeaders = {
            'authority': 'www.instagram.com',
            'method': 'GET',
            'path': '/p/Cmci1YJpAck/?__a=1&__d=dis',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36',
            'viewport-width': '324',
            'cookie': 'dpr=2; datr=BLcGZCnjJUjKDz2omr9gFde3; csrftoken=IbEsGeeenFTtKHolyV0q9kT3feMosvvW; mid=ZAa3BQALAAE4yXID-23_PbmkVTEP; ig_did=6C6FBD91-C6F8-4D59-B065-DF997E50B280; ig_nrcb=1',   
        }

        data = {
                'username': f'' + os.getenv('USER'),
                'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:'+ os.getenv('PASSWORD'),
                'queryParams': '{}',
                'optIntoOneTap': 'false'
        } 

        s = requests.Session()

        res = s.post('https://www.instagram.com/accounts/login/ajax/', headers=headers, data=data)
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