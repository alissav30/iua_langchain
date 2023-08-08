import os
import sys
import constants
import langchain

os.environ["OPENAI_API_KEY"] = constants.APIKEY

query = sys.argv[1]

from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.document_loaders import DirectoryLoader
#from langchain.cache import InMemoryCache


#langchain.llm_cache = InMemoryCache()

print(DirectoryLoader)

#loader = DirectoryLoader('../', glob="**/*.txt", show_progress=True)
#print("loader", loader)
#documents = loader.load()
loader = TextLoader('CONSTITUTION.txt')
#docs = loader.load()
index = VectorstoreIndexCreator().from_loaders([loader])
print("index", index)

print(index.query(query))
