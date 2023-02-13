"""This is the logic for ingesting Notion data into LangChain."""
from pathlib import Path
from langchain.text_splitter import CharacterTextSplitter
import faiss
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
import pickle
import argparse


# Here we load in the data in the format that Notion exports it in.

parser = argparse.ArgumentParser(description="Ingest markdown or csv from a directory")
parser.add_argument(
    "-d",
    "--directory",
    type=str,
    help="The directory to use for training",
    default="source_data/",
)

args = parser.parse_args()

ps = list(Path(args.directory).glob("**/*.md"))

data = []
sources = []
for p in ps:
    with open(p) as f:
        data.append(f.read())
    sources.append(p)

# Here we split the documents, as needed, into smaller chunks.
# We do this due to the context limits of the LLMs.
text_splitter = CharacterTextSplitter(chunk_size=2000, separator="\n")
docs = []
metadatas = []
for i, d in enumerate(data):
    splits = text_splitter.split_text(d)
    docs.extend(splits)
    metadatas.extend([{"source": sources[i]}] * len(splits))


# Here we create a vector store from the documents and save it to disk.
# TODO: check if it exists, then load it or make a new one 
#new_store = FAISS.from_texts(docs, OpenAIEmbeddings(), metadatas=metadatas)
with open("faiss_store.pkl", "rb") as f:
    current_store: FAISS = pickle.load(f)
current_store.index = faiss.read_index("docs.index")

current_store.add_texts(docs,  metadatas=metadatas)

faiss.write_index(current_store.index, "docs.index")
current_store.index = None
with open("faiss_store2.pk", "wb") as f:
    pickle.dump(current_store, f)
