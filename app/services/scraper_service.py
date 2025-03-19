import requests
from bs4 import BeautifulSoup

def scrape_linkedin_page(page_id):
    url = f"https://www.linkedin.com/company/{page_id}"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    
    return {
        "page_id": page_id,
        "name": soup.find("title").text.strip(),
        "url": url,
        "description": "Extracted description...",
        "total_followers": 10000  # Dummy value
    }
