class User:
    def __init__(self,username,email,value):
        self.username = username
        self.email = email
        self.value = value

class Userdb:
    def __init__(self):
        self.db = []
    
    def __str__(self):
        return str([user.username for user in self.db])

    def insert(self,user):
        if (user is None):
            print('user is None')
            return
        if len(self.db) == 0:
            print('first user added')
            self.db.append(user)
            return
        lo = 0
        hi = len(self.db)-1
        while (lo<=hi):
            mid = (lo+hi)//2
            print(lo,mid,hi)
            if (self.db[mid].username == user.username):
                print('username already exist')
                return
            elif (self.db[mid].username > user.username) and ((mid+1>hi) or self.db[mid+1].username < user.username):
                print('succesfully added user')
                self.db.insert(mid,user)
                return True
            elif (self.db[mid].username < user.username) and ((mid-1<lo) or self.db[mid-1].username > user.username):
                print('succesfully added user')
                self.db.insert(mid,user)
                return True
            elif (self.db[mid].username > user.username):
                print('moving to left')
                hi = mid-1
            else:
                print('moving to right')
                lo = mid+1
    
    def find(self,username):
        lo = 0
        hi = len(self.db)-1
        while (lo<=hi):
            mid = (lo+hi)//2
            print(mid)
            if (self.db[mid].username == username):
                return self.db[mid]
            elif (self.db[mid].username > username):
                hi = mid-1
            else:
                lo = mid+1
        return -1
        
db = Userdb()
db.insert(User('rahman','rahman@gmail.com',None))
db.insert(User('ramzan','ramzan@gmail.com',None))
db.insert(User('ramzan12','ramzan@gmail.com',None))
db.insert(User('anu','ramzan@gmail.com',None))
db.insert(User('vahman','rahman@gmail.com',None))
db.insert(User('xaaamzan','ramzan@gmail.com',None))
db.insert(User('mzan12','ramzan@gmail.com',None))
db.insert(User('efaanu','ramzan@gmail.com',None))

print(db.find('vahman'))
print(db)

"""
As the index of the values changes, this method will not be effective.
"""