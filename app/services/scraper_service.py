import requests
from bs4 import BeautifulSoup
from app.models.linkedin_page import LinkedInPage
from app.database import SessionLocal

def scrape_and_store_linkedin_page(page_id):
    url = f"https://www.linkedin.com/company/{page_id}/"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return {'error': 'Failed to retrieve the LinkedIn page'}
    
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the data
    page_data = {
        'page_id': page_id,
        'name': soup.find('h1').text.strip() if soup.find('h1') else 'N/A',
        'url': url,
        'profile_picture': soup.find('img', {'class': 'profile-picture'})['src'] if soup.find('img', {'class': 'profile-picture'}) else 'N/A',
        'description': soup.find('div', {'class': 'description'}).text.strip() if soup.find('div', {'class': 'description'}) else 'N/A',
        'website': soup.find('a', {'class': 'website'})['href'] if soup.find('a', {'class': 'website'}) else 'N/A',
        'industry': soup.find('span', {'class': 'industry'}).text.strip() if soup.find('span', {'class': 'industry'}) else 'N/A',
        'followers': int(soup.find('span', {'class': 'followers'}).text.strip().replace(',', '')) if soup.find('span', {'class': 'followers'}) else 0,
        'headcount': int(soup.find('span', {'class': 'head-count'}).text.strip().replace(',', '')) if soup.find('span', {'class': 'head-count'}) else 0,
        'specialities': soup.find('div', {'class': 'specialities'}).text.strip() if soup.find('div', {'class': 'specialities'}) else 'N/A',
    }

    # Create a new LinkedInPage instance and store it in the database
    db = SessionLocal()
    linkedin_page = LinkedInPage(**page_data)

    try:
        db.add(linkedin_page)
        db.commit()  # Commit the transaction
        db.refresh(linkedin_page)  # Refresh the instance to reflect any changes made by the database (e.g., auto-generated ID)
    except Exception as e:
        db.rollback()  # Rollback in case of error
        return {'error': f'Failed to store the data: {str(e)}'}
    finally:
        db.close()  # Close the session

    return {'success': f'LinkedIn page {page_id} data stored successfully.'}
