from flask import Flask, render_template, request, redirect, send_file
import urllib.request, requests
import json 

app = Flask(__name__)

all_links = []

@app.route('/', methods = ['POST', 'GET'])
def index():

    if request.method == 'POST':

        download_url = request.form['url']

        all_links.clear()

        if(len(download_url)>40):
            download_url=download_url[:-28]

        headers = {'Accept': 'application/json'}

        r = requests.get(download_url + '?__a=1&__d=dis', headers=headers)
        media = r.json()
        #print (json.dumps(media['graphql']['shortcode_media']['edge_sidecar_to_children']['edges'], indent=4, sort_keys=True))

        for items in media['graphql']['shortcode_media']['edge_sidecar_to_children']['edges']:
            all_links.append(items['node']['display_url'])

        return render_template('index.html', links=all_links)


if __name__ == "__main__":
    app.run(debug=True)



