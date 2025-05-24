from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

from pinecone_retrival import retrive_context


template = """context : {context}
                Question: {question}
                based on the context pick the right answer and provide the answer no extra words"""
                
prompt = ChatPromptTemplate.from_template(template)
model = OllamaLLM(model="llama3.2")
chain = prompt | model

# getting right context is
# forward and backward passes is repeated for multiple iterations (epochs) until the network converges to a solution where the error is minimized"]

while True:
    # ai_msg= chain.invoke({"context": context, "question": "when should I apply wfh"})
    question= str(input("Enter Query: "))
    context= retrive_context(question)
    context= " ".join(context)
    if question=="exit":
        break
    ai_msg= chain.invoke({"context": context, "question": question})

    print(ai_msg)