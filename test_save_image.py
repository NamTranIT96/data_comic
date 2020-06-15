import requests


def saveImage(name, url):
    with open(name + '.jpg', 'wb') as handle:
        response = requests.get(url, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)


saveImage('test', 'https://www.nasa.gov/sites/default/files/thumbnails/image/blackhole.png')
