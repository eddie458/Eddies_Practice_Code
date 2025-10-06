# Step 3.1: Fetch HTML Content
# Please be careful to follow instructions on how to run the program; 
# the Run menu or right-click > Run options do not work in the simulated environment. 
# Ensure you have run the terminal command to install the correct libraries using pip.
# You must use the terminal window as directed in Step 3.

import requests
from bs4 import BeautifulSoup

# Fetch the webpage content
url = "http://127.0.0.1:5500/baseball_stats.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Print the HTML content to inspect
# print(soup.prettify())

# Step 3.2: Extract the Required Data

all_table_headers = soup.find_all('th')
all_table_rows = soup.find_all('td')

num_headers = len(all_table_headers)
num_rows = int(len(all_table_rows) / len(all_table_headers))

dict_keys = []
for table_hearder in all_table_headers:
    dict_keys.append(table_hearder.get_text())
# print(dict_keys)

dict_values = []
dict_values_temp = []
value_iteration = 0
for table_row in all_table_rows:
    if (value_iteration / num_headers) != 1:
        value_iteration += 1
        dict_values_temp.append(table_row.get_text())
    if (value_iteration / num_headers) == 1:
        value_iteration = 0
        dict_values.append(dict_values_temp.copy())
        dict_values_temp.clear()
# print(dict_values)    

values_dictionary_temp = {}
list_values_dictionary = []
for j in range(num_rows):
    for i in range(num_headers):
        values_dictionary_temp[dict_keys[i]] = dict_values[j][i]
    list_values_dictionary.append(values_dictionary_temp.copy())
    values_dictionary_temp.clear()
# print(list_values_dictionary)

# Step 4.1: Convert to a DataFrame

import pandas as pd

pandas_values_dictionary = {}
pre_dictionary_list = []
for k in range(num_headers):
    for l in range(num_rows):
        pre_dictionary_list.append(list_values_dictionary[l][dict_keys[k]])
    pandas_values_dictionary[dict_keys[k]] = pre_dictionary_list.copy()
    pre_dictionary_list.clear()
# print(pandas_values_dictionary)

# Convert the game data into a pandas DataFrame
# Inspect the DataFrame
# Save and print the shaped data

df = pd.DataFrame(pandas_values_dictionary)
print(df)

# Step 5.1: Save to a CSV File
# Save the DataFrame to a CSV file named sports_statistics.csv

df.to_csv('sports_statistics.csv', index=False)