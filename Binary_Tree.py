'''
Michael Lepori
Simple Binary Tree structure to build up listops parses
'''

class Node:

    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

    def addRight(self, node):
        self.right = node

    def addLeft(self, node):
        self.left = node
    
    def hasChildren(self):
        if self.right != None or self.left != None:
            return True
        else:
            return False

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def getData(self):
        return self.data
