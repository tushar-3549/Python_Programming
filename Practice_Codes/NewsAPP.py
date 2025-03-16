import requests
from datetime import datetime, timedelta


API_KEY = '097ce638a3554620adf35f86f7333a16'
BASE_URL = 'https://newsapi.org/v2/everything'

# https://newsapi.org/v2/everything?q={query}&from=2025-02-16&sortBy=publishedAt&apiKey=API_KEY

def fetch_news(query):
    from_date = (datetime.today() - timedelta(days=10)).strftime('%Y-%m-%d')
    to_date = datetime.today().strftime('%Y-%m-%d')
    
    params = {
        'q': query,
        'from': from_date,
        'to': to_date,
        'sortBy': 'publishedAt',
        'apiKey': API_KEY
    }
    response = requests.get(BASE_URL, params = params)
    
    if response.status_code == 200:
        data = response.json()
        # print(data)
        articles = data.get("articles", [])
        
        if not articles:
            print("No news found for this topic.")
            return
        
        print(f"\nTop {len(articles)} news for '{query}':\n")
        for i, article in enumerate(articles, start=1):
            print(f"{i}. {article['title']}")
            print(f"   {article['url']}\n")
            
    else:
        print("Error:", response.status_code, response.json())


if __name__ == "__main__":
    query = input('Enter a topic to search name: ')
    fetch_news(query)
