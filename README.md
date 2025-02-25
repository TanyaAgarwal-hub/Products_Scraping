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

Install the required Python libraries.

#### Step 3: Run the Script

Execute the script using Python:

    python file_name.py

#### Step 4: View the Output

The scraped data will be saved in a file named products.json in the project directory.

### Challenges Faced and Solutions

1. Bot Protection:

    Some websites use bot detection mechanisms to block scraping scripts.
  
    *Solution*: Use Selenium with a headless browser and rotate user agents to mimic human behavior.

2. Dynamic Content:

    Some websites load content dynamically using JavaScript.

    *Solution*: Use Selenium to render the JavaScript and extract the data.

3. Content Extraction:

   Different pages may take different times to load content, because of varying amount of data.

   *Solution*: Instead of iterating through categories, making individual json files and finally combining them.

4. Errors encountered:

   As I was making use of Google Colab to run my code, inconsistent errors were occuring.

   *Solution*: Loading categories individually and storing data in separate json files.

### Sample Output

Here are the first 5 products scraped by the script:

            [
                {
                    "Category": "OTOP",
                    "Quantity": "30g",
                    "Product Name": "Doikham Savoury Strawberry",
                    "Product Images": "https://assets.tops.co.th/DOIKHAM-DoikhamSavouryStrawberry30g-8850773551115-1?$JPEG$",
                    "Barcode Number": "8850773551115",
                    "Price": "30 Baht",
                    "Labels": [
                        "Snacks & Desserts",
                        "Nuts & Dried Fruit",
                        "Dried Fruit"
                    ],
                    "Product Details": "The product received may be subject to package modification and quantity from the manufacturer."
                },
                {
                    "Category": "OTOP",
                    "Quantity": "140g",
                    "Product Name": "Doikham Dried",
                    "Product Images": "https://assets.tops.co.th/DOIKHAM-DoikhamDriedMango140g-8850773550262-1?$JPEG$",
                    "Barcode Number": "8850773550262",
                    "Price": "80 Baht",
                    "Labels": [
                        "Shop by Brands",
                        "I LOVE THAILAND",
                        "Thai Dried Fruits & Thai Snacks"
                    ],
                    "Product Details": "The product received may be subject to package modification and quantity from the manufacturer."
                },
                {
                    "Category": "OTOP",
                    "Quantity": "140g",
                    "Product Name": "Doikham Dried Strawberry",
                    "Product Images": "https://assets.tops.co.th/DOIKHAM-DoikhamDriedStrawberry140g-8850773550279-1?$JPEG$",
                    "Barcode Number": "8850773550279",
                    "Price": "155 Baht",
                    "Labels": [
                        "Shop by Brands",
                        "I LOVE THAILAND",
                        "Thai Dried Fruits & Thai Snacks"
                    ],
                    "Product Details": "The product received may be subject to package modification and quantity from the manufacturer."
                },
                {
                    "Category": "OTOP",
                    "Quantity": "15g",
                    "Product Name": "Sweet Milk Tablets",
                    "Product Images": "https://assets.tops.co.th/LALAFARM-LalafarmSweetMilkTablets15g-8857124514072-1?$JPEG$",
                    "Barcode Number": "8857124514072",
                    "Price": "10 Baht",
                    "Labels": [
                        "Shop by Brands",
                        "I LOVE THAILAND",
                        "Thai Dried Fruits & Thai Snacks"
                    ],
                    "Product Details": "The owner has experience in producing dairy products for various brands in Thailand.He used premium imported full-fat milk powder, making them nutrient-rich snacks just like drinking a whole glass of milk."
                },
                {
                    "Category": "OTOP",
                    "Quantity": "25g",
                    "Product Name": "Doikham Dehydrated Chewy Tasty Mulberry",
                    "Product Images": "https://assets.tops.co.th/DOIKHAM-DoikhamDehydratedChewyTastyMulberry25g-8850773550750-1?$JPEG$",
                    "Barcode Number": "8850773550750",
                    "Price": "25 Baht",
                    "Labels": [
                        "Healthiful",
                        "Alternative Healthy Lifestyle",
                        "Vegan"
                    ],
                    "Product Details": "The product received may be subject to package modification and quantity from the manufacturer."
                }
            ]
 
