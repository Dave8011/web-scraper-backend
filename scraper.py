import requests
from bs4 import BeautifulSoup

def scrape_title(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.title.string if soup.title else "No title found"
    except Exception as e:
        return f"Error: {e}"
def scrape_data(url):
    # Example dummy response
    return {
        'url': url,
        'title': 'Fake Title from ' + url,
        'content': 'This is just sample scraped content.'
    }
