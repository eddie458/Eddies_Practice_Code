from bs4 import BeautifulSoup

html_content = """
<div class="product">
  <h1>Awesome Headphones</h1>
  <p class="price">$99.99</p>
  <p class="description">These headphones offer amazing sound quality!</p>
</div>
"""

soup = BeautifulSoup(html_content, 'html.parser')

# Use soup.find() to locate the <h1> tag and store the extracted text in a variable called 'product_name'.
### YOUR CODE HERE ###
product_name = soup.find('h1')

# Use soup.find() to locate <p> tags with class_='price' and store the extracted text in a variable called 'price'.
### YOUR CODE HERE ###
price = soup.find('p')

# Use soup.find() to locate <p> tags with class_='description' and store the extracted text in a variable called 'description'.
### YOUR CODE HERE ###
description = soup.find('p', class_='description')

# Print the extracted data in the format:
print(f"Product name: {product_name.get_text()}")
print(f"Price: {price.get_text()}")
print(f"Description: {description.get_text()}") 