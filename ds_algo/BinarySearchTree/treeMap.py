from UserDatabase import BSTree,User

class treeMap(BSTree):
    def __init__(self):
        self.root = None
    
    def __setitem__(self,key,value):
        keys = value.keys()
        if ('email' in keys and 'password' in keys):
            user = User(username=key,email=value['email'],password=value['password'])
            return self.insert(user)
    
    def __getitem__(self,key):
        return self.find(username=key)
    
    def __len__(self):
        return 0

tree = treeMap()
tree['rahman'] = {'email':'rahman@gmail.com','password':'123'}
tree['raheem'] = {'email':'raheem@gmail.com','password':'123'}
print(tree['rahman']) 
print(tree)
print(len(tree))
