from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
import time

driver = webdriver.PhantomJS("F:\\Programming\\phantomjs\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")

driver.get("https://www.olx.ua/obyavlenie/lampa-razryadnaya-metallogalogennaya-driz-700-IDeRlW2.html")
driver.find_element_by_class_name('spoiler').click()
time.sleep(0.5)
print (driver.current_url)
driver.save_screnshot('screenshot.png')

driver.quit()





