import requests
from bs4 import BeautifulSoup
import os
import re

def scrape_download_reviews(url: str) -> bool:
    try:
        dir_path = "/Users/Tango.Tew/Library/CloudStorage/OneDrive-EY/Documents/repos/AI-Projects/review-enforcer-genAI/"
        pages = 5

        # Create an empty list to store the cleaned reviews
        cleaned_reviews = []
        
        for i in range(1, pages + 1):
            # Generate the URL for each page
            current_url = url if i == 1 else f'{url}?page={i}#scroll_to_reviews=true'
                
            response = requests.get(current_url)
            
            if response.status_code != 200:
                print(f"Failed to get the webpage for page {i}. Status code: {response.status_code}")
                return False
            
            soup = BeautifulSoup(response.content, 'html.parser')
            text = soup.get_text()
            
            if text is None:
                print('No text found on the page')
                return False
            
            text = text.split("\n\n")[2]
            text = text[1550:]

            pattern = r'Reviewed (.*?)\n(.*?)\n\s+Thanks for your vote!'
            review_tuples = re.findall(pattern, text, re.DOTALL)
            
            for date, review_text in review_tuples:
                cleaned_text = review_text.replace('\n', ' ').strip()
                cleaned_reviews.append((date, cleaned_text))
        
        # Create the directory if it doesn't exist
        if not os.path.exists(f'{dir_path}/docs'):
            os.makedirs(f'{dir_path}/docs')
            
        # Save all reviews to file
        with open(f'{dir_path}/docs/cleaned_reviews.txt', 'w') as f:
            for date, cleaned_text in cleaned_reviews:
                f.write(f"Date: {date}\n")
                f.write(f"Review: {cleaned_text}\n\n")

        return True
    except Exception as e:
        print(e)
        return False

