import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.support.wait import WebDriverWait

answer = math.log(int(time.time()-0.7))

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('url', [
"https://stepik.org/lesson/236905/step/1"
])
def test_guest_should_see_login_link(browser, url):
    link = f"{url}"
    browser.get(link)
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.TAG_NAME, "textarea")))
    browser.find_element(By.TAG_NAME, "textarea").send_keys(f'{answer}')
    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
    button.click()
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
    feedback = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text
    assert feedback == "Correct!"
    