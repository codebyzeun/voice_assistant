import requests

def tell_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    if response.status_code == 200:
        joke = response.json()
        return f"Here's a joke for you: {joke['setup']} ... {joke['punchline']}"
    else:
        return "Sorry, I couldn't fetch a joke right now."
