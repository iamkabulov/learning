from selenium import webdriver
import time 
import math 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By



link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, "num1").text
    y = browser.find_element(By.ID, "num2").text
    z = int(x) + int(y)
    print(z)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(f"{z}") # ищем элемент с текстом "Python"
    
    # def calc(x):
    #      return str(math.log(abs(12*math.sin(int(x)))))
    # x_element = browser.find_element_by_id("treasure")
    # x = x_element.get_attribute("valuex")
    # y = calc(x)
    # input1 = browser.find_element_by_id("answer")
    # input1.send_keys(y)
    # input2 = browser.find_element_by_id("robotCheckbox")
    # input2.click()
    # input3 = browser.find_element_by_id("robotsRule")
    # input3.click()

    

    button = browser.find_element_by_class_name("btn.btn-default")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()


  
