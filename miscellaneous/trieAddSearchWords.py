'''
You should design a data structure that supports adding new words and finding if a string matches 
any previously added string.

Implement the WordDictionary class:

    WordDictionary() Initializes the object.
    void addWord(word) adds word to the data structure, it can be matched later.
    bool search(word) returns true if there is any string in the data structure that matches word or false otherwise. 
    word may contain dots '.' where dots can be matched with any letter.

'''

class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        current = self.root
        
        for i in word:
            if i not in current:
                current[i] = {}
            current = current[i]
        current['*'] = True
        
    def searchAgain(self, word, trie):
        for i, ch in enumerate(word):
            if ch not in trie:
                if ch == '.':
                    for j in trie:
                        if j != '*' and self.searchAgain(word[i+1:], trie[j]):
                            return True
                return False
            trie = trie[ch]
        return '*' in trie
        
    def search(self, word: str) -> bool:
        return self.searchAgain(word, self.root)
