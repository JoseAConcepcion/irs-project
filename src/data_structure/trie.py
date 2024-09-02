class TrieNode:
    def __init__(self):
        """
        Initializes a new TrieNode.

        :ivar children: Dictionary to store child nodes (default is empty).
        :ivar is_end_of_word: Boolean flag indicating if this node represents the end of a word (default is False).
        """
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        """
        Initializes a new Trie data structure.

        Creates a root node for the Trie.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the Trie.

        :param word: String to be inserted into the Trie.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, prefix):
        """
        Searches for words starting with the given prefix in the Trie.

        :param prefix: String representing the beginning of the words to search for.
        :return: List of words found in the Trie that start with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._find_words(node, prefix)

    def _find_words(self, node, prefix):
        """
        Recursively finds all words starting from the given node.

        :param node: Current TrieNode to start searching from.
        :param prefix: Prefix string to append to found words.
        :return: List of words found in the subtree rooted at the given node.
        """
        words = []
        if node.is_end_of_word:
            words.append(prefix)
        for char, child_node in node.children.items():
            words.extend(self._find_words(child_node, prefix + char))
        return words
