class bst:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        
def insert(root, key):
    if not root:
        return bst(key)
    if key >= root.value:
        root.right = insert(root.right, key)
    elif key < root.value:
        root.left = insert(root.left, key)
    return root

def insert_values(root, values):
    for value in values:
        root = insert(root, value)
    return root

def print2DTree(root, space=0, LEVEL_SPACE = 5):
    if (root == None): return
    space += LEVEL_SPACE
    print2DTree(root.right, space)
    # print() # neighbor space
    for i in range(LEVEL_SPACE, space): 
      print(end = " ")  
    print("|" + str(root.value) + "|<")
    print2DTree(root.left, space)

def print_tree(root):
        if root != None:
            _print_tree(root)

def _print_tree(cur_node):
      if cur_node != None:
          _print_tree(cur_node.left)
          print(str(cur_node.value))
          _print_tree(cur_node.right)

def print_preorder_tree(root):
      if root != None:
         print(str(root.value))
         _print_tree(root.left)
         _print_tree(root.right)

def print_inorder_tree(root):
      if root != None:
          _print_tree(root.left)
          print(str(root.value))
          _print_tree(root.right)

def print_postorder_tree(root):
      if root != None:
         _print_tree(root.left)
         _print_tree(root.right)
         print(str(root.value))

root=insert_values(None,[8,4,12,2,6,10,14,1,3,5,7,9,11,13,15])
print2DTree(root)
#               |15|<
#          |14|<
#               |13|<
#     |12|<
#              |11|<
#          |10|<
#               |9|<
#|8|<
#               |7|<
#          |6|<
#               |5|<
#     |4|<
#               |3|<
#          |2|<
#               |1|<
print_inorder_tree(root)
#1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
print_postorder_tree(root)
#1 2 3 4 5 6 7 9 10 11 12 13 14 15 8
print_preorder_tree(root)
#8 1 2 3 4 5 6 7 9 10 11 12 13 14 15