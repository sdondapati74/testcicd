import sys
sys.path.append('/home/runner/work/testcicd/testcicd/vector_store/VectorStore.py')

# Requisite imports
import vector_store.VectorStore  # Importing the VectorStore class from vector_store module
import numpy as np  

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
