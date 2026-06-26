class Node:
    def __init__(self):
        self.children={}
        self.end=False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for x in word:
            if x not in node.children:
                node.children[x] = Node()
            node = node.children[x]
        node.end = True

    def search(self, word: str) -> bool:
        # recursion happens only if "." exists in search string
        def dfs(j,node):
            # index j is used to start remaining portion of search after "."
            for i in range(j,len(word)):
                x = word[i]
                if x=='.':
                    for child in node.children.values():
                        if dfs(i+1,child):
                            return True
                    return False
                else:
                    # only else executes and no recursion if no "."
                    if x not in node.children:
                        return False
                    node = node.children[x]
            return node.end
        return dfs(0,self.root)