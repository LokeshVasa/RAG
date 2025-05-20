from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM


template = """context : {context}
                Question: {question}
                based on the context pick the right answer and provide the answer no extra words"""
                
prompt = ChatPromptTemplate.from_template(template)
model = OllamaLLM(model="llama3.2")
chain = prompt | model

# getting right context is
context= ["Backpropagation is a supervised learning algorithm used for training neural networks. The key idea is to minimize the error (or loss) by adjusting the weights of the network.","1.	Forward Pass: The input data is passed through the network layer by layer, and each layer applies a set of weights and an activation function to produce the output. The final output is compared to the target output to calculate the error (or loss).","2.Backward Pass: The error is propagated back through the network from the output layer to the input layer. This involves computing the gradient of the error with respect to each weight in the network","3.	Weight Update: The weights are adjusted using the gradient descent algorithm. The weights are updated in the direction that reduces the error, based on the calculated gradients. The learning rate determines the size of the steps taken during weight updates."
,"The process of forward and backward passes is repeated for multiple iterations (epochs) until the network converges to a solution where the error is minimized"]

while True:
    # ai_msg= chain.invoke({"context": context, "question": "when should I apply wfh"})
    question= str(input("Enter Query:-"))
    if question=="exit":
        break
    ai_msg= chain.invoke({"context": context, "question": question})

    print(ai_msg)