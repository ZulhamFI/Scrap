from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import pandas as pd
import time

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
url = 'https://www.oto.com/mobil-bekas/jabodetabek'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)


# for i in range(2):
#     time.sleep(3)
#     try:
#         driver.find_element(By.CSS_SELECTOR, "a.btn-view-all btn-line btn-more arrow-down").click()
#         time.sleep(3)
#     except NoSuchElementException:
#         break
# time.sleep(3)


driver.save_screenshot("home.png")
products=[]
soup = BeautifulSoup(driver.page_source, "html.parser")
for item in soup.findAll('li',class_="card splide__slide shadow-light filter-listing-card used-car-card"):
    name = item.find('a', class_='vh-name').get_text()
    tipe = item.find('ul', class_='list-bullet t-light d-flex f-12 m-sm-b').get_text()
    # harga = item.find('span', class_='item  push-quarter--ends').get_text()
    products.append(
        (name, tipe)
        )


df = pd.DataFrame(products, columns=['Merk', 'Tipe'])
print(df)
df.to_excel('Mobil.xlsx', index=False)
print('Data berhasil di simpan')
driver.close()

