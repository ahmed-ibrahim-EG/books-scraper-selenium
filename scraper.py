import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://books.toscrape.com/")
driver.maximize_window()
pages=[]
for H in range(5):
    elems=driver.find_elements(By.CLASS_NAME , value ="product_pod")
    for i in elems :
        pages.append(i.text)
    time.sleep(2)
    if H<4:
        driver.find_element(By.CSS_SELECTOR , value ="#default > div > div > div > div > section > div:nth-child(2) > div > ul > li.next > a").click()

driver.close()
j=0
time.sleep(3)

for i  in pages:
    pages[j]=i.split("\n")
    pages[j].remove("Add to basket")
    pages[j][1]=pages[j][1].replace("£","")
    pages[j][1] = float(pages[j][1].replace("£", ""))
    j+=1

data = pd.DataFrame(pages , columns=["Book","price", "status"])
data.to_csv("your path here/books.csv")
print("Done saving")
print(f"Head{data.head()}")