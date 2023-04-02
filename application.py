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
    'content-length': '356',
    'content-type': 'application/x-www-form-urlencoded',
    "cookie" : 'fbm_124024574287414=base_domain=.instagram.com; mid=Ykx7ZgALAAEuA5ym-037fLHn17yE; ig_did=1878DCE3-1DD2-4E8A-AEBF-F030FB4E39C5; ig_nrcb=1; datr=QDcAY3K6EgsSgRBNdwVvBkB-; shbid="2028\0542237186360\0541711574683:01f7885efc0cdd6a9c2af3a750d21dbb7bda580dabe9c87be3df6532cef209006ae2ad0c"; shbts="1680038683\0542237186360\0541711574683:01f7ca084f07ce34887509e1495aa2843428a9a281cfbf2dbeefb65569e26ef66f56d67b"; dpr=2; ds_user_id=58604319986; fbsr_124024574287414=BYDvxujK62i3Aw2D3JS6YG_MLQm_2uj8a9_wbmei4hQ.eyJ1c2VyX2lkIjoiMTAwMDE0MjI4OTgzMDMzIiwiY29kZSI6IkFRQTd1Z1Q3X3hyODNaaDJaR1B6ZUdhUGlnaW4wcEh3YmxVcjNKNVc0a3VSOGlCX1dWb2JMdnNvTHZLaHRqSzJXNEFsMktXR0xISlMyTXpvS0d0N2dxWXhlQXpLYWNMOTIySmpYdExma1NESUZEcWw3ampRb0RlX2NSVjRlb1JQYjh2Ujl5S3dvN3hlZkNyTlZfTGVoRGYxQ1k2VUMwdDhtd1dQckRGd29zUS1HaS1QZ2VqVWFfdUI1Nm1NemRxblY2WXpsSHc2T25hMWVaS045UXdLMmJBbG1TYVpxVFhMV0lZN0t1MjEwcXl2QS1EWlg0Nl83OHk1aXdKamc3dERMRUlKOTRqQXBKbGk4UWZxN2VmU29Kb25qY0lya2dmWHczVEt3ZUkzNmpXNWFCdUZHLXJlb25xT2NyMl81RV9iZHd1cUdPbXNiMmJoSXNldmVkemE1dFRKdXBQQ3JLeUwtZFFzdFpIM0taUkhIdyIsIm9hdXRoX3Rva2VuIjoiRUFBQnd6TGl4bmpZQkFNRlpBZHJYQ1pBNURDY1haQ2pDdVpCS1BsNnoybUdaQ0RWQ0FJQ2hJbXQxWkFpY29QbmxXVU45QXdaQUM0UGdaQXg4SzRDZXNTZVhlMDFWYlFrelRvaXVZOVVhdmkyenY4aUNHZFBUaHVUdzZhMjF1RVdtYjVpMXpzeFJLWkJIV2o3MWNXTU5SZWZjWkFnUHhLQ0RVN3VGaGYwMVJaQmIwOVpBajJ1MXhhTXF5V0JOb205bUZFS3pRTmtaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgwNDcxMzQxfQ; csrftoken=pewYUcj4lonHEXEM4nQ5XHYxeyrLyQRI; sessionid=58604319986:EUwpQmmligHHvK:12:AYf030upKnJWCN5qWd-a7RT7gPmBfs3RkWsCNYsS0w; fbsr_124024574287414=BYDvxujK62i3Aw2D3JS6YG_MLQm_2uj8a9_wbmei4hQ.eyJ1c2VyX2lkIjoiMTAwMDE0MjI4OTgzMDMzIiwiY29kZSI6IkFRQTd1Z1Q3X3hyODNaaDJaR1B6ZUdhUGlnaW4wcEh3YmxVcjNKNVc0a3VSOGlCX1dWb2JMdnNvTHZLaHRqSzJXNEFsMktXR0xISlMyTXpvS0d0N2dxWXhlQXpLYWNMOTIySmpYdExma1NESUZEcWw3ampRb0RlX2NSVjRlb1JQYjh2Ujl5S3dvN3hlZkNyTlZfTGVoRGYxQ1k2VUMwdDhtd1dQckRGd29zUS1HaS1QZ2VqVWFfdUI1Nm1NemRxblY2WXpsSHc2T25hMWVaS045UXdLMmJBbG1TYVpxVFhMV0lZN0t1MjEwcXl2QS1EWlg0Nl83OHk1aXdKamc3dERMRUlKOTRqQXBKbGk4UWZxN2VmU29Kb25qY0lya2dmWHczVEt3ZUkzNmpXNWFCdUZHLXJlb25xT2NyMl81RV9iZHd1cUdPbXNiMmJoSXNldmVkemE1dFRKdXBQQ3JLeUwtZFFzdFpIM0taUkhIdyIsIm9hdXRoX3Rva2VuIjoiRUFBQnd6TGl4bmpZQkFNRlpBZHJYQ1pBNURDY1haQ2pDdVpCS1BsNnoybUdaQ0RWQ0FJQ2hJbXQxWkFpY29QbmxXVU45QXdaQUM0UGdaQXg4SzRDZXNTZVhlMDFWYlFrelRvaXVZOVVhdmkyenY4aUNHZFBUaHVUdzZhMjF1RVdtYjVpMXpzeFJLWkJIV2o3MWNXTU5SZWZjWkFnUHhLQ0RVN3VGaGYwMVJaQmIwOVpBajJ1MXhhTXF5V0JOb205bUZFS3pRTmtaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgwNDcxMzQxfQ; rur="EAG\05458604319986\0541712007848:01f76a236cecddefe3cc81a5fd979d95d4ed2e61a2fc97449b45fc2073d16a3a1ce051d8"',
    "origin": 'https://www.instagram.com',
    "referer" : "https://www.instagram.com/",
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest' : 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
    'viewport-width': '425',
    'x-asbd-id': '198387',
    'x-csrftoken' : 'pewYUcj4lonHEXEM4nQ5XHYxeyrLyQRI',
    'x-ig-app-id': '1217981644879628',
    'x-ig-www-claim': 'hmac.AR2YJUm4-djg30GSAO7GeOXGzk0BpGjoy1p98_o1I58hs-K3',
    'x-instagram-ajax': '1007228779',
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

        print(r.content)

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