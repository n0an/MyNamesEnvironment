from selenium import webdriver
import pdb

driver = webdriver.Chrome("C:/chromedriver.exe")

driver.get('http://www.seleniumhq.org')

# pdb.set_trace()

wd_link = driver.find_element_by_link_text('Selenium WebDriver')
wd_link.click()

pdb.set_trace()
about_selenium_link = driver.find_element_by_link_text('About Selenium')
about_selenium_link.click()

pdb.set_trace()
# if multiple match it will pick the first as always
partial = driver.find_element_by_partial_link_text('Sponsor')
# print partial
partial.click()


pdb.set_trace()
#show it wont find if it is not a link
