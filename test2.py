from selenium import webdriver
import time 
import unittest


class TestHypc(unittest.TestCase):
 def test_Hypc1(self):
    self = webdriver.Chrome() 
    link = "http://suninjuly.github.io/registration1.html"
    self.get(link)
    input1 = self.find_element_by_xpath("/html/body/div/form/div[1]/div[1]/input")
    input1.send_keys("Ivan")
    input2 = self.find_element_by_xpath("/html/body/div/form/div[1]/div[2]/input")
    input2.send_keys("Petrov")
    input3 = self.find_element_by_xpath("/html/body/div/form/div[1]/div[3]/input")
    input3.send_keys("Smolensk")
    input4 = self.find_element_by_xpath("/html/body/div/form/div[2]/div[1]/input")
    input4.send_keys("Ivan")
    input5 = self.find_element_by_xpath("/html/body/div/form/div[2]/div[2]/input")
    input5.send_keys("Petrov")
    button = self.find_element_by_xpath("/html/body/div/form/button")
    button.click()
    # успеваем скопировать код за 30 секунд
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    self.quit()
 def test_Hypc2(self):
    self = webdriver.Chrome() 
    link = "http://suninjuly.github.io/registration2.html"
    self.get(link)
    input1 = self.find_element_by_xpath("/html/body/div/form/div[1]/div[1]/input")
    input1.send_keys("Ivan")
    input2 = self.find_element_by_xpath("/html/body/div/form/div[1]/div[21]/input")
    input2.send_keys("Petrov")
    input5 = self.find_element_by_xpath("/html/body/div/form/div[2]/div[2]/input")
    input5.send_keys("Petrov")
    button = self.find_element_by_xpath("/html/body/div/form/button")
    button.click()    
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    self.quit()
if __name__=="__main__":
    unittest.main()

  
