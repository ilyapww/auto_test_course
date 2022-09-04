from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.support.ui import Select


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)  
     
    value1 = browser.find_element(By.ID, "num1")
    value2 = browser.find_element(By.ID, "num2")
       
    x = value1.text
    y = value2.text
    z = str(int(x) + int(y))
    
    select = Select(browser.find_element(By.CSS_SELECTOR, ".custom-select"))
    select.select_by_value(z)
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
# не забываем оставить пустую строку в конце файла
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла