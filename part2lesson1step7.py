import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    
    
    treasure = browser.find_element(By.ID, "i")
    treasure_value = treasure.get_attribute("valuex")
       
    x = treasure_value
    y = calc(x) 
    
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y) 

    checkbox1 = browser.find_element(By.ID, "robotCheckbox")
    checkbox1.click()

    radio1 = browser.find_element(By.ID, "robotsRule")
    radio1.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

# не забываем оставить пустую строку в конце файла
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла