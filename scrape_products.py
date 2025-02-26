import requests
from bs4 import BeautifulSoup
import pprint
import json
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

url = 'https://www.tops.co.th/en'
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')
rows = soup.select('div.item')

from re import split
links = {}
n = len(rows)
OTOP_link = (rows[0].select_one('a')['href'])
links['Only At Tops'] = (rows[1].select_one('a')['href'])
categories = ['OTOP', 'Only At Tops', 'Fruits & Vegetables', 'Meat & Seafood', 'Fresh Food & Bakery', 'Pantry & Ingredients', 'Snacks & Desserts', 'Beverages', 'Health & Beauty Care', 'Mom & Kids', 'Household & Merit', 'PetNme']

for i in range(2,n):
  link = (rows[i].select_one('a')['href']).split("/")
  links[categories[i]] = (url + '/' + link[2])

# pprint.pprint(links)

def get_product_description(product_url):
  head = {'User-Agent': "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}
  product_response = requests.get(product_url, headers=head)
  product_soup = BeautifulSoup(product_response.content, 'html.parser')
  product_description = product_soup.select_one('div.accordion-property span.text p')
  if product_description:
    return product_description.text

  return ''


def get_category_links(link_url):
  chrome_options = Options()
  chrome_options.add_argument("--incognito")  # Enable incognito mode
  chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
  chrome_options.add_argument("--no-sandbox")  # Required for Colab
  chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource issues
  chrome_options.add_argument("/tmp/chrome-profile-1")  # Unique directory
  driver = webdriver.Chrome(service=Service(), options=chrome_options)

  driver.get(link_url)

  html_content = driver.page_source
  soup_content = BeautifulSoup(html_content, 'html.parser')
  link_categories = soup_content.select('div.plp-carousels div.plp-carousel__title')
  category_links = []

  for l in link_categories:
    category_links.append(l.select_one('a')['href'])

  driver.quit()

  return category_links



def get_products_data(category_link_list, product_data):
  for category_link in category_link_list:
    chrome_options = Options()
    chrome_options.add_argument("--incognito")  # Enable incognito mode
    chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
    chrome_options.add_argument("--no-sandbox")  # Required for Colab
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource issues
    chrome_options.add_argument("/tmp/chrome-profile-1")  # Unique directory
    driver = webdriver.Chrome(service=Service(), options=chrome_options)
    driver.get(category_link)

    content = driver.page_source
    soup_category = BeautifulSoup(content, 'html.parser')

    data = soup_category.select('div.hits ol li article')
    product_data.append(data)

  return product_data




def get_product_details_OTOP(product_data, product_details, SKU):
  for data in product_data:
    if data:
      for d in data:
        sku_data = d.get('data-product-id')
        if sku_data not in SKU:
          SKU.append(sku_data)
          product = {}
          product['Category'] = 'OTOP'

          name = d.get('data-product-name')
          if '.' in name:
            remove_dot = name.split('.')
            split_name = remove_dot[0].split()
          else:
            split_name = name.split()

          split_name = split_name[1:]

          new_name = ''

          product['Quantity'] = ''
          for s in split_name:
            if ('mg' in s) or ('ml' in s) or ('L' in s) or ('kg' in s) or ('g' in s):
              product['Quantity'] = s
            else:
              new_name += s + " "

          product['Product Name'] = new_name.strip()

          product['Product Images'] = d.get('data-product-image-url')

          product['Barcode Number'] = sku_data
          product['Price'] = d.get('data-product-price') + " Baht"
          product['Labels'] = d.get('data-product-categories').split(' /// ')
          product_link = d.get('data-product-url')
          product['Product Details'] = ''
          product['Product Details'] = get_product_description(product_link)

          product_details.append(product)


  return product_details




def get_product_details(product_data, product_details, SKU, category):
  for data in product_data:
    if data:
      for d in data:
        sku_data = d.get('data-product-id')
        if sku_data not in SKU:
          SKU.append(sku_data)
          product = {}
          product['Category'] = category

          name = d.get('data-product-name')
          if '.' in name:
            remove_dot = name.split('.')
            split_name = remove_dot[0].split()
          else:
            split_name = name.split()

          new_name = ''

          product['Quantity'] = ''
          for s in split_name:
            if ('mg' in s) or ('ml' in s) or ('L' in s) or ('kg' in s) or ('g' in s):
              product['Quantity'] = s
            else:
              new_name += s + " "

          product['Product Name'] = new_name.strip()

          product['Product Images'] = d.get('data-product-image-url')

          product['Barcode Number'] = sku_data
          product['Price'] = d.get('data-product-price') + " Baht"
          product['Labels'] = d.get('data-product-categories').split(' /// ')
          product_link = d.get('data-product-url')
          product['Product Details'] = ''
          product['Product Details'] = get_product_description(product_link)

          product_details.append(product)


  return product_details


SKU = []
product_details = []

# Get product details of Category='OTOP'
link_categories = get_category_links(OTOP_link)
data_products = get_products_data(link_categories, [])
product_details = get_product_details_OTOP(data_products, [], SKU)

with open("product_data_OTOP.json","w") as json_file:
  json.dump(product_details, json_file, indent=4)

# Get product details of Category='Only At Tops'
link_categories = get_category_links(links['Only At Tops'])
data_products = get_products_data(link_categories, [])
product_details = get_product_details(data_products, [], SKU, 'Only At Tops')

with open("product_data_OnlyAtTops.json","w") as json_file:
  json.dump(product_details, json_file, indent=4)

# Get product details of Category='Fruits & Vegetables'
link_categories = get_category_links(links['Fruits & Vegetables'])
data_products = get_products_data(link_categories, [])
product_details = get_product_details(data_products, [], SKU, 'Fruits & Vegetables')

with open("product_data_FruitsVegetables.json","w") as json_file:
  json.dump(product_details, json_file, indent=4)

# Get product details of Category='Meat & Seafood'
link_categories = get_category_links(links['Meat & Seafood'])
data_products = get_products_data(link_categories, [])
product_details = get_product_details(data_products, [], SKU, 'Meat & Seafood')

with open("product_data_MeatSeafood.json","w") as json_file:
  json.dump(product_details, json_file, indent=4)

# Get product details of Category='Fresh Food & Bakery'
link_categories = get_category_links(links['Fresh Food & Bakery'])
data_products = get_products_data(link_categories, [])
product_details = get_product_details(data_products, [], SKU, 'Fresh Food & Bakery')

with open("product_data_FreshFoodBakery.json","w") as json_file:
  json.dump(product_details, json_file, indent=4)

# Get product details of Category='Pantry & Ingredients'
link_categories = get_category_links(links['Pantry & Ingredients'])
data_products = get_products_data(link_categories, [])
product_details = get_product_details(data_products, [], SKU, 'Pantry & Ingredients')

with open("product_data_PantryIngredients.json","w") as json_file:
  json.dump(product_details, json_file, indent=4)

# Get product details of Category='Snacks & Desserts'
link_categories = get_category_links(links['Snacks & Desserts'])
data_products = get_products_data(link_categories, [])
product_details = get_product_details(data_products, [], SKU, 'Snacks & Desserts')

with open("product_data_SnacksDesserts.json","w") as json_file:
  json.dump(product_details, json_file, indent=4)

# Get product details of Category='Beverages'
link_categories = get_category_links(links['Beverages'])
data_products = get_products_data(link_categories, [])
product_details = get_product_details(data_products, [], SKU, 'Beverages')

with open("product_data_Beverages.json","w") as json_file:
  json.dump(product_details, json_file, indent=4)

# Get product details of Category='Health & Beauty Care'
link_categories = get_category_links(links['Health & Beauty Care'])
data_products = get_products_data(link_categories, [])
product_details = get_product_details(data_products, [], SKU, 'Health & Beauty Care')

with open("product_data_HealthBeautyCare.json","w") as json_file:
  json.dump(product_details, json_file, indent=4)

# Get product details of Category='Mom & Kids'
link_categories = get_category_links(links['Mom & Kids'])
data_products = get_products_data(link_categories, [])
product_details = get_product_details(data_products, [], SKU, 'Mom & Kids')

with open("product_data_MomKids.json","w") as json_file:
  json.dump(product_details, json_file, indent=4)

# Get product details of Category='Household & Merit'
link_categories = get_category_links(links['Household & Merit'])
data_products = get_products_data(link_categories, [])
product_details = get_product_details(data_products, [], SKU, 'Household & Merit')

with open("product_data_HouseholdMerit.json","w") as json_file:
  json.dump(product_details, json_file, indent=4)

# Get product details of Category='PetNme'
link_categories = get_category_links(links['PetNme'])
data_products = get_products_data(link_categories, [])
product_details = get_product_details(data_products, [], SKU, 'PetNme')

with open("product_data_PetNme.json","w") as json_file:
  json.dump(product_details, json_file, indent=4)

def combine_jsons():
  file_list = ['product_data_OTOP.json', 'product_data_OnlyAtTops.json', 'product_data_FruitsVegetables.json', 'product_data_MeatSeafood.json', 'product_data_FreshFoodBakery.json', 'product_data_PantryIngredients.json', 'product_data_SnacksDesserts.json', 'product_data_Beverages.json', 'product_data_HealthBeautyCare.json', 'product_data_MomKids.json', 'product_data_HouseholdMerit.json', 'product_data_PetNme.json']

  combined_data = []

  for file_name in file_list:
        try:
            with open(file_name, "r") as json_file:
                file_data = json.load(json_file)  # Load JSON data from the file
                combined_data.extend(file_data)  # Add all items to the combined list
        except Exception as e:
            print(f"Error reading {file_name}: {e}")

    # Write the combined data to the output file
        with open("product_data.json", "w") as res_file:
            json.dump(combined_data, res_file, indent=4)

combine_jsons()
