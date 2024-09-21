# Web Scraping Project

This project is a web scraper for JustWatch built using Python and Selenium.

## Setup

1. Install Python 3.7+
2. Install dependencies: `pip install -r requirements.txt`
3. Download ChromeDriver that matches your Chrome browser version
4. Place the ChromeDriver executable in the `drivers/` directory

## Usage

Run the scraper:

```
python src/scraper.py
```

Run tests:

```
python -m unittest discover tests
```

## Project Structure

- `src/`: Contains the main source code
- `tests/`: Contains unit tests
- `data/`: Stores scraped data
- `drivers/`: Contains the ChromeDriver executable

## ChromeDriver

Make sure to download the ChromeDriver version that matches your Chrome browser version. Place the executable in the `drivers/` directory. The script will automatically locate it.

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details