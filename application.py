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
            'method': 'GET',
            'path': '/api/v1/web/login_page/',
            'scheme': 'https',
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'cookie': 'fbm_124024574287414=base_domain=.instagram.com; mid=Ykx7ZgALAAEuA5ym-037fLHn17yE; ig_did=1878DCE3-1DD2-4E8A-AEBF-F030FB4E39C5; ig_nrcb=1; datr=QDcAY3K6EgsSgRBNdwVvBkB-; dpr=2; shbid="2028\0542237186360\0541707683625:01f7ae4f7f24983f285a96393de06cc32792957a8d41b9bcfdc8eca2a3a3018a03d243f0"; shbts="1676147625\0542237186360\0541707683625:01f7f66d20d530ba09c48b4d372a077bb63d2be9b5371f2bdeafd2647223240ec17750b9"; rur="EAG\0542237186360\0541707683829:01f7fe6ca4f31bba2a664ed3a8ca58ed068e4aee89c33b9afb81001e9302883f61388290"; csrftoken=v1MeTUrYWEIQEpbMG64RGxLfEhKblygq; fbsr_124024574287414=5Rg6oWgoAvWiGwNCST2DSueNiKiBO0q5OcOuVgkMWok.eyJ1c2VyX2lkIjoiMTAwMDE0MjI4OTgzMDMzIiwiY29kZSI6IkFRQ2lPbWhMWElQcEtpc2NKSWJoU1FyQzRpdGM3WC1mcXR6Q0Z1TlZ1dkhnNjMzYmcweExCWFN1NVV4OURtV05PUkhOOGZDRm1fMGEtTUhkY2U3elRmRWU5Q1h3NEwxS0RTOXktZ25UQzdaeUZxQk9uMDB4QVVId1BLbEFZNzFic09INjVmano0bG5UcXBydTNJeUxFMmxqWXpTWEhCb05XdjVjYWdsMlF0bklaM05YUDRmME1KQ25ndUc3Um5XNnFyelREVHJBMkdoWXo5Y0IxX3RDNXEydi1RYTlmMUljeFcxbkktY3pEcHh2VkFwSUhaelVrZ0dUZkNFSmFuQ0syYlJDVzB3cFlLZ2k0VG5tQTlmOW0xakhjWjU3anItNUNldUgyRXNhY2pDeDJoRVZaSFpwRUFuOXJOV1ktY1NodUtEYkh3bGxHUm1La292LUNZQlFPWU5FLUVuQUYzSFNNSENSeFd1bTNFTURMdyIsIm9hdXRoX3Rva2VuIjoiRUFBQnd6TGl4bmpZQkFEWGZkOFhMaEZMNlluWVhXS3RaQTI1RGlLSDhPNHRoS21UTXVwTXRuWTlORHpiRkZVWkF5QWR1WEFZbGg3RFpCekJlY2lrMHFVM1pCTVpBeU1BQ2RmTDFNQ1Jod0dBNEFVdkdrbWs4VVhJSXM1WkMwclFEZ2xKdExuT1pDZ0RsWkFoOFlxQXVJMkdjY1NYd1hxZGpBbXZhREUweGkxVzZPWWtzVWU4WkMxbkV6cDBLSEE2SXJNNllaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjc2MTQ4MTQ4fQ',
            'referer': 'https://www.instagram.com/accounts/login/',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36',
            'viewport-width': '1440',
            'x-asbd-id': '198387',
            'x-csrftoken': 'v1MeTUrYWEIQEpbMG64RGxLfEhKblygq',
            'x-ig-app-id': '1217981644879628',
            'x-ig-www-claim': 'hmac.AR2cAdvVLtr0e7cXsLAoALArvOFYjFH8FyQWT53etA8ZkoYK',
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
            'cookie': 'fbm_124024574287414=base_domain=.instagram.com; mid=Ykx7ZgALAAEuA5ym-037fLHn17yE; ig_did=1878DCE3-1DD2-4E8A-AEBF-F030FB4E39C5; ig_nrcb=1; datr=QDcAY3K6EgsSgRBNdwVvBkB-; dpr=2; shbid="2028\0542237186360\0541707683625:01f7ae4f7f24983f285a96393de06cc32792957a8d41b9bcfdc8eca2a3a3018a03d243f0"; shbts="1676147625\0542237186360\0541707683625:01f7f66d20d530ba09c48b4d372a077bb63d2be9b5371f2bdeafd2647223240ec17750b9"; csrftoken=7mWAhMxnyK6gNmB5GPpNnL2BVobFZd6v; ds_user_id=2237186360; sessionid=2237186360%3ABAay6kKJ3lsTld%3A26%3AAYfgKRGAxW1FfVlgfn091HAO9QHjduZ-99rteIMgZQ; fbsr_124024574287414=k3OE1KjvGvr5NkPVDEof0lDTh75L4YA7Qm4GuKbdL58.eyJ1c2VyX2lkIjoiMTAwMDE0MjI4OTgzMDMzIiwiY29kZSI6IkFRQlFWTVRpejduazZEVzQzTlNRZGpCcUgzV2xkSWdCeEwwV0RDRE9KRDNUUU9JYkppd1pZcWFHZFNneTN5MXp1Zkd4Q1E0V1QyQ2lMLTF3aEpsdFlpOVVaTEJicE82NXpyb3ZjRXA4Ujg5R3doaDhlUXdlLVRRNmd2cVI5dkVyRXlJV2ZnOHBtUzlJMFRPNy1mb1o2RUpCeXA2TEE0emN3X2ljRnQzSUVWS3NtVnVZcGZEa1RPRGluVGc4OEF5eXBJU1BGUnZ1V2FSbWZNVVNhU282ckdRZzFIczBERHlzQmkxZ1ZLcTBsczhYc3l0ZkZGM1N0Z0l3dExTbUJNQllVQ3hEQldPVFRJTzdKRWRsdXVId2tUVURTT1BVd3FLa1hONjl1RHVpUjMxNkpMTlFfbzl3VG8xTUIxdHBQLXc1dmNUeWNMNVA4YlNrX1F6bjdhYnItT3BZeWc4N3FtbVI3TlBFNDc2bi01OUR6QSIsIm9hdXRoX3Rva2VuIjoiRUFBQnd6TGl4bmpZQkFEdG5sOHA0VWF4UDNWeG5WNWVhekJ6NzY2YWVlSUM1N3o0dE9neElwNFVVaElnM2JFNUpiVjRzQTcxd0JFaDVLczNVbmtNNlA4MmJzUnBaQk9aQWQwYWxzMlpCRldBaEo1QUxENzVDWkFaQ29aQlhGVVpBWkFaQUlVUUhBNm1IcWlEZlQ0UEI5WFJDRFhaQkppZE03TGp5U29mZ0U2a0twWHRZUEFDeVBVZXBDRm9QMGJ0SGdyUk1rWkQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY3NjE1NDIzNn0; fbsr_124024574287414=k3OE1KjvGvr5NkPVDEof0lDTh75L4YA7Qm4GuKbdL58.eyJ1c2VyX2lkIjoiMTAwMDE0MjI4OTgzMDMzIiwiY29kZSI6IkFRQlFWTVRpejduazZEVzQzTlNRZGpCcUgzV2xkSWdCeEwwV0RDRE9KRDNUUU9JYkppd1pZcWFHZFNneTN5MXp1Zkd4Q1E0V1QyQ2lMLTF3aEpsdFlpOVVaTEJicE82NXpyb3ZjRXA4Ujg5R3doaDhlUXdlLVRRNmd2cVI5dkVyRXlJV2ZnOHBtUzlJMFRPNy1mb1o2RUpCeXA2TEE0emN3X2ljRnQzSUVWS3NtVnVZcGZEa1RPRGluVGc4OEF5eXBJU1BGUnZ1V2FSbWZNVVNhU282ckdRZzFIczBERHlzQmkxZ1ZLcTBsczhYc3l0ZkZGM1N0Z0l3dExTbUJNQllVQ3hEQldPVFRJTzdKRWRsdXVId2tUVURTT1BVd3FLa1hONjl1RHVpUjMxNkpMTlFfbzl3VG8xTUIxdHBQLXc1dmNUeWNMNVA4YlNrX1F6bjdhYnItT3BZeWc4N3FtbVI3TlBFNDc2bi01OUR6QSIsIm9hdXRoX3Rva2VuIjoiRUFBQnd6TGl4bmpZQkFEdG5sOHA0VWF4UDNWeG5WNWVhekJ6NzY2YWVlSUM1N3o0dE9neElwNFVVaElnM2JFNUpiVjRzQTcxd0JFaDVLczNVbmtNNlA4MmJzUnBaQk9aQWQwYWxzMlpCRldBaEo1QUxENzVDWkFaQ29aQlhGVVpBWkFaQUlVUUhBNm1IcWlEZlQ0UEI5WFJDRFhaQkppZE03TGp5U29mZ0U2a0twWHRZUEFDeVBVZXBDRm9QMGJ0SGdyUk1rWkQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY3NjE1NDIzNn0; rur="EAG\0542237186360\0541707690380:01f7d7f1ab6403285368cb06f190a696ab4bdeb76ccd6c69c586e56f27d8d84a5de1bab1"',
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
        }

        data = {
                'username': f'' + os.getenv('USER'),
                'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:'+ os.getenv('PASSWORD'),
                'queryParams': '{}',
                'optIntoOneTap': 'false'
        } 

        s = requests.Session()

        r = s.get(download_url + '?__a=1&__d=dis')

        if('graphql' in r.json()):
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