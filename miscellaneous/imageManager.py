'''
Create a ImageManager that can be used for downloading an image from an URL.
If the image has been downloaded previously, retrieve from cache.
'''

from collections import OrderedDict
class Cache():
    def __init__(self):
        self.cache = OrderedDict()
        self.capacity = 3

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value)->None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        print("Inserted in cache")
        if len(self.cache) > self.capacity:
            self.cache.popitem(0)

class ImageDownloader():

    'Retrive image from URL'
    def getImage(self, url)->str:
        return url.split('//')[1]

class ImageManager():
    def __init__(self):
        self.lruCache = Cache()
        self.imageDownloader = ImageDownloader()
        self.localStorage = {}

    def processRequest(self, url):
        print(url + '|| ', end=' ')
        if url in self.lruCache.cache:
            print(">>> Request Processed from Cache")
            return self.lruCache.get(url)
        elif url in self.localStorage:
            print(">>> Request Processed from Local Storage", end = ' >>> ')
            self.lruCache.put(url, self.localStorage[url])
            return self.localStorage[url]
        else:
            image = self.imageDownloader.getImage(url)
            self.lruCache.put(url, image)
            self.localStorage[url] = image


imageUrls = ['url//1.png', 'url//8.png', 'url//2.png', 'url//3.png', 'url//1.png',
             'url//1.png', 'url//4.png', 'url//4.jpg', 'url//5.jpg', 'url//5.jpg']
manager = ImageManager()
for url in imageUrls:
    manager.processRequest(url)s
