from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children[ch]
        node.word = True

    def search(self, word: str) -> bool:
        def dfs(node, idx):
            if idx == len(word):
                return True if node.word == True else False
            if word[idx] in node.children:
                return dfs(node.children[word[idx]], idx+1)
            
            return False
        return dfs(self.root, 0)

    def startsWith(self, prefix: str) -> bool:
        def dfs(node, idx):
            if idx == len(prefix):
                return True
            if prefix[idx] in node.children:
                return dfs(node.children[prefix[idx]], idx+1)
            
            return False
        
        return dfs(self.root, 0)
        