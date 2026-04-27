from sentence_transformers import SentenceTransformer

# Use same cache folder as above
model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2",
    cache_folder=r"C:\Users\MirdulaaBalaji\.huggingface_cache"
)
print("Model downloaded successfully")