import time
from selenium.webdriver.common.by import By

link = "http://master.tbpm-lrc01.isate.kz/"
def test_check_title(browser):
    browser.get(link)
    title = browser.find_element(By.XPATH, "/html/body/div/div/div[1]/div[1]/div[2]/span").text
    assert title == "TENGRI BPM"