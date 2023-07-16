import requests
import json

headers = {
    'x-api-key': 'c10ad5c6-768f-4b4c-a42f-ee807e93f763',
}
def anythiink(search_query):
    search_query =search_query.replace(' ', '+')

    response = requests.get(
        f'https://api.scrape-it.cloud/scrape/google?location=Austin%2CTexas%2CUnited+States&q={search_query}&filter=1&domain=google.com&gl=us&hl=en&deviceType=desktop&start=1',
        headers=headers,
    )
    search = json.loads(response.text)

    # Extract snippetHighlitedWords from each result
    snippet_highlited_words = [result.get("snippetHighlitedWords", []) for result in search.get("organicResults", [])]

    # Flatten the list of lists into a single list
    snippet_highlited_words = [word for sublist in snippet_highlited_words for word in sublist]

    # Print the extracted snippetHighlitedWords
    for word in snippet_highlited_words:
        return word
def anythiinks(search_query):
    search_query =search_query.replace(' ', '+')

    response = requests.get(
        f'https://api.scrape-it.cloud/scrape/google?location=Austin%2CTexas%2CUnited+States&q={search_query}&filter=1&domain=google.com&gl=us&hl=en&deviceType=desktop&start=1',
        headers=headers,
    )
    search = json.loads(response.text)

    # Extract snippetHighlitedWords from each result
    snippet_highlited_words = [result.get("snippetHighlitedWords", []) for result in search.get("organicResults", [])]

    # Flatten the list of lists into a single list
    snippet_highlited_words = [word for sublist in snippet_highlited_words for word in sublist]

    # Print the extracted snippetHighlitedWords
    for word in snippet_highlited_words:
      print(word) 
