class Trie:

    dictionary = []

    def __init__(self):
        self.dictionary = []

    def insert(self, word: str) -> None:
        self.dictionary.append(word)

    def search(self, word: str) -> bool:
        for el in self.dictionary:
            if el == word:
                return True
        return False

    def startsWith(self, prefix: str) -> bool:
        if self.dictionary is None or len(self.dictionary) == 0:
            return False
        
        for el in self.dictionary:
            if el.startswith(prefix):
                return True

        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


if __name__ == "__main__":
    obj = Trie()
    word = "aaa"
    obj.insert(word)
    print(obj.search(word))
    print(obj.startsWith("a"))
    
    obj2 = Trie()
    print(obj2.startsWith("a"))
