import requests
from bs4 import BeautifulSoup
import time  # ✅ Required for retry delay

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
}

def scrape_title(url):
    try:
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.title.string if soup.title else "No title found"
    except requests.exceptions.ReadTimeout:
        print("Timeout. Retrying...")
        time.sleep(2)
        try:
            response = requests.get(url, headers=headers, timeout=15)
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup.title.string if soup.title else "No title found"
        except Exception as e:
            return f"Error: {e}"
    except Exception as e:
        return f"Error: {e}"
