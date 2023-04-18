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
    'content-length': '292',
    'content-type': 'application/x-www-form-urlencoded',
    "cookie" : 'fbm_124024574287414=base_domain=.instagram.com; mid=Ykx7ZgALAAEuA5ym-037fLHn17yE; ig_did=1878DCE3-1DD2-4E8A-AEBF-F030FB4E39C5; datr=QDcAY3K6EgsSgRBNdwVvBkB-; dpr=2; ig_nrcb=1; csrftoken=jDPQuJprT6E6HgL1IsgJoIHfCjsSrNji; ds_user_id=58604319986',
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
    'x-csrftoken' : 'jDPQuJprT6E6HgL1IsgJoIHfCjsSrNji',
    'x-ig-app-id': '1217981644879628',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '1007329431',
    'x-requested-with' : 'XMLHttpRequest',
}

getHeaders = {
    'authority': 'www.instagram.com',
    'method': 'GET',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0', 
    'cookie': 'fbm_124024574287414=base_domain=.instagram.com; mid=Ykx7ZgALAAEuA5ym-037fLHn17yE; ig_did=1878DCE3-1DD2-4E8A-AEBF-F030FB4E39C5; datr=QDcAY3K6EgsSgRBNdwVvBkB-; dpr=2; ig_nrcb=1; ds_user_id=58604319986; csrftoken=iLhYgVIfmHXfsOmRr4eNXXThM5DmaxTf; sessionid=58604319986:DLCoRnkdlsINWt:3:AYfuGIFbt-gW0I4_QKQwa4BHWvtI9el6_5GFELqvZg; rur="RVA\05458604319986\0541713323135:01f7f6ab20cfcdcfd1ec98bb86f619b92475647a8e7e90b2dfd4d87f875b607b99476a0e"',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
    'viewport-width': '425'
}

updateHeaders = {
    'authority': 'www.instagram.com',
    'method': 'GET',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0', 
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
    'viewport-width': '425'
}

s = requests.Session()

def login():
    
    r = s.get('https://www.instagram.com/api/v1/web/accounts/login/ajax/', headers=updateHeaders)

    newCookies = r.cookies.get_dict()

    #Update headers

    currentCookie = headers['cookie']
    #Replace csrf
    currentCookie = re.sub("csrftoken=(.*?)\;", 'csrftoken=' + newCookies['csrftoken'] + ';', currentCookie)
    #Replace ig_did
    currentCookie = re.sub("ig_did=(.*?)\;", 'ig_did=' + newCookies['ig_did'] + ';', currentCookie)
    #Replace mid
    currentCookie = re.sub("mid=(.*?)\;", 'mid=' + newCookies['mid'] + ';', currentCookie)
    #Replace headers with new strings
    headers['x-csrftoken'] = newCookies['csrftoken']
    headers['cookie'] = currentCookie

    #Update getHeaders

    getHeadersCookie = getHeaders['cookie']
    #Replace csrf
    getHeadersCookie = re.sub("csrftoken=(.*?)\;", 'csrftoken=' + newCookies['csrftoken'] + ';', getHeadersCookie)
    #Replace ig_did
    getHeadersCookie = re.sub("ig_did=(.*?)\;", 'ig_did=' + newCookies['ig_did'] + ';', getHeadersCookie)
    #Replace mid
    getHeadersCookie = re.sub("mid=(.*?)\;", 'mid=' + newCookies['mid'] + ';', getHeadersCookie)
    #Replace getHeadesr with new string
    getHeaders['cookie'] = getHeadersCookie

    #Finally login
    r = s.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', data=data, headers=headers)

    print(r.content)

login()

@backoff.on_exception(backoff.expo, requests.exceptions.ConnectionError)
def getJSON(url):
    r = s.get(url, headers=getHeaders)
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

        #Check if media array is valid, otherwise login() and getJSON()
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