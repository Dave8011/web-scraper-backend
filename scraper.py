import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import time  # Required for retry delay

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
}

def scrape_title(url):
    domain = urlparse(url).netloc.lower()

    if "amazon" in domain:
        return scrape_amazon(url)
    elif "flipkart" in domain:
        return scrape_flipkart(url)
    else:
        return scrape_generic(url)


# 🟠 Generic scraper (fallback for other sites)
def scrape_generic(url):
    try:
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string.strip() if soup.title else "No title"
        return {
            "title": title,
            "price": "N/A",
            "rating": "N/A"
        }
    except requests.exceptions.ReadTimeout:
        time.sleep(1)
        return {"error": "Timeout while fetching URL"}
    except Exception as e:
        return {"error": str(e)}


# 🟢 Amazon scraper
def scrape_amazon(url):
    try:
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.select_one('#productTitle')
        price = soup.select_one('.a-price-whole')
        rating = soup.select_one('.a-icon-alt')

        return {
            "title": title.text.strip() if title else "No title",
            "price": price.text.strip() if price else "N/A",
            "rating": rating.text.strip() if rating else "N/A"
        }
    except Exception as e:
        return {"error": str(e)}


# 🔵 Flipkart scraper
def scrape_flipkart(url):
    try:
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.select_one('span.B_NuCI')
        price = soup.select_one('._30jeq3')
        rating = soup.select_one('._3LWZlK')

        return {
            "title": title.text.strip() if title else "No title",
            "price": price.text.strip() if price else "N/A",
            "rating": rating.text.strip() if rating else "N/A"
        }
    except Exception as e:
        return {"error": str(e)}
