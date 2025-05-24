
# Import the Pinecone library
from pdf_reader import read_pdf_and_chunk
from pinecone import Pinecone


api_key=  "pcsk_HmKNx_4YNZ4EiMRryuEC95vH8RqPJaKV8UJC39eMvsjwb2bLzFc8rnpn4aHW8r6zqcGbp"


# Initialize a Pinecone client with your API key
pc = Pinecone(api_key=api_key)

# Create a dense index with integrated embedding
index_name = "resume"
if not pc.has_index(index_name):
    pc.create_index_for_model(
        name=index_name,
        cloud="aws",
        region="us-east-1",
        embed={
            "model":"llama-text-embed-v2",
            "field_map":{"text": "chunk_text"}
        }
    )
    

chunks= read_pdf_and_chunk(r"C:\Users\lokes\Downloads\Lokesh_Chandra_Resume (1).pdf")

records= []

for i, chunk in enumerate(chunks):
    records.append({"_id": f"rec_{i}", "chunk_text": chunk})
    
print(records)
    
# Target the index
dense_index = pc.Index(index_name)

# Upsert the records into a namespace
dense_index.upsert_records("example-namespace", records[:94])
        

    
