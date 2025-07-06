# Wedding Venue Scraper

This Scrapy project scrapes wedding venue data from [wedding-spot.com](https://www.wedding-spot.com), 
cleans and processes the data, and exports it in multiple formats including CSV and JSON.

---

## Features

- Crawl multiple pages of wedding venues
- Extract details like name, contact, guest capacity, location, and highlights
- Clean and normalize scraped data through pipelines
- Remove duplicate highlights and format output neatly
- Export data to CSV or JSON files

---

## Requirements

- Python 3.7+
- Scrapy

1) For Linux/Debian 
    Use these commands 
        ```console
        sudo apt update
        sudo apt install python3 python3-pip
        pip3 install scrapy
        ```
2) For MacOS (Use Homebrew)
    Use these commands 
        ```console
        brew install python
        pip3 install scrapy
        ```

    If you dont have homebrew installed, 
    install homebrew from https://brew.sh/ and then run those command

3) For Windows
    Download and install Python 3.7+ from the official website:
    https://www.python.org/downloads/

    Then, use pip to install scrapy 
        ```console
        pip install scrapy
        ```

---

## Setup Instructions


### 1. Clone the Repository

First, clone the project to your local machine:

    ```console
    git clone https://github.com/dashivam06/wedding_venue_scraper.git
    cd wedding_venue_scraper
    ```

### 2. Run the spider 

    ```console
    scrapy crawl wedding_venue_spider
    ```
### 3. Export Data

    a) To export the scraped data as a JSON file:

    ```console
    scrapy crawl wedding_venue_spider -o output.json
    ```    

    b) To export the scraped data as a CSV file:

    ```console
    scrapy crawl wedding_venue_spider -o output.csv
    ```
    NOTE : 
        You can replace output.json or output.csv with any filename you prefer.
        The exported data files will be saved in your current working directory.

---




