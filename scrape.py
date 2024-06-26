from bs4 import BeautifulSoup
import csv

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all relevant div elements
divs = soup.find_all('div', class_='sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 AdHolder sg-col s-widget-spacing-small sg-col-4-of-20 gsx-ies-anchor')

# Initialize the list to hold the extracted data
data = []

# Extract data from each div
for div in divs:
    item = {}
    
    # Extract image link
    img = div.find('img', class_='s-image s-image-optimized-rendering')
    item['link'] = img['src'] if img else ''
    
    # Extract title
    title_span = div.find('span', class_='a-size-base-plus a-color-base a-text-normal')
    item['title'] = title_span.text.strip() if title_span else ''
    
    # Extract rating
    rating_span = div.find('span', class_='a-icon-alt')
    item['rating'] = rating_span.text.strip() if rating_span else ''
    
    # Extract number of ratings
    no_ratings_span = div.find('span', class_='a-size-base s-underline-text')
    item['no_ratings'] = no_ratings_span.text.strip() if no_ratings_span else ''
    
    # Extract cover type
    cover_type_a = div.find('a', class_='a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-bold')
    item['cover_type'] = cover_type_a.text.strip() if cover_type_a else ''
    
    # Extract price
    price_span = div.find('span', class_='a-offscreen')
    item['price'] = price_span.text.strip() if price_span else ''
    
    data.append(item)

# Write the data to a JSON file
# with open('data.json', 'w', encoding='utf-8') as json_file:
#     json.dump(data, json_file, ensure_ascii=False, indent=4)

# print(json.dumps(data, indent=4))

# Define the CSV file columns
csv_columns = ['link', 'title', 'rating', 'no_ratings', 'cover_type', 'price']

# Write the data to a CSV file
csv_file = 'data.csv'
try:
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for item in data:
            writer.writerow(item)
except IOError:
    print("I/O error")

# Print the location of the CSV file
print(f"Data has been written to {csv_file}")
