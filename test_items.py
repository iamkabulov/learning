import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_search_button_basket(browser):
    browser.get(link)
    time.sleep(1) #Для визуальной проверки языка изменить на 30
    x = len(browser.find_elements_by_css_selector(".btn-add-to-basket"))
    assert x > 0, 'Button Basket not find'