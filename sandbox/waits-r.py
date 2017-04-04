from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome("C:/chromedriver.exe")
#driver.implicitly_wait(30)

#save the url to navigate to in a variable
url = 'http://localhost:63342/PythonSelenium%20Course/Test_Site/test_site.html'

#Navigate to the url
driver.get(url)

my_btn = driver.find_element_by_id('slow_btn')
my_btn.click()

my_mage = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(('id', 'the_slow_image')))
print ('I explicitly waited and I finally found the element')
