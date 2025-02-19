import requests
from bs4 import BeautifulSoup
import csv 

# url = "https://www.geeksforgeeks.org/popular-programming-languages/"
url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
#  Website er title print korbe
#print(soup.title.text)  

# Webpage er sob link extract kora
# for link in soup.find_all("a"):
#     print(link..get("href"))

# ekta specific class er sob element extract kora ; ".classname" hocche CSS class
# elements = soup.select(".header-main__slider")  
# for element in elements:
#     print(element.text)
    
data = [["Title", "URL"]]

for book in soup.find_all("article", class_="product_pod"):
    title = book.h3.a['title']
    book_url = "http://books.toscrape.com/" + book.h3.a["href"]
    
    data.append([title, book_url])
    
# for i in data:
#     print(i)
with open('answer_books.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(data)
    
print("OK")
    
    
    
    
    
    
    
    
    
    
    
