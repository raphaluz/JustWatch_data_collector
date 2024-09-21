from src.scraper import Scraper

def main():
    scraper = Scraper()
    try:
        scraper.scrape_website("https://www.justwatch.com/br")     
    finally:
        scraper.close()

if __name__ == "__main__":
    main()