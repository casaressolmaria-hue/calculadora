from selenium import webdriver 
import time  

driver = webdriver.Chrome()

try:
    driver.get('https://www.saucedemo.com')  
    
    print('Título:', driver.title) 
    assert driver.title == 'Swaq Labs' 
    
    time.sleep(2) 
finally:
    driver.quit() 