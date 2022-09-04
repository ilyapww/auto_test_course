import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 


try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)    
    
        
    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print("value of people radio: ", robots_checked)
    assert robots_checked is None    

# не забываем оставить пустую строку в конце файла
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла