import time
class Product_cache_get:
    def __init__(self,expiry_time):
        self.cache={}
        self.expiry_time=expiry_time

    
    def set(self,key,value):
        self.cache[key]={
                'value':value,
                'inserted_at':time.time()        
        }
  
    
    def get(self,key):
        if key not in self.cache:
            return None
        time_left=time.time()-self.cache[key]['inserted_at']
        if time_left>self.expiry_time:
            print("You can't access that")
            return None
        else:
            return self.cache[key]['value']

    def delete(self,key):
        if key in self.cache:
            del self.cache[key]
 

    def cleanup(self):
        expired=[]
        for i in self.cache:
            time_left=time.time()-self.cache[i]['inserted_at']
            if time_left>self.expiry_time:
                expired.append(i)
        for i in expired:
            self.delete(i)
        return {self.cache[i]['value'] for i in self.cache}
     

item1=Product_cache_get(expiry_time=4)
item1.set('a','banana')
item1.set('b','apple')
print(item1.get('a'))
print(item1.get('z'))
time.sleep(9)
print(item1.get('a'))
item1.cleanup()
print(item1.cache)


