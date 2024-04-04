from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import pandas as pd
import time

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
url = 'https://www.olx.co.id/mobil-bekas_c198'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)


for i in range(20):
    time.sleep(3)
    try:
        driver.find_element(By.CSS_SELECTOR, "div._38O09 > button").click()
        time.sleep(3)
    except NoSuchElementException:
        break
time.sleep(3)


driver.save_screenshot("home.png")
products=[]
soup = BeautifulSoup(driver.page_source, "html.parser")
for item in soup.findAll('div',class_="_2v8Tq"):
    name = item.find('div', class_='_2Gr10').get_text()
    tahun = item.find('div', class_='_21gnE').get_text()
    harga = item.find('span', class_='_1zgtX').get_text()
    products.append(
        (name, tahun, harga)
        )


df = pd.DataFrame(products, columns=['Merk', 'Tahun', 'Harga'])
print(df)
df.to_excel('Mobil.xlsx', index=False)
print('Data berhasil di simpan')
driver.close()

