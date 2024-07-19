# Dutch Wiki Web Scraper

This project is a web scraper that extracts information from the [Dutch](https://www.gordijnen.nl/wiki) Website, which provides detailed information about window decoration. The scraper is built using Selenium in Python, allowing for robust and efficient data extraction.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Installation

To get started with this project, clone the repository and install the required dependencies.

```bash
git clone https://github.com/yourusername/gordijnen-wiki-scraper.git
pip install -r requirements.txt
```

## Usage

1. **Configure the scraper:**
   - Open `config.py` and set the URL and other parameters as needed.

2. **Run the scraper:**
   - Execute the main script to start scraping the data.

```bash
python scraper.py
```

3. **Output:**
   - The scraped data will be saved into a Text file named `items.txt` in the project directory.

## Features

- Scrapes detailed information about various window decoration topics.
- Utilizes Selenium for browser automation.
- Saves the scraped data into a Text file.
- Handles dynamic content and JavaScript-rendered pages.

## Dependencies

- Python 3.7+
- Selenium
- Pandas
- WebDriver (e.g., ChromeDriver, GeckoDriver)

Install the required dependencies using:

```bash
pip install -r requirements.txt
```

You also need to download the appropriate WebDriver for your browser and ensure it is in your system PATH.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please open an issue or create a pull request.

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Open a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### requirements.txt

You will also need to download the appropriate WebDriver for your browser (e.g., ChromeDriver for Chrome, GeckoDriver for Firefox) and ensure it is in your system PATH.