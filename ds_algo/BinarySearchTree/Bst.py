def is_bst(root):
    def process(node,lbound,hbound):
        if node is None:
            return True
        print(lbound,node.key,hbound)
        if (node.key < lbound) or (node.key > hbound):
            return False
        return process(node.left,lbound,min(node.key,hbound)) and process(node.right,max(lbound,node.key),hbound)
    return process(root,-float('inf'),float('inf'))

def display(root):
    def process(node,spacing=0):
        if node is None:
            print(spacing*'\t\t')
            return
        process(node.right,spacing+1)
        print(spacing*'\t\t',node.key)
        process(node.left,spacing+1)
    return process(root)

class BSTNode:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

# tree with digits
node1 = BSTNode(key=1,value=[])
node2 = BSTNode(key=2,value=[])
node3 = BSTNode(key=3,value=[])   
node4 = BSTNode(key=4,value=[])
node5 = BSTNode(key=5,value=[])

root = node1
root.left = node2
root.left.right = node3
root.right = node4
root.right.right = node5

print(is_bst(root))
display(root)
