# https://dummyjson.com/products

import requests
import json
import csv

data = requests.get("https://dummyjson.com/products").text

json_data = json.loads(data)

fields = ['Product Category', 'GST Rate']

category = []

for item in json_data["products"]:
    for key, value in item.items():
        if key == 'category' and value not in category:
            category.append(value)

print(category)

with open("prdinfo.csv", 'r') as csvfile:
    # csvwriter = csv.writer(csvfile)

    # csvwriter.writerow(fields)
    csvFile = csv.reader(csvfile)

    for i in csvFile:
        print(i)
