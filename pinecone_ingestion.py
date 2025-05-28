# Import the Pinecone library and PDF chunking function
from pdf_reader import read_pdf_and_chunk
from pinecone import Pinecone

# Your Pinecone API key
api_key = "pcsk_HmKNx_4YNZ4EiMRryuEC95vH8RqPJaKV8UJC39eMvsjwb2bLzFc8rnpn4aHW8r6zqcGbp"

# Initialize the Pinecone client
pc = Pinecone(api_key=api_key)

# Use a lowercase index name (case-sensitive)
index_name = "nptel"

# Create the index if it doesn't exist
if not pc.has_index(index_name):
    pc.create_index_for_model(
        name=index_name,
        cloud="aws",
        region="us-east-1",
        embed={
            "model": "llama-text-embed-v2",
            "field_map": {"text": "chunk_text"}
        }
    )

# ✅ Corrected: use a direct Windows path, not a file:// URL
chunks = read_pdf_and_chunk(r"D:\New folder\nptel.pdf")

# Prepare records for upsertion
records = [{"_id": f"rec_{i}", "chunk_text": chunk} for i, chunk in enumerate(chunks)]

# Print to verify the content before uploading (optional)
print(f"Prepared {len(records)} records.")

# Target the correct index
dense_index = pc.Index(index_name)

# Upsert records into a namespace
dense_index.upsert_records(namespace="example-namespace", records=records[:94])
