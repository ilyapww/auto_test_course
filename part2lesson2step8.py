import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import os 

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("first name")    
    
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("last name")   
    
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("e-mail")    
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'text.txt')           # добавляем к этому пути имя файла 
    element = browser.find_element(By.ID, "file")
    element.send_keys(file_path)      
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()   
                       
# не забываем оставить пустую строку в конце файла
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла