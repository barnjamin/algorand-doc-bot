from langchain import PromptTemplate

###

example_prompt = PromptTemplate(
    template="Content: {page_content}\nSource: {source}",
    input_variables=["page_content", "source"],
)

###


question_prompt = PromptTemplate(
    template="""
Use the following portion of a long document to see if any of the text is relevant to answer the question.  Answer the question using text or code examples. 

{context}
Question: {question}
Answer, if any:""",
    input_variables=["context", "question"],
)


#####


src1 = """
encode_address(addr_bytes)

   Encode a byte address into a string composed of the encoded bytes
   and the checksum.

   Parameters:
      **addr_bytes** (*bytes*) -- address in bytes

   Returns:
      base32 encoded address

   Return type:
      str
""".replace(
    "\n", "\\n"
)


src2 = """```python
from algosdk.encoding import decode_address, encode_address

address = "4H5UNRBJ2Q6JENAXQ6HNTGKLKINP4J4VTQBEPK5F3I6RDICMZBPGNH6KD4"
pk = decode_address(address)
addr = encode_address(pk)

assert addr == address
```""".replace(
    "\n", "\\n"
)

search_answer = """Using the python sdk, the method `encoding.encode_address` will provide the encoded address.

Please see the following code example:
```python
from algosdk.encoding import decode_address, encode_address

address = "4H5UNRBJ2Q6JENAXQ6HNTGKLKINP4J4VTQBEPK5F3I6RDICMZBPGNH6KD4"
pk = decode_address(address)
addr = encode_address(pk)

assert addr == address
```
""".replace(
    "\n", "\\n"
)


combine_prompt_template = (
    """Given the following extracted parts of a long document and a question, create a final answer with references ("SOURCES"). 
If you don't know the answer, just say that you don't know. Don't try to make up an answer.
ALWAYS return a "SOURCES" part in your answer.

QUESTION: How do I encode an address using the python sdk?
=========
Content: """
    + src1
    + """ 
Source: source_data/pysdk/text/algosdk/encoding.txt 70:82

Content: """
    + src2
    + """
Source: source_data/docs/get-details/encoding.md 57:66

=========
FINAL ANSWER: """
    + search_answer
    + """
SOURCES:


QUESTION: {question}
=========
{summaries}
=========
FINAL ANSWER:"""
)


combine_prompt = PromptTemplate(
    template=combine_prompt_template, input_variables=["summaries", "question"]
)
