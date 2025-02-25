# Web Scraping Project

This project is a web scraping script designed to extract product information from a website. It uses Python and libraries like requests, BeautifulSoup, and Selenium to scrape data and store it in a structured format.

### Approach

1. Static Content Scraping: For static websites, the script uses the requests library to fetch the HTML content and BeautifulSoup to parse and extract data.
2. Dynamic Content Scraping: For websites with JavaScript-rendered content, the script uses Selenium to simulate a browser and load the dynamic content.
3. Data Storage: The scraped data is stored in a JSON file for further analysis or processing.

### Dependencies Required

To run this script, you need the following Python libraries:

- requests
- BeautifulSoup
- Selenium
- pandas (optional, for data manipulation)
- json (for saving data)

### How to Run the Script

Follow these steps to run the web scraping script:
#### Step 1: Clone the Repository

Clone this repository to your local machine:

    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name

#### Step 2: Install Dependencies

Install the required Python libraries:

    pip install -r requirements.txt

#### Step 3: Run the Script

Execute the script using Python:

    python scrape.py

#### Step 4: View the Output

The scraped data will be saved in a file named products.json in the project directory.

### Challenges Faced and Solutions

1. Bot Protection:

    Some websites use bot detection mechanisms to block scraping scripts.
  
    *Solution*: Use Selenium with a headless browser and rotate user agents to mimic human behavior.

2. Dynamic Content:

    Some websites load content dynamically using JavaScript.

    *Solution*: Use Selenium to render the JavaScript and extract the data.

3. Rate Limiting:

   Websites may block IP addresses that send too many requests in a short time.

   *Solution*: Add delays between requests using time.sleep().

4. Inconsistent HTML Structure:

   Some websites have inconsistent HTML structures, making it difficult to locate elements.

   *Solution*: Use flexible selectors and error handling to handle edge cases.

### Sample Output

Here are the first 5 products scraped by the script:

-- the different categories were either not loading or taking too long to load
  Possible causes --> Different amounts of data loading on different pages
  solution --> had to load each category separately

-- some links were not working and throwing errors

-- Stored data of a particular category in a corresponding json file.
-- Then combine them all to one file.
