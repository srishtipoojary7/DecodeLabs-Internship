"""DecodeLabs - Artificial Intelligence Project 3: AI Recommendation Logic."""
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DATA_FILE = "items.csv"

def load_items():
    return pd.read_csv(DATA_FILE)

def build_recommendations(user_preferences, items, top_n=5):
    corpus = [user_preferences] + items["description"].fillna("").tolist()
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform(corpus)
    scores = cosine_similarity(vectors[0:1], vectors[1:]).flatten()
    result = items.copy()
    result["similarity_score"] = scores
    return result.sort_values("similarity_score", ascending=False).head(top_n)

def main():
    print("=" * 60)
    print("       DecodeLabs - AI Recommendation Logic")
    print("=" * 60)
    print("Enter your interests separated by commas.")
    print("Example: python, artificial intelligence, data science\n")
    user_input = input("Your interests: ").strip()
    if not user_input:
        print("Please enter at least one interest.")
        return
    items = load_items()
    recommendations = build_recommendations(user_input, items)
    print("\nRecommended items:")
    print("-" * 60)
    for _, row in recommendations.iterrows():
        print(f"{row['item']}")
        print(f"Category : {row['category']}")
        print(f"Match    : {row['similarity_score']:.2%}")
        print(f"Reason   : {row['description']}")
        print("-" * 60)

if __name__ == "__main__":
    main()
