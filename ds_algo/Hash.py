class HashTable:
    def __init__(self):
        self.data = [None for _ in range(4000)]
        
    def __getitem__(self,key):
        idx = self.get_index(key)
        if idx!=-1 and self.data[idx]:
            return self.data[idx][1]
        return self.data[idx]
    
    def __setitem__(self,key,value):
        return self.insert(key,value)
    
    def get_index(self,key):
        idx = 0
        for c in key:
            idx += ord(c)
        if self.data[idx]!=None and self.data[idx][0]!=key:
            return self.get_validIndex(key,idx)
        return idx
    
    def get_validIndex(self,key,idx):
        newIdx=idx+1
        while (newIdx <= len(self.data)) :
            if (newIdx == len(self.data)):
                newIdx = 0
            elif (self.data[newIdx] == None):
                return newIdx
            elif newIdx == idx:
                return -1
            newIdx+=1
    
    def insert(self,key,value):
        idx = self.get_index(key)
        if idx!=-1:
            self.data[idx] = [key,value]
            return True
        return False

    def delete(self,key):
        idx = self.get_index(key)
        if idx!=-1:
            self.data[idx] = None
            return True
        return False

data =HashTable()
data['rahman'] = 99
print(data['rahman'])
data['rahman'] = 100
print(data['rahman'])
print(data['me'])

