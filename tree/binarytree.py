class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left 
        self.right = right 
        
    def insert(self, new_value):
        if self.value:
            if self.value > new_value: 
                if self.left is None:
                    self.left = Node(new_value)

                else:
                    self.left.insert(new_value)

            if self.value < new_value: 
                if self.right is None:
                    self.right = Node(new_value)

                else:
                    return self.right.insert(new_value)
    
    def find(self, value_to_search):
        if self.value == value_to_search:
            return True

        if self.right: 
            return self.right.search(value_to_search)
            
        if self.left:
            return self.left.search(value_to_search)

    def print_tree(self):
        print(self.value, end="  ")

        if self.left:
            self.left.print_tree()

        if self.right:
            self.right.print_tree()

    def __str__(self):
        return str(self.value)



