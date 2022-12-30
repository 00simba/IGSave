from flask import Flask, render_template, request, redirect, send_file
import urllib.request, requests
import json

application = Flask(__name__)

all_links = []


@application.route('/', methods = ['POST', 'GET'])
def index():

    if request.method == 'POST':

        s = requests.Session()

        headers = {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36',
            'x-asbd-id': '198387',
            'x-csrftoken': 'cJYpdquHZ63aoWhJgLoJIPVDSkGxn4rW',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR2pitRBXWeGMybAC8XIej3q4FpvQjB27u7pmysXYjSkIXYN',
            'x-instagram-ajax': '4934ba29fa49',
            'x-requested-with': 'XMLHttpRequest',
            'connection': 'keep-alive',
        }

        data = {
                'username': f'<Your Username>',
                'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:<Your Password>',
                'queryParams': '{}',
                'optIntoOneTap': 'false'
            }   

        res = s.post('https://www.instagram.com/accounts/login/ajax/', headers=headers, data=data)

        
        all_links.clear()

        download_url = request.form['url']

        #If link is reel
        if 'reel' in download_url:
            download_url = download_url[0:43]
        else:
            download_url = download_url[0:40]

        r = s.get(download_url + '?__a=1&__d=dis', headers=headers)
        media = r.json()

        mediaArray = []

        
        #Either reel or not reel
        try:
            all_links.append(media['items'][0]['video_versions'][0]['url'])
        except:
            mediaArray = media['items'][0]
    
        if len(mediaArray):
            try:
                for items in mediaArray['carousel_media']:  
                    all_links.append(items['image_versions2']['candidates'][0]['url'])
            except:
                all_links.append(mediaArray['image_versions2']['candidates'][0]['url'])

        return render_template('index.html', links = all_links)

    else:
        return render_template('index.html')


if __name__ == "__main__":
    application.run()