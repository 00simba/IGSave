import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
import urllib.request, requests
import json
from flask_cors import CORS, cross_origin
import base64
import backoff
import re

application = Flask(__name__)

cors = CORS(application)
application.config['CORS_HEADERS'] = 'Content-Type'
load_dotenv()

data = {
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1755111618:{os.getenv('PASSWORD')}',
        'username': 'igsavedotio',
        'queryParams': '{}',
        'optIntoOneTap': 'false'
} 

headers = {
    'authority': 'www.instagram.com',
    'method': 'POST',
    'path': '/api/v1/web/accounts/login/ajax/',
    'scheme': 'https',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'content-length': '417',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'mid=aJZx3wALAAFrjh-Fbtpvfhri-TKg; datr=jYyXaFTa6TSs0_Szv38dpfZk; ig_did=B09BAB07-E433-4B69-A792-3A609FADFC6E; ps_l=1; ps_n=1; dpr=1.5; ig_nrcb=1; wd=953x868; rur="PRN\05458604319986\0541786647467:01feb75d084eee5c8c89441c7476889728b69857639f50cc180677dc3a53e96ffc3d1389"; csrftoken=oBJbY62yTadDoPYxqIYGtpi8hp79YoED',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/accounts/login/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': 'Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'x-asbd-id': '359341',
    'viewport-width': '768',
    'x-asbd-id': '359341',
    'x-csrftoken': 'oBJbY62yTadDoPYxqIYGtpi8hp79YoED',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': 'hmac.AR2YJUm4-djg30GSAO7GeOXGzk0BpGjoy1p98_o1I58hs2DH',
    'x-instagram-ajax': '1025847364',
    'x-requested-with': 'XMLHttpRequest',
    'x-web-session-id': 'r676jh:jj186o:9e8iph',
    'x-fb-friendly-name': 'PolarisShareSheetV3PostShareBarQuery',
    'x-root-field-name': 'fetch__XDTMediaDict',
    'x-fb-lsd': '-y0cMGTvW01TJpBQ_kZIyC'
}

s = requests.Session()

def login():

    s.cookies.clear()  
    r = s.get('https://www.instagram.com/api/v1/web/accounts/login/ajax/')
    #newCookies = r.cookies.get_dict()

    #Update headers
    #currentCookie = headers['cookie']
    #Replace csrf
    #currentCookie = re.sub("csrftoken=(.*?)\;", 'csrftoken=' + newCookies['csrftoken'] + ';', currentCookie)
    #Replace ig_did
    #currentCookie = re.sub("ig_did=(.*?)\;", 'ig_did=' + newCookies['ig_did'] + ';', currentCookie)
    #Replace mid
    #currentCookie = re.sub("mid=(.*?)\;", 'mid=' + newCookies['mid'] + ';', currentCookie)
    #Replace headers with new strings
    #headers['x-csrftoken'] = newCookies['csrftoken']
    #headers['cookie'] = currentCookie

    #Finally login
    r = s.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', data=data, headers=headers)

    print(r.content)


login()

def get_base64(url):
    return base64.b64encode(requests.get(url).content)

@application.route('/', methods = ['POST', 'GET'])
@cross_origin()
@backoff.on_exception(backoff.expo, requests.exceptions.ConnectionError)
def index():

    all_links = []

    if(request.method == 'POST'):

        req = request.json
        shortcode = str(req['url'].split('/')[-2])
 
        variables = "{\"shortcode\":\"" + f"{shortcode}" + "\",\"__relay_internal__pv__PolarisShareSheetV3relayprovider\":true}"

        post_data = {
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'PolarisPostRootQuery',
            'variables': f"{variables}",
            'server_timestamps': 'true',
            'doc_id': '24760146316904293',  # May change over time
        }


        response = requests.post('https://www.instagram.com/graphql/query', headers=headers, data=post_data)
        response.raise_for_status()

        post_data = response.json()

        response = {}

        # check if carousel
        try:
            media_array = post_data['data']['xdt_api__v1__media__shortcode__web_info']['items'][0]['carousel_media']
            media_links = []
            for i in range(0, len(media_array)): 

                current_media = {}

                # img link
                current_media['img'] = media_array[i]['image_versions2']['candidates'][0]['url']
                
                try:
                    # optional video link
                    current_media['vid'] = media_array[i]['video_versions'][0]['url']
                except Exception as e:
                    print("no video at carousel index")

                # thumbnail base64 string
                current_media['thumbnail'] = str(get_base64(media_array[i]['image_versions2']['candidates'][0]['url']))

                media_links.append(current_media)

            response['data'] = media_links
            return response
        except Exception as e:
            print("media is not carousel")

        # check if reel
        try:
            vid = post_data['data']['xdt_api__v1__media__shortcode__web_info']['items'][0]['video_versions'][-1]['url']
            thumbnail = str(get_base64(post_data['data']['xdt_api__v1__media__shortcode__web_info']['items'][0]['image_versions2']['candidates'][0]['url']))
            response = {
                'data': [
                    {
                        'vid': vid,
                        'thumbnail': thumbnail
                    }
                ]
            }
            return response
        except Exception as e:
            print("media is not a reel")

        # check if single image
        try:
            img = post_data['data']['xdt_api__v1__media__shortcode__web_info']['items'][0]['image_versions2']['candidates'][0]['url']
            thumbnail = str(get_base64(img))
            response = {
                'data': [
                    {
                        'img': img,
                        'thumbnail': thumbnail
                    }
                ]
            }
            return response
        except Exception as e:
            print("media is not an image")
 
        response['message'] = "invalid response"
        return response 

if __name__ == "__main__":
    application.run()