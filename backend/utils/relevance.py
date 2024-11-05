from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

def check_relevance(prompt: str, context: str, threshold=0.5) -> bool:
    vectorizer = TfidfVectorizer().fit_transform([prompt, context])
    vectors = vectorizer.toarray() 
    similarity = cosine_similarity([vectors[0]], [vectors[1]])[0][0]
    
    return similarity > threshold
