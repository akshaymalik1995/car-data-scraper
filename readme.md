# Car Data Scraper

## Overview

Car Data Scraper is a Python application designed to extract and compile detailed information about cars from [cardekho](https://cardekho.com). It specifically targets car and car specs pages to retrieve essential data such as the car's name and price. This tool is invaluable for data analysts, car enthusiasts, or anyone interested in compiling an extensive database of car information.

## Features

- **Efficient Data Extraction**: Utilizes BeautifulSoup to parse and extract data from HTML content.
- **Session Management**: Manages web sessions to optimize the scraping process, making it faster and more reliable.
- **Error Handling**: Implements error handling to gracefully manage and log exceptions, ensuring the scraper's robustness.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your system.
- Familiarity with virtual environments in Python (recommended).

## Installation

1. Clone the repository:

```
git clone https://github.com/akshaymalik1995/car-data-scraper.git
```

2. Navigate to the project directory:

```
cd car-data-scraper
```

3. Create and activate a virtual environment (optional but recommended):

```
python -m venv venv
source venv/bin/activate

# On Windows use
venv\Scripts\activate
```

4. Install the required dependencies:

```
pip install -r requirements.txt
```

## Usage

To use the Car Data Scraper, follow these steps:

1. Run the script:

```
python app.py
```

2. Enter the car company name and model

3. The extracted data will be saved in the csv format.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

- Email - akshaymalik191@gmail.com
- Project Link: [https://github.com/akshaymalik1995/car-data-scraper](https://github.com/yourusername/car-data-scraper)

Feel free to contact me for any questions or contributions to the project.
