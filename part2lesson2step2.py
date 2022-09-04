from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.support.ui import Select


try:
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)  

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value("1") # ищем элемент с текстом "Python"

# не забываем оставить пустую строку в конце файла
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла