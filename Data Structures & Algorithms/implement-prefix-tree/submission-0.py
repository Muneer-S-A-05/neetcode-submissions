class Node:
    def __init__(self,value=None):
        self.value = value
        self.children = {}
        self.end=False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for x in word:
            if x not in node.children:
                node.children[x] = Node(x)
                node = node.children[x]
            else:
                node = node.children[x]
        node.end=True
        

    def search(self, word: str) -> bool:
        node = self.root
        for x in word:
            if x not in node.children:
                return False
            else:
                node = node.children[x]
        if node.end:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for x in prefix:
            if x not in node.children:
                return False
            else:
                node = node.children[x]
        return True
        
        