import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
import urllib.request, requests
import json
from flask_cors import CORS, cross_origin
import base64
import time
import backoff
import re
import calendar
import time

application = Flask(__name__)

cors = CORS(application)
application.config['CORS_HEADERS'] = 'Content-Type'
load_dotenv()

data = {
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:10:1682473797:' + os.getenv('PASSWORD'),
        'username': f'' + os.getenv('USER'),
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
    'content-length': '302',
    'content-type': 'application/x-www-form-urlencoded',
    "cookie" : 'dpr=2; ig_did=2679650D-61BD-4EC2-91F8-3FD9D96EA5E1; datr=rqdFZKdt0BBuKuQ_30wLtiD8; ig_nrcb=1; mid=ZEWnrwAEAAFk2ka6SPMfxPt_trkZ; csrftoken=CazoVxOKBEaDUwGBNUHBSR1fgYkAjJSA; ds_user_id=58604319986; rur="RVA\05458604319986\0541714012453:01f7beab6ea38d324915c5da33a87f91ab60ac37e0dcb4ca4cf143f011cf05a87b2500c3"',
    "origin": 'https://www.instagram.com',
    "referer" : 'https://www.instagram.com/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest' : 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'viewport-width': '1096',
    'x-asbd-id': '198387',
    'x-csrftoken' : 'CazoVxOKBEaDUwGBNUHBSR1fgYkAjJSA',
    'x-ig-app-id': '1217981644879628',
    'x-ig-www-claim': 'hmac.AR2YJUm4-djg30GSAO7GeOXGzk0BpGjoy1p98_o1I58hs7d2',
    'x-instagram-ajax': '1007377421',
    'x-requested-with' : 'XMLHttpRequest',
}

s = requests.Session()

def login():

    s.cookies.clear()

    r = s.get('https://www.instagram.com/api/v1/web/accounts/login/ajax/')

    newCookies = r.cookies.get_dict()

    #Update headers

    currentCookie = headers['cookie']
    #Replace csrf
    currentCookie = re.sub("csrftoken=(.*?)", 'csrftoken=' + newCookies['csrftoken'] + ';', currentCookie)
    #Replace ig_did
    currentCookie = re.sub("ig_did=(.*?)\;", 'ig_did=' + newCookies['ig_did'] + ';', currentCookie)
    #Replace mid
    currentCookie = re.sub("mid=(.*?)\;", 'mid=' + newCookies['mid'] + ';', currentCookie)
    #Replace headers with new strings
    headers['x-csrftoken'] = newCookies['csrftoken']
    headers['cookie'] = currentCookie

    #Finally login

    current_GMT = time.gmtime()
    time_stamp = calendar.timegm(current_GMT)
    data['enc_password'] = f'#PWD_INSTAGRAM_BROWSER:10:{time_stamp}:'+ os.getenv('PASSWORD'),
    print(data['enc_password'])

    r = s.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', data=data, headers=headers)

    print(r.content)

login()

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

        #Check if media is valid, otherwise login() and getJSON()
        if 'items' not in media:
            login()
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