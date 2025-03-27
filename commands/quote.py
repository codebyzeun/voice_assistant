import requests

def get_quote():
    url = "https://api.quotable.io/random"
    response = requests.get(url)
    if response.status_code == 200:
        quote = response.json()
        return f"Here's your quote: {quote['content']} — {quote['author']}"
    else:
        return "Sorry, I couldn't fetch a quote right now."
