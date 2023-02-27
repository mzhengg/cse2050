# A class for trie nodes
class TrieNode:
    # Initializes a trie node
    def __init__(self, _is_word=False):
        # Initialize attributes
        self._children = {}
        self._is_word = _is_word

    # adds a word to the Trie (only used during initialization)
    def add_word(self, word):
        # Case 1: only the key remains
        if len(word) == 1:
            if (len(self._children) > 0) and (word in self._children):
                self._children[word]._is_word = True
                return
            else:
                self._children[word] = TrieNode(True)
                return

        # Case 2: key in trie
        for child in self._children:
            if word[0:1] == child:
                return self._children[child].add_word(word[1:])
        
        # Case 3: key not in trie
        self._children[word[0:1]] = TrieNode()
        self._children[word[0:1]].add_word(word[1:])

    # Find the node with a given prefix
    def find_node(self, prefix):
        if len(prefix) == 0: return self

        for child in self._children:
            if prefix[0:1] == child:
                return self._children[child].find_node(prefix[1:])

    # Generate all the words with the given prefix
    def get_words(self, prefix, s=None):
        if prefix == '' and len(self._children) == 0:
            return []

        if prefix == '': 
            yield from self.get_words_helper(prefix)
            return

        if s is None: s = prefix

        if (self._is_word == True) or (len(self._children) == 0):
            yield s

        for child in self._children:
            yield from self._children[child].get_words(prefix, s + child)

    def get_words_helper(self, s):
        if (self._is_word == True) or (len(self._children) == 0):
            yield s

        for child in self._children:
            yield from self._children[child].get_words_helper(s + child)

    # Return the number of words in the trie
    def get_nb_words(self):
        if len(self._children) == 0:
            return 0
        out = []
        for val in self.get_nb_words_helper(0):
            out.append(val)
        return len(out)

    def get_nb_words_helper(self, c):
        if (self._is_word == True) or (len(self._children) == 0):
            yield 'l'

        for child in self._children:
            yield from self._children[child].get_nb_words_helper(c)

    def is_word(self):
        return self._is_word


# A class that implements a prefix tree for words
# This is the "public facing" interface - users interact with WordTrie directly
# TrieNode is private. Users do not directly use that class, but WordTrie can.
# Note that this class is defined for you - you do not need to make any changes.
class WordTrie:
    def __init__(self, words):
        self._root = TrieNode()                         # root node is empty
        for word in words: self._root.add_word(word)    # add all words to trie

    # Generate all the words with a given prefix
    def get_words(self, prefix=''):
        node = self._root.find_node(prefix)     # Locate the node corresponding to the given prefix

        if node is not None:                
            yield from node.get_words(prefix)   # Yield from the generator defined for trie nodes

    # Generate all the words in the prefix tree
    def __iter__(self):
        yield from self.get_words() # Yield from the more general generator

    # Return the number of words with a given prefix
    def get_nb_words(self, prefix=''):
        node = self._root.find_node(prefix)                   # Locate the node corresponding to the given prefix
        return node.get_nb_words() if node is not None else 0 # Delegate the work to the node class
        
    # Return the number of words in the prefix tree
    def __len__(self):
        return self._root.get_nb_words()    # Delegate the work to the node class

    # Implement the in operator: Returns True if word is in the prefix tree
    def __contains__(self, word):
        node = self._root.find_node(word)           # Locate the node corresponding to the given prefix            
        return (node is not None) and node.is_word  # Return true if the node exists and is a word

if __name__ == '__main__':
    my_words = ['am', 'at', 'ate', 'eat', 'mat', 'me', 'met', 'tea', 'tee']
    my_trie = WordTrie(my_words)

    print(my_trie.get_nb_words('m'))

    empty_trie = WordTrie([])
    print(len(empty_trie))