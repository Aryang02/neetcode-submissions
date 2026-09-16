class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = True

    def search(self, word: str) -> bool:
        def dfs(node, idx):
            if idx == len(word):
                return True if node.word == True else False
            if word[idx] == '.':
                for _, child in node.children.items():
                    if dfs(child, idx+1):
                        return True
            if word[idx] in node.children:
                return dfs(node.children[word[idx]], idx+1)
            return False
            
        return dfs(self.root, 0)