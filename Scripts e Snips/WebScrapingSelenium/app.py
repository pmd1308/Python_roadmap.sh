import argparse
from web_scraper import WebScraper
from utils import get_user_input

def main():
    parser = argparse.ArgumentParser(description="Web scraping script with Selenium.")
    parser.add_argument('url', type=str, help="The URL of the page to be accessed.")
    parser.add_argument('tag_name', type=str, help="The tag name of the element you want to extract.")
    parser.add_argument('--cookie_file', type=str, default='cookies.json', help="Path to save the cookie file.")
    parser.add_argument('--wait_for', type=str, default='body', help="Selector of the element to wait for.")
    parser.add_argument('--wait_type', type=str, choices=['id', 'name', 'xpath', 'tag', 'class', 'css'], default='tag', help="Type of selector of the element to wait for.('id', 'name', 'xpath', 'tag', 'class', 'css')")

    args = parser.parse_args()
    
    scraper = WebScraper(chrome_driver_path="/path/to/chromedriver")
    scraper.scrape(args.url, args.tag_name, args.cookie_file, args.wait_for, args.wait_type)

if __name__ == "__main__":
    main()