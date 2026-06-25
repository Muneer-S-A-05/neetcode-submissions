class Node:
    def __init__(self):
        self.children = {}
        self.end=False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for x in word:
            if x not in node.children:
                node.children[x] = Node()
            node = node.children[x]
        node.end=True
        

    def search(self, word: str) -> bool:
        node = self.root
        for x in word:
            if x not in node.children:
                return False
            node = node.children[x]
        return node.end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for x in prefix:
            if x not in node.children:
                return False
            node = node.children[x]
        return True
        
        