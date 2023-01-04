import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = "http://suninjuly.github.io/get_attribute.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def click_on_boxes(link):
    """
    1. Открыть страницу http://suninjuly.github.io/get_attribute.html.
    2. Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
    3. Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
    4. Посчитать математическую функцию от x (сама функция остаётся неизменной).
    5. Ввести ответ в текстовое поле.
    6. Отметить checkbox "I'm the robot".
    7. Выбрать radiobutton "Robots rule!".
    8. Нажать на кнопку "Submit".
    """
    browser = webdriver.Chrome()
    try:
        browser.get(link)
        x = browser.find_element(By.XPATH, "//*[@id=\"treasure\"]")
        x = int(x.get_attribute("valuex"))
        assert x is not None, "Вместо числа пустота"
        y = calc(x)
        input_field = browser.find_element(By.ID, "answer")
        input_field.send_keys(y)
        checkbox = browser.find_element(By.XPATH, "//*[@id=\"robotCheckbox\"]")
        radiobox = browser.find_element(By.XPATH, "//*[@id=\"robotsRule\"]")
        checkbox.click()
        radiobox.click()
        submit = browser.find_element(By.XPATH, "/html/body/div/form/div/div/button")
        submit.click()
        print("Тест успешно завершен!")

    finally:
        time.sleep(5)
        browser.quit()


click_on_boxes(link)
