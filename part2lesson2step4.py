from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.support.ui import Select
from selenium import webdriver

try:
    browser = webdriver.Chrome()
    browser.execute_script("document.title='Script executing';alert('Robots at work');")

# не забываем оставить пустую строку в конце файла
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла