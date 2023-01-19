from flask import Flask, render_template, request
import urllib.request, requests
import json

application = Flask(__name__)

all_links = []

@application.route('/', methods = ['POST', 'GET'])
def index():

    if request.method == 'POST':

        req = request.json
        download_url = req['url']

        #If link is reel or mobile version
        if 'reel' in download_url:
            download_url = download_url[0:43]
        else:
            download_url = download_url[0:40]

        s = requests.Session()

        headers = {
				"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",			
				"Accept-Encoding" : "gzip, deflate, br",	
				"Accept-Language" : "en-CA,en-US;q=0.7,en;q=0.3",		
				"Connection" : "keep-alive",
				"Cookie" : 'fbm_124024574287414=base_domain=.instagram.com; mid=Ykx7ZgALAAEuA5ym-037fLHn17yE; ig_did=1878DCE3-1DD2-4E8A-AEBF-F030FB4E39C5; ig_nrcb=1; datr=QDcAY3K6EgsSgRBNdwVvBkB-; dpr=2; csrftoken=rKnymk7cq5nAt6rePZgHvVL9loa57V3O; ds_user_id=2237186360; shbid="2028\0542237186360\0541705536455:01f7487ae8e73d18f8ddb60a0d0429aafc23a5e1b6c1a0aca398efe66072142cafabc4c8"; shbts="1674000455\0542237186360\0541705536455:01f748d6e03da490e7a14c26af3a9c973073d8834f556048578bca0be3b1f43d61935108"; fbsr_124024574287414=2VyviBh4z0udNoK0rCU-5yJSfKdzItiXiAhSvqHYQfY.eyJ1c2VyX2lkIjoiMTAwMDE0MjI4OTgzMDMzIiwiY29kZSI6IkFRQTNtVllkY2FEaFRaQkhUaTU3eG9xRzg5OE80dmZVbEZBSDRIeWo0M3d0bGpsOGdhNXZJRUNYOUp3R0JjV09VRUFKOGNicDVvdHBNVXhfUkFNZFJrQVpTQ1Q0VFRlUktoTTFXUFdYRktnQ29XSEpOMVdfOFNMOXR0OXVhVkxEVHdHSktMeWVlalVTU1VuY3BvZy1nN3MwbnZvTGJmR3BVbmxWYTdSeUIwbDNNQl9pWVVWNnloMXdYZ0tkX3NUWlY3V2JxYzJxOE1WMmlqTWszd1dkbkRHOHBjWmJQUnJMVnJUVVZMU0dGb25jQXlXQ2F2NVViYmYyclRBZ1BoQkxwWWE3WkdNNDI1U0cxMzZIaTRIS3JtNTFxa2JwaGY4YmlGejZET2laVU5wQjJBSmU5Tl9WYVREZEFRb2ZOSFFtbW9Xakh5OUhCMm1MTnFwU0NlVmVPc0JWIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQURmSWVCaXRPSTMxZlpCZDFNWkNYR1pBUGRlMnNJbUlCRTBFZ3I2TVpDVGxpbmJJUG9zZUNXNzdrcTZDM1YzdjJUT29tWkMwMmhZV2dCTFluWkE1N3RNTXVHblRoWkFmWGZWTzI2bVpBTVpCMVhJQWk2WEpHUE1HOWVNQzY5eTJnR05XNFBSczJoWUd3VE45RW1ONm9DU3RwRExaQU5oZDA4R0JRcHhJTUpoN0RMa3RLTGFqWHRueGdaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjc0MDExOTExfQ; sessionid=2237186360:io1cFi0imrNrM5:21:AYfrgXg3dnVd1NnuIF0XxWZTgP5B3yHLITLYAs-Tsw; fbsr_124024574287414=2VyviBh4z0udNoK0rCU-5yJSfKdzItiXiAhSvqHYQfY.eyJ1c2VyX2lkIjoiMTAwMDE0MjI4OTgzMDMzIiwiY29kZSI6IkFRQTNtVllkY2FEaFRaQkhUaTU3eG9xRzg5OE80dmZVbEZBSDRIeWo0M3d0bGpsOGdhNXZJRUNYOUp3R0JjV09VRUFKOGNicDVvdHBNVXhfUkFNZFJrQVpTQ1Q0VFRlUktoTTFXUFdYRktnQ29XSEpOMVdfOFNMOXR0OXVhVkxEVHdHSktMeWVlalVTU1VuY3BvZy1nN3MwbnZvTGJmR3BVbmxWYTdSeUIwbDNNQl9pWVVWNnloMXdYZ0tkX3NUWlY3V2JxYzJxOE1WMmlqTWszd1dkbkRHOHBjWmJQUnJMVnJUVVZMU0dGb25jQXlXQ2F2NVViYmYyclRBZ1BoQkxwWWE3WkdNNDI1U0cxMzZIaTRIS3JtNTFxa2JwaGY4YmlGejZET2laVU5wQjJBSmU5Tl9WYVREZEFRb2ZOSFFtbW9Xakh5OUhCMm1MTnFwU0NlVmVPc0JWIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQURmSWVCaXRPSTMxZlpCZDFNWkNYR1pBUGRlMnNJbUlCRTBFZ3I2TVpDVGxpbmJJUG9zZUNXNzdrcTZDM1YzdjJUT29tWkMwMmhZV2dCTFluWkE1N3RNTXVHblRoWkFmWGZWTzI2bVpBTVpCMVhJQWk2WEpHUE1HOWVNQzY5eTJnR05XNFBSczJoWUd3VE45RW1ONm9DU3RwRExaQU5oZDA4R0JRcHhJTUpoN0RMa3RLTGFqWHRueGdaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjc0MDExOTExfQ; rur="NCG\0542237186360\0541705547949:01f76a58f58bbf5af703c726f884f2c08d5fcde6e34db00299afba65e78cbe8b1b1bfa20"',
				"Host" : "www.instagram.com",   
                "Sec-Fetch-Dest" : "document",
				"Sec-Fetch-Mode" : "navigate",
				"Sec-Fetch-Site" : "none",		
				"Sec-Fetch-User" : "?1",		
				"TE" : "trailers",     
                "Upgrade-Insecure-Requests" : "1",
				"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0"		
	    }

        data = {
                'username': f'flaskgram',
                'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:@Canada1.',
                'queryParams': '{}',
                'optIntoOneTap': 'false'
        }   

        r = s.get(download_url + '?__a=1&__d=dis', headers=headers)

        if(r.status_code != 200):
            res = s.post('https://www.instagram.com/accounts/login/ajax/', headers=headers, data=data)
            r = s.get(download_url + '?__a=1&__d=dis', headers=headers)
        
        all_links.clear()

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

     
        return {'links': all_links}
    else:
        return {'links': all_links}

if __name__ == "__main__":
    application.run()