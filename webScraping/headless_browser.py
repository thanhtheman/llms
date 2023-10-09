
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

url1="https://the-internet.herokuapp.com/login"
url2="https://the-internet.herokuapp.com/dynamic_loading/2"

driver.get(url2)
# driver.find_element(By.XPATH, '//*[@id="username"]').send_keys("tomsmith")
# driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("SuperSecretPassword!")
# driver.find_element(By.XPATH, '//*[@id="login"]/button').click()
driver.find_element(By.XPATH, '//*[@id="start"]/button').click()
driver.implicitly_wait(6)
text = driver.find_element(By.XPATH, '//*[@id="finish"]/h4').text
print(text)