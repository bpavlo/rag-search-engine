#!/usr/bin/env python3

import argparse
import json
import string

def preprocess_text(text: str) -> str:
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text

def search_movies(query: str) -> None:
     with open('data/movies.json', 'r') as f:
         data = json.load(f)

     results = []

     for movie in data['movies']:
         if preprocess_text(query) in preprocess_text(movie['title']):
             results.append(movie)

     results.sort(key=lambda x: x['id'])
     results = results[:5]

     print(f"Searching for: {query}")
     for i, movie in enumerate(results, 1):
         print(f"{i}. {movie['title']}")

def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using BM25")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()

    match args.command:
        case "search":
            search_movies(args.query)
            pass
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()

