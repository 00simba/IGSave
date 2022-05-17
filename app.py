from flask import Flask, render_template, request, redirect, send_file
import urllib.request, requests


app = Flask(__name__)

all_links = []

@app.route('/', methods = ['POST', 'GET'])
def index():

    if request.method == 'POST':

        download_url = request.form['url']

        all_links.clear()

        if(len(download_url)>40):
            download_url=download_url[:-28]

        headers = {'User-Agent': 'Mozilla'}
        r = requests.get(download_url + '?__a=1', headers=headers)
        i=0
        loop=0

        while(loop<10):

            if(r.json()['graphql']['shortcode_media']['__typename'] == "GraphImage"):
                images = r.json()['graphql']['shortcode_media']
                img = images['display_url']
                #urllib.request.urlretrieve(img, 'C:/Users/Qureshi/Desktop/IGproject/{}.jpg'.format(i))
                all_links.append(img)
                break

            try:
                videos = r.json()['graphql']['shortcode_media']
                if(videos['is_video'] == True):
                    download_url = videos['video_url']
                    all_links.append(download_url)
                    #urllib.request.urlretrieve(download_url, 'C:/Users/Qureshi/Desktop/IGproject/{}.mp4'.format(i))
                    break
            except Exception:
                pass
        

            try:
                images = r.json()['graphql']['shortcode_media']['edge_sidecar_to_children']['edges'][i]
                img = images['node']['display_url']
                try:
                    #urllib.request.urlretrieve(img, 'C:/Users/Qureshi/Desktop/IGproject/{}.jpg'.format(i))
                    all_links.append(img)
                except Exception:
                    pass
            except Exception:
                pass


            try:
                videos = r.json()['graphql']['shortcode_media']['edge_sidecar_to_children']['edges'][i]
                if(videos['node']['is_video'] == True):
                    download_url = videos['node']['video_url']
                    try:
                        #urllib.request.urlretrieve(download_url, 'C:/Users/Qureshi/Desktop/IGproject/{}.mp4'.format(i))
                        all_links.append(download_url)
                    except Exception:
                        pass
            except Exception:
                pass

            i=i+1
            loop=loop+1

        return redirect('/')

    else:
        return render_template('index.html', links=all_links)

if __name__ == "__main__":
    app.run()



