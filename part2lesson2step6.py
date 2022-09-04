import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x) 
    
    text_area = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", text_area)
    text_area.send_keys(y) 

    checkbox1 = browser.find_element(By.ID, "robotCheckbox")
    checkbox1.click()

    radio1 = browser.find_element(By.ID, "robotsRule")
    radio1.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
# не забываем оставить пустую строку в конце файла
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла