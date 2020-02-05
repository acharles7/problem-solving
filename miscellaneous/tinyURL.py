class tinyURL():

    def encode(self, n):
        char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        shortUrl = 'https://myurl/'
        while n > 0:
            shortUrl += char[n%62]
            n = n//62
        return shortUrl[::-1]

    def decode(self, shortUrl):
        idx = 0
        for i in range(len(shortUrl.split('/')[0])):
            if shortUrl[i] >= 'a' and shortUrl[i] <= 'z':
                idx = idx*62 + (ord(shortUrl[i]) - ord('a'))
            if shortUrl[i] >= 'A' and shortUrl[i] <= 'Z':
                idx = idx*62 + (ord(shortUrl[i]) - ord('A')) + 26
            if shortUrl[i] >= '0' and shortUrl[i] <= '9':
                idx = idx*62 + (ord(shortUrl[i]) - ord('0')) + 52
        return idx

url = tinyURL()
url.decode(url.encode(734311))
