class ProxyManager:
    def __init__(self, file=None):
        self.proxies = []
        self.index = 0

        if file != None:
            self.load(file)
    
    def load(self, proxies):
        if proxies is str:
            with open(proxies, 'r') as f:
                proxies = f.read().splitlines()
        
        for proxy in proxies:
            self.proxies.append(proxy)
        
        print(f"Loaded {len(proxies)} proxies")
    
    def load_single(self, proxy):
        self.proxies.append(proxy)
    
    def random(self):
        import random

        if len(self.proxies) == 0:
            return None

        return random.choice(self.proxies)