import time
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

def check_relevance(prompt: str, context: str, threshold=0.5) -> bool:
    start_time = time.time()  # Start time for performance monitoring
    
    vectorizer = TfidfVectorizer().fit_transform([prompt, context])
    vectors = vectorizer.toarray()  # Ensure you convert to array for cosine similarity
    similarity = cosine_similarity([vectors[0]], [vectors[1]])[0][0]
    
    end_time = time.time()  # End time for performance monitoring
    logging.info(f"check_relevance execution time: {end_time - start_time:.4f} seconds")
    
    return similarity > threshold
