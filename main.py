from review_scrapper import scrape_download_reviews
import os

def main():
    print('scrapping...')
    url = 'https://www.consumeraffairs.com/food/chick-fil-a.html'
    if not os.path.exists('docs/cleaned_reviews.txt'):
        scrape_download_reviews(url)
        print('reviews saved successfully')
    else:
        print('cleaned_reviews.txt already exists, skipping scraping')

    

if __name__ == '__main__':
   main()