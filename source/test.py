import sys

from vector_store.VectorStore import VectorStore

print("Hello World")

# Establish a VectorStore instance
vector_store = VectorStore()  # Creating an instance of the VectorStore class

# Define sentences
sentences = [  # Defining a list of example sentences
    "I eat mango",
    "mango is my favorite fruit",
    "mango, apple, oranges are fruits",
    "fruits are good for health",
]

# Tokenization and Vocabulary Creation
vocabulary = set()  # Initializing an empty set to store unique words
for sentence in sentences:  # Iterating over each sentence in the list
    tokens = sentence.lower().split()  # Tokenizing the sentence by splitting on whitespace and converting to lowercase
    vocabulary.update(tokens)  # Updating the set of vocabulary with unique tokens
