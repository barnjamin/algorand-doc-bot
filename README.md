# Algorand docs bot question answering 


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
