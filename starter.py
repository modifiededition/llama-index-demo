import logging
import sys
import os

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage


logging.basicConfig( stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

PERSISTENT_DIR = "./storage"
if not os.path.exists(PERSISTENT_DIR):
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)

    index.storage_context.persist(persist_dir=PERSISTENT_DIR)
else:
    storage_context = StorageContext.from_defaults(persist_dir=PERSISTENT_DIR)
    index = load_index_from_storage(storage_context)

query_engine = index.as_query_engine()
response = query_engine.query("What did the author do growing up?")
print(response)
