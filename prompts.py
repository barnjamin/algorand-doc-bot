from langchain import PromptTemplate, FewShotPromptTemplate


question_prompt_template = """
Use the following portion of a long document to see if any of the 
text is relevant to answer the question.  
Answer the question using text or code examples. 

{context}
Question: {question}
Answer, if any:"""

combine_prompt_template = """Given the following extracted parts of a developer 
documentation and a question, provide an answer as a developer helping a new developer
trying to understand the tools and protocol.
If you don't know the answer, say 'I don't know', do not try to make up an answer.

QUESTION: How do I encode an address using the python sdk?
=========
source_data/pysdk/text/algosdk/encoding.txt:encode_address(addr_bytes)


source_data/docs/get-details/dapps/smart-contracts/apps/index.md:python3 -c "import algosdk.encoding as e; print(e.encode_address(e.checksum(b'appID'+(1).to_bytes(8, 'big'))))"

Given an address `4H5UNRBJ2Q6JENAXQ6HNTGKLKINP4J4VTQBEPK5F3I6RDICMZBPGNH6KD4`, encoding to and from the public key format can be done as follows:
```python
from algosdk.encoding import decode_address, encode_address

address = "4H5UNRBJ2Q6JENAXQ6HNTGKLKINP4J4VTQBEPK5F3I6RDICMZBPGNH6KD4"
pk = decode_address(address)
addr = encode_address(pk)

assert addr == address
```

=========
ANSWER: Using the python sdk, the method `encoding.encode_address` will\nprovide the encoded address.\n Please see the following code example\n```python
from algosdk.encoding import decode_address, encode_address

address = "4H5UNRBJ2Q6JENAXQ6HNTGKLKINP4J4VTQBEPK5F3I6RDICMZBPGNH6KD4"
pk = decode_address(address)
addr = encode_address(pk)

assert addr == address
```


QUESTION: {question}
=========
{summaries}
=========
ANSWER:"""


question_prompt = PromptTemplate(
    template=question_prompt_template, input_variables=["context", "question"]
)
combine_prompt = PromptTemplate(
    template=combine_prompt_template, input_variables=["summaries", "question"]
)


example_prompt = PromptTemplate(
    template="Content: {page_content}\nSource: {source}",
    input_variables=["page_content", "source"],
)

# question_prompt_template = """
# Use the following portion of a long document to see if any of the
# text is relevant to answer the question.  Return any relevant text verbatim.
# {context}
# Question: {question}
# Relevant text, if any:"""
#
# combine_prompt_template = """
#
# QUESTION: {question}
# =========
# {summaries}
# =========
# FINAL ANSWER:"""
#
# QUESTION_PROMPT = PromptTemplate(
#    template=question_prompt_template, input_variables=["context", "question"]
# )
# COMBINE_PROMPT = PromptTemplate(
#    template=combine_prompt_template, input_variables=["summaries", "question"]
# )
# EXAMPLE_PROMPT = PromptTemplate(
#    template="Content: {page_content}\nSource: {source}",
#    input_variables=["page_content", "source"],
# )


# First, create the list of few shot examples.
# examples = [
#    {
#        "question": "happy",
#        "answer": "sad"
#    },
#    {
#        "question": "tall",
#        "answer": "short"
#    },
# ]
#
## Next, we specify the template to format the examples we have provided.
## We use the `PromptTemplate` class for this.
# example_formatter_template = """
# Question: {question}
# Answer: {answer}\n
# """
# example_prompt = PromptTemplate(
#    input_variables=["question", "answer"],
#    template=example_formatter_template,
# )
#
## Finally, we create the `FewShotPromptTemplate` object.
# few_shot_prompt = FewShotPromptTemplate(
#    examples=examples,
#    example_prompt=example_prompt,
#    prefix="""
#    Answer the question as a member of the developer relations team
#    helping someone to understand how to work with the tools available
#    and the Algorand protocol.
#    """,
#    # The suffix is some text that goes after the examples in the prompt.
#    # Usually, this is where the user input will go
#    suffix="Word: {input}\nAntonym:",
#    # The input variables are the variables that the overall prompt expects.
#    input_variables=["input"],
#    # The example_separator is the string we will use to join the prefix, examples, and suffix together with.
#    example_separator="\n\n",
# )
#
#
