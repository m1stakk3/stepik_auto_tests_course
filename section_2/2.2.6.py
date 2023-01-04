import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import math

link = "http://suninjuly.github.io/execute_script.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def click_on_boxes(link):
    """
    1. Открыть страницу http://SunInJuly.github.io/execute_script.html.
    2. Считать значение для переменной x.
    3. Посчитать математическую функцию от x.
    4. Проскроллить страницу вниз.
    5. Ввести ответ в текстовое поле.
    6. Выбрать checkbox "I'm the robot".
    7. Переключить radiobutton "Robots rule!".
    8. Нажать на кнопку "Submit".
    """
    browser = webdriver.Chrome()
    try:
        browser.get(link)
        x = int(browser.find_element(By.XPATH, "//*[@id=\"input_value\"]").text)
        print(x)
        assert x is not None, "Вместо числа пустота"
        y = calc(x)
        input_field = browser.find_element(By.ID, "answer")
        input_field.send_keys(y)

        checkbox = browser.find_element(By.XPATH, "//*[@id=\"robotCheckbox\"]")
        browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
        checkbox.click()

        radiobox = browser.find_element(By.XPATH, "//*[@id=\"robotsRule\"]")
        browser.execute_script("return arguments[0].scrollIntoView(true);", radiobox)
        radiobox.click()

        submit = browser.find_element(By.CSS_SELECTOR, ".btn")
        browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
        submit.click()

    finally:
        time.sleep(5)
        browser.quit()


click_on_boxes(link)
