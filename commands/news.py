import requests

def get_news():
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=your_news_api_key"
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json()['articles']
        headlines = [article['title'] for article in articles[:5]]
        return f"Here are the latest headlines: {', '.join(headlines)}"
    else:
        return "Sorry, I couldn't fetch the news right now."
