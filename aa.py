# THis is for testion and practising 



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.linkedin.com")
driver.implicitly_wait(2)
driver.refresh()
login_email = driver.find_element(By.ID, "session_key")
login_email.send_keys(".@gmail.com")
password_login = driver.find_element(By.ID, "session_password")
password_login.send_keys("password")
password_login.send_keys(Keys.ENTER)
driver.implicitly_wait(2)
search_box = driver.find_element(By.CLASS_NAME, "search-global-typeahead__input")
search_box.send_keys("Internship")
search_box.send_keys(Keys.ENTER)
#jobs hissesine get olunmasi
driver.get("https://www.linkedin.com/jobs/search?keywords=internship&f_AL=true")
#easy apply tapilmasi ve tiklenmesi
driver.implicitly_wait(2)





sleep(30)
