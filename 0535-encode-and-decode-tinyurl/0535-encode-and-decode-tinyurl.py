class Codec:
    
    def __init__(self):
        self.enc = {}
        self.dec = {}
        self.base = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.enc:
            url = self.base + str(len(self.enc) + 1)
            self.enc[longUrl] = url
            self.dec[url] = longUrl
        
        return self.enc[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        
        return self.dec[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))