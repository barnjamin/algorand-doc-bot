# Algorand docs bot question answering 


## What?

Ran some of the available markdown files through a vector embedding with openai stuff using [langchain](https://langchain.readthedocs.io/en/latest/). Keeping source markdown in git for now

The vector db is written to disk (also in git) and used for questions later. 

## Can I use it?

Get an openai api key then:

1) Install prereqs:

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2) Add your api key:

```sh
export OPENAI_API_KEY="..."
```


3) Run:

```sh
python qa.py "How many box references can I pass in a single app call?"
```

## Can I add to it?

Yes, submit a pr with a markdown document in a new named file in data_sources and I'll add it to the vector db locally then push it.

To add a source locally, follow the steps above to set up the environment. 

Then run:
```sh
python ingest.py -d source_data/$SOURCE_NAME/
```
