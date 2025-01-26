
# User oject
class User:
    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password

# create some test users
users = {
    "user1": User("john_doe", "john.doe@example.com", "password123"),
    "user2": User("jane_smith", "jane.smith@example.com", "mypassword456"),
    "user3": User("alice_williams", "alice.williams@example.com", "alice2025"),
    "user4": User("bob_johnson", "bob.johnson@example.com", "secure789"),
    "user5": User("michael_lee", "michael.lee@example.com", "michaelpass"),
    "user6": User("susan_clark", "susan.clark@example.com", "susan321"),
    "user7": User("david_martin", "david.martin@example.com", "david1234"),
    "user8": User("emily_jones", "emily.jones@example.com", "emilyabcd"),
    "user9": User("charles_brown", "charles.brown@example.com", "charles2025"),
    "user10": User("lucy_davis", "lucy.davis@example.com", "lucysecret"),
    "user11": User("tom_white", "tom.white@example.com", "tomstrong"),
    "user12": User("olivia_moore", "olivia.moore@example.com", "olivia88"),
    "user13": User("james_harris", "james.harris@example.com", "jamespass"),
    "user14": User("isabella_king", "isabella.king@example.com", "kingisabella"),
    "user15": User("william_taylor", "william.taylor@example.com", "willtaylor01")
}

class BSTNode:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        
class BSTree:
    def __init__(self,root=None):
        self.root = root
    
    def insert(self,user):
        def process(node,user):
            if node is None:
                node = BSTNode(user.username,user)
            elif (user.username > node.key):
                node.left = process(node.left,user)
            else:
                node.right = process(node.right,user)
            return node
        self.root = process(self.root,user)
        return self.root
    
    def find(self,username):
        def process(node,username):
            if node is None:
                return None
            elif node.key == username:
                return node
            elif username > node.key :
                return process(node.left,username)
            else:
                return process(node.right,username)
        return process(self.root,username)
    
    def is_balanced(self):
        def process(node):
            if node is None :
                return True,0
            balanced_l,height_l = process(node.left)
            balanced_r,height_r = process(node.right)
            balanced = balanced_l and balanced_r and abs(balanced_l-balanced_r)<=1
            height = 1+max(height_l,height_r)
            return balanced,height
        return process(self.root)
    
    def display(self):
        def process(node,spacing=0):
            if node is None:
                print(spacing*'\t')
                return
            process(node.left,spacing+1)
            print(spacing*'\t\t',node.key)
            process(node.right,spacing+1)
        return process(self.root)
    
    def __str__(self):
        self.display()
        return ''


# tree operations
tree = BSTree()
for user in users:
    tree.insert(users[user])
print(tree)
print(tree.find('charles_brown'))
print(tree.is_balanced())


                    
        
        
        




