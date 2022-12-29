import urllib.request, requests

download_url = input("Enter URL: ")

headers = {'User-Agent': 'Mozilla'}
r = requests.get(download_url + '?__a=1', headers=headers)
i=0
loop=0

links = []

while(loop<10):

    try:
        videos = r.json()['graphql']['shortcode_media']
        console.log(videos)
        if(videos['is_video'] == True):
            download_url = videos['video_url']
            links.append(download_url)
            urllib.request.urlretrieve(download_url, 'C:/Users/<Your System Name>/Desktop/IGproject/{}.mp4'.format(i))
            break
    except Exception:
        pass
   

    try:
        images = r.json()['graphql']['shortcode_media']['edge_sidecar_to_children']['edges'][i]
        img = images['node']['display_url']
        console.log(images)
        links.append(download_url)
        urllib.request.urlretrieve(img, 'C:/Users/<Your System Name>/Desktop/{}.jpg'.format(i))
    except Exception:
        pass


    try:
        videos = r.json()['graphql']['shortcode_media']['edge_sidecar_to_children']['edges'][i]
        if(videos['node']['is_video'] == True):
            download_url = videos['node']['video_url']
            links.append(download_url)
            urllib.request.urlretrieve(download_url, 'C:/Users/<Your System Name>/Desktop/{}.mp4'.format(i))
    except Exception:
        pass

    i=i+1
    loop=loop+1
