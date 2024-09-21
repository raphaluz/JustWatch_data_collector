import unittest
from src.scraper import Scraper

class TestScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = Scraper()

    def tearDown(self):
        self.scraper.close()

    def test_scrape_website(self):
        pass

if __name__ == '__main__':
    unittest.main()
