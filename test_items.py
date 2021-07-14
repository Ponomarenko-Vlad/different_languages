link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_basket_should_be(browser):
    browser.get(link)
    browser.implicitly_wait(10)
    basket_btn = browser.find_element_by_css_selector('#add_to_basket_form .btn')
    assert False, "кнопка добавить в корзину не существует"