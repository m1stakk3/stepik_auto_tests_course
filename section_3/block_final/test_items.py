from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_different_languages_interfaces(browser):
    # переход по ссылке и ожидание прогрузки элемента
    browser.get(LINK)
    browser.implicitly_wait(5)
    # поиск всех элементов по XPATH, хоть он и является уникальным
    basket = browser.find_elements(By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')
    # проверка на существование объекта, либо вызов исключения
    assert len(basket) > 0, NoSuchElementException()
