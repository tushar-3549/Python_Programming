import os
from bs4 import BeautifulSoup
import pandas as pd

d = {'title': [], 'price': [], 'link': []}
for file in os.listdir("data"):
    with open(f"data/{file}", encoding="utf-8") as f: 
        html_doc = f.read()

    soup = BeautifulSoup(html_doc, "html.parser")  
    # print(soup.prettify())
    t = soup.find("h2")
    title = t.get_text()
    print(title)
    l = soup.find("a", class_="a-link-normal")
    link = "https://amazon.in/" + l['href']
    print(link)
    p = soup.find("span", attrs={"class": "a-price-whole"})
    price = p.get_text() if p else "Price not found"
    print(price)
    d['title'].append(title)
    d['price'].append(price)
    d['link'].append(link)

df = pd.DataFrame(data=d)
df.to_csv("data.csv")
print("OK...")