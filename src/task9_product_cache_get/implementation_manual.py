import time
class Product_cache_get:
    def __init__(self,expiry_time):
        self.cache={}
        self.expiry_time=expiry_time

    
    def set(self,key,value,ttl=None):
        if ttl is not None and ttl<0:
            return None
        new_ttl=self.expiry_time/1000
        if ttl is not None:
            new_ttl=ttl/1000
        
        self.cache[key]={
                'value':value,
                'inserted_at':time.time(),        
                'expiry_time':time.time()+new_ttl
        }

    
    def get(self,key):
        if key not in self.cache:
            return None        
        if time.time()>self.cache[key]['expiry_time']:
            print("You can't access that")
            del self.cache[key]
            return None

        else:
            return self.cache[key]['value']

    def delete(self,key):
        if key in self.cache:
            del self.cache[key]
        return "deleted successfully"

    def cleanup(self):
        self.cache={}
        return "Cleaned successfully"
     

cache=Product_cache_get(expiry_time=60)
cache.set('a','apple')
print(cache.get('a'))

 