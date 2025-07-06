# Wedding Venue Scraper

This Scrapy project scrapes wedding venue data from [wedding-spot.com](https://www.wedding-spot.com/wedding-venues/?pr=new%20jersey&r=new%20jersey%3anorth%20jersey&r=new%20jersey%3aatlantic%20city&r=new%20jersey%3ajersey%20shore&r=new%20jersey%3asouth%20jersey&r=new%20jersey%3acentral%20jersey&r=new%20york%3along%20island&r=new%20york%3amanhattan&r=new%20york%3abrooklyn&r=pennsylvania%3aphiladelphia&sr=1), 
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



### 1) For Linux/Debian

```bash
sudo apt update
sudo apt install python3 python3-pip
pip3 install scrapy
```

### 2) For MacOS (Use Homebrew)
```bash
brew install python
pip3 install scrapy
```
Note :
    If you dont have homebrew installed, 
    Install homebrew from https://brew.sh/ and then run those command

3) For Windows
    Download and install Python 3.7+ from the official website:
    https://www.python.org/downloads/

    Then, use pip to install scrapy 
        ```
        pip install scrapy
        ```

---

## Setup Instructions


### 1. Clone the Repository

First, clone the project to your local machine and move to that folder :

    ```
    git clone https://github.com/dashivam06/wedding_venue_scraper.git
    cd wedding_venue_scraper
    ```

### 2. Run the spider 

    ```
    scrapy crawl wedding_venue_spider
    ```
### 3. Export Data

    a) To export the scraped data as a JSON file:

    ```
    scrapy crawl wedding_venue_spider -o output.json
    ```    

    b) To export the scraped data as a CSV file:

    ```
    scrapy crawl wedding_venue_spider -o output.csv
    ```
    NOTE : 
        You can replace output.json or output.csv with any filename you prefer.
        The exported data files will be saved in your current working directory.

---




