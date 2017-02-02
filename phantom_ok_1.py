from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
import time

driver = webdriver.PhantomJS("F:\\Programming\\phantomjs\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")

driver.get("https://www.olx.ua/nedvizhimost/dnepr/")
driver.find_element_by_xpath('//a[@href="https://www.olx.ua/nedvizhimost/dnepr/?search%5Bpaidads_listing%5D=1"]').click()
# driver.find_element_by_id("fZl").click()
print (driver.current_url)
driver.save_screenshot('screenshot.png')

driver.quit()





