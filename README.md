# Zillow Rental Scraper & Google Form Submission

This Python project automates the process of scraping rental listings from a Zillow clone website and submitting the scraped data to a Google Form. It combines **web scraping** with **browser automation** using `BeautifulSoup` and `Selenium`.

---

## Features

- Scrapes rental data including:
  - **Addresses**
  - **Prices**
  - **Links to listings**
- Automatically submits each scraped property to a Google Form.
- Handles page load delays and dynamic content with Selenium’s explicit waits.
- Works with Firefox WebDriver and Google Forms.

---

## Technologies Used

- Python 3
- [Selenium](https://www.selenium.dev/) for browser automation
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) for web scraping
- `requests` for fetching web page content
- Firefox WebDriver (GeckoDriver)

---

## Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd <repo-folder>
````

Install required Python packages:
````bash
pip install selenium beautifulsoup4 requests
````

Download **GeckoDriver** and make sure it’s in your system PATH.

## Usage

Open the Python script (main.py) and verify the URLs:
````bash
ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"
FORMS_URL = "https://forms.gle/k6aois5PdhDe5E
````

Run the script:
````bash
python main.py
````

The script will:

- Scrape all rental listings from the Zillow clone page.

- Open Firefox, navigate to the Google Form.

- Fill in each property’s address, price, and link.

- Submit the form automatically for each property.

## How It Works

1. Scraping with BeautifulSoup

- Fetches the Zillow clone HTML using requests.

- Extracts prices, links, and addresses using CSS selectors.

2. Form Submission with Selenium

- Opens the Google Form in Firefox.

- Waits for input fields to load using WebDriverWait.

- Enters each property’s data into the form.

- Clicks the submit button automatically.

3. Looping through listings

- Each property is submitted one at a time.

- Ensures no data is missed or overwritten.

## Notes

- Make sure Firefox is installed and compatible with the GeckoDriver version.

- Google Forms layout may change, so XPaths or selectors might need updates in the future.

- The script currently uses a visible browser window; you can enable headless mode for faster automation.

## License

This project is open-source and free to use for educational purposes.

### Author `mazerissa`