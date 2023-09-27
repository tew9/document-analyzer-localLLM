from review_scrapper import scrape_download_reviews
from llm_run import run_llm
import os


def main():
    print("scrapping...")
    review_url = "https://www.consumeraffairs.com/food/chick-fil-a.html"
    review_file_path = "docs/cleaned_reviews.txt"
    if not os.path.exists(review_file_path):
        scrape_download_reviews(review_url)
        print("reviews saved successfully")
    else:
        print("cleaned_reviews.txt already exists, skipping scraping")
    
    print("running llm...")
    prompt = "give me the most impactful reviews"
    
    insights = run_llm(review_file_path, prompt)
    
    print(f"insights: {insights}")


if __name__ == "__main__":
    main()
