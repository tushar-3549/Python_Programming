from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import time
import os

driver = webdriver.Chrome()
os.makedirs("data", exist_ok=True)
query = "laptop"
file = 0
for i in range(1, 20):
    driver.get(f"https://www.amazon.com/s?k={query}&page={i}&xpid=uW8GwMmN4XoFi&qid=1741152613&ref=sr_pg_2")
    # https://www.amazon.com/s?k=laptop&page=2&xpid=uW8GwMmN4XoFi&qid=1741152613&ref=sr_pg_2

    # elem = driver.find_element(By.CLASS_NAME, "puis-card-container ")
    # print(elem.get_attribute("outerHTML"))
    # print(elem.text)

    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    print("Items founds: ", len(elems))
    for elem in elems:
        # print(elem.text)
        d = elem.get_attribute("outerHTML")
        
        with open(f"data/{query}_{file}.html", "w", encoding="utf-8") as f:
            f.write(d)
            file += 1

    time.sleep(2)
driver.close()


