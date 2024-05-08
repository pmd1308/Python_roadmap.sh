'''
    This script implements a binary search tree to efficiently store
    and retrieve word definitions, allowing insertion words with their 
    corresponding definitions, updating existing definitions, and 
    searching for definitions based on query words.
    ----------------------------------------------------------------
    The script's focus on handling definitions, and updates makes it 
    suitable for applications like dictionaries, thesauri, spell 
    checkers and NPL tasks involving word meanings.
    ----------------------------------------------------------------
    Applying set theory, Its obatain a percentage value through an 
    aritmétic operation, which defines the similarity relationship 
    between searched word and the saved node, returning the the one
    with the greatest similarity similarity
    ----------------------------------------------------------------
    Concepts:
    - Data Structure
    - Binary Search
    - Strings
    - Error handling
    - Class and Methods
    - Set Theory
'''

class TreeNode:
    def __init__(self, word, definition):
        self.word = word
        self.definition = definition
        self.left = None
        self.right = None

class binarySearchTree:
    def __init__(self):
        self.root = None
        self.words = []
        self.definitions = []

    def insert(self, word, definition):
        '''
        Inserts a word and its definition into the tree.
        '''
        if not word or not definition:
            return "This empty word and definition"
        
        if not self.root:
            self.root = TreeNode(word, definition)
        else:
            self._insert_recursively(self.root, word, definition)
        self._update_lists(word, definition)

    def _insert_recursively(self, node, word, definition):
        '''
        Recursively inserts a word and its definition into the tree.
        '''
        if not word or not definition:
            return "This empty word and definition"
        if word.lower() < node.word.lower():
            if node.left:
                self._insert_recursively(node.left, word, definition)
            else:
                node.left = TreeNode(word, definition)
        elif word.lower() > node.word.lower():
            if node.right:
                self._insert_recursively(node.right, word, definition)
            else:
                node.definitions.append(definition)

    def _update_lists(self, word, definition):
        '''
        Updates the words and definitions lists.
        '''
        if not word or not definition:
            return "This empty word and definition"
        index = next((i for i, w in enumerate(self.words) if w.lower() == word.lower()), -1)
        if index == -1:
            # If exists, update...
            self.definitions[index] = definition
        else:
            self.words.append(word)
            self.definitions.append(definition)

    def search(self, query):
        if not query:
            return "This empty query"
        if not isinstance(query, str):
            return "This query is not a string"

        query_lower()
        max_similarity = 0
        most_similar_definition = None

        try:
            for word, definition in zip(self.words, self.definitions):
                word_lower = word.lower()
                instersection = len(set(query_lower).instersection(set(word_lower)))
                union = len(set(query_lower).union(set(word_lower)))
                similarity = instersection / union                
            
                if similarity > max_similarity:
                    max_similarity = similarity
                    most_similar_definition = definition
        except Exception as e:
            print(e)
        return most_similar_definition

def menu():
    print("Welcome to the Binary Search Tree Dictionary!")
    print("Please choose one of the following options:")
    print("1. Insert a word and its definition")
    print("2. Update a word's definition")
    print("3. Search for a word's definition")
    print("4. Quit")

if __name__ == "__main__":
    bst = binarySearchTree()
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            word = input("Enter the word: ")
            definition = input("Enter the definition: ")
            bst.insert(word, definition)
        elif choice == "2":
            word = input("Enter the word: ")
            definition = input("Enter the definition: ")
            bst.update(word, definition)
        elif choice == "3":
            word = input("Enter the word: ")
            definition = bst.search(word)
            print(definition)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")