#!/usr/bin/env python3
"""
Simple AI Recommendation System
Matches user interests against a built-in database of items.
"""

def get_recommendations():
    # Built-in database of 10 items with keywords
    items = [
        {"name": "The Matrix", "keywords": ["action", "sci-fi", "movie", "thriller"]},
        {"name": "Python Crash Course", "keywords": ["python", "programming", "book"]},
        {"name": "Learn Python", "keywords": ["python", "coding", "book", "tutorial"]},
        {"name": "Machine Learning Masterclass", "keywords": ["python", "ai", "course"]},
        {"name": "The Beatles", "keywords": ["music", "rock", "classic", "band"]},
        {"name": "Interstellar", "keywords": ["sci-fi", "movie", "drama", "space"]},
        {"name": "Web Development with Python", "keywords": ["python", "web", "course"]},
        {"name": "Dune", "keywords": ["sci-fi", "book", "adventure", "epic"]},
        {"name": "Data Science Bootcamp", "keywords": ["python", "data", "course", "ai"]},
        {"name": "Inception", "keywords": ["action", "sci-fi", "movie", "thriller"]},
    ]

    # Get user interests\
    print("=" * 60)
    print("Welcome to the AI Recommendation System!")
    print("=" * 60)
    user_input = input("\nEnter your interests (e.g., 'action movies, python, music'): ").strip().lower()

    if not user_input:
        print("No interests provided. Exiting.")
        return

    # Parse user interests into a list of keywords
    user_interests = [word.strip() for word in user_input.replace(",", " ").split() if word.strip()]

    # Score each item based on keyword matches
    scored_items = []
    for item in items:
        matched_keywords = [kw for kw in item["keywords"] if kw in user_interests]
        scored_items.append({
            "name": item["name"],
            "matches": matched_keywords,
            "score": len(matched_keywords)
        })

    # Sort by score (descending)
    scored_items.sort(key=lambda x: -x["score"])

    # Get top 3 recommendations
    top_3 = scored_items[:3]

    # Display recommendations
    print("\n" + "=" * 60)
    print("Your top recommendations:")
    print("=" * 60)
    for idx, item in enumerate(top_3, 1):
        matches_str = ", ".join(item["matches"]) if item["matches"] else "related content"
        print(f"{idx}. {item['name']} — matches: {matches_str}")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    get_recommendations()
