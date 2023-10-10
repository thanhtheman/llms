
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

url1="https://www.zolo.ca/"
url2="https://the-internet.herokuapp.com/dynamic_loading/2"


data = []

# driver.get(url1)

# profiles = driver.find_elements(By.CSS_SELECTOR, 'article.card-listing')

# def run_loops(profiles):
#     for count, profile in enumerate(profiles, start=1):
#         try:
#             price = profile.find_element(By.XPATH, f'//*[@id="gallery"]/div/article[{count}]/div[1]/ul/li[1]/span[2]').text
#         except:
#             price = "N/A"
#         bed = profile.find_element(By.XPATH, f'//*[@id="gallery"]/div/article[{count}]/div[1]/ul/li[2]').text
#         bath = profile.find_element(By.XPATH, f'//*[@id="gallery"]/div/article[{count}]/div[1]/ul/li[3]').text
#         try:
#             area = profile.find_element(By.XPATH, f'//*[@id="gallery"]/div/article[{count}]/div[1]/ul/li[4]').text
#         except:
#             area = "N/A"
#         street = profile.find_element(By.XPATH, f'//*[@id="gallery"]/div/article[{count}]/div[1]/div[1]/a/h3/span[1]').text
#         city = profile.find_element(By.XPATH, f'//*[@id="gallery"]/div/article[{count}]/div[1]/div[1]/a/h3/span[2]').text
#         province = profile.find_element(By.XPATH, f'//*[@id="gallery"]/div/article[{count}]/div[1]/div[1]/a/h3/span[3]').text
#         data.append({"address": f"{street} {city} {province}","price":price,"bed":bed,"bath":bath,"area":area}) 
# driver.close()



for page_number in range(1,10):
    driver.get(f"https://www.zolo.ca/toronto-real-estate/page-{page_number}")
    profiles = driver.find_elements(By.CSS_SELECTOR, 'article.card-listing')
    for count, profile in enumerate(profiles, start=1):
        try:
            price = profile.find_element(By.XPATH, f'//*[@id="gallery"]/div/article[{count}]/div[1]/ul/li[1]/span[2]').text
        except:
            price = "N/A"
        bed = profile.find_element(By.XPATH, f'//*[@id="gallery"]/div/article[{count}]/div[1]/ul/li[2]').text
        bath = profile.find_element(By.XPATH, f'//*[@id="gallery"]/div/article[{count}]/div[1]/ul/li[3]').text
        try:
            area = profile.find_element(By.XPATH, f'//*[@id="gallery"]/div/article[{count}]/div[1]/ul/li[4]').text
        except:
            area = "N/A"
        street = profile.find_element(By.XPATH, f'//*[@id="gallery"]/div/article[{count}]/div[1]/div[1]/a/h3/span[1]').text
        city = profile.find_element(By.XPATH, f'//*[@id="gallery"]/div/article[{count}]/div[1]/div[1]/a/h3/span[2]').text
        province = profile.find_element(By.XPATH, f'//*[@id="gallery"]/div/article[{count}]/div[1]/div[1]/a/h3/span[3]').text
        data.append({"address": f"{street} {city} {province}","price":price,"bed":bed,"bath":bath,"area":area})
    driver.implicitly_wait(6) 
driver.close()


with open("data.json","w") as f:
    json.dump(data,f)




# driver.find_element(By.XPATH, '//*[@id="login"]/button').click()
# driver.find_element(By.XPATH, '//*[@id="start"]/button').click()
# driver.implicitly_wait(6)
# text = driver.find_element(By.XPATH, '//*[@id="finish"]/h4').text
