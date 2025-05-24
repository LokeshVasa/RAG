from pinecone import Pinecone

def retrive_context(query):
    api_key=  "pcsk_HmKNx_4YNZ4EiMRryuEC95vH8RqPJaKV8UJC39eMvsjwb2bLzFc8rnpn4aHW8r6zqcGbp"
    # Initialize a Pinecone client with your API key
    pc = Pinecone(api_key=api_key)

    index_name = "resume"
    dense_index = pc.Index(index_name)

    # Define the query
    

    # Search the dense index
    results = dense_index.search(
        namespace="example-namespace",
        query={
            "top_k": 5,
            "inputs": {
                'text': query
            }
        }
    )


    context= []
    # Print the results
    for hit in results['result']['hits']:
            context.append(hit['fields']['chunk_text'])
            
    #print(context)
    return context