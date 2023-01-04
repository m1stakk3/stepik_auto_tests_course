import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = "https://suninjuly.github.io/math.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


def click_on_boxes(link):
    """
    1. Открыть страницу https://suninjuly.github.io/math.html.
    2. Считать значение для переменной x.
    3. Посчитать математическую функцию от x (код для этого приведён ниже).
    4. Ввести ответ в текстовое поле.
    5. Отметить checkbox "I'm the robot".
    6. Выбрать radiobutton "Robots rule!".
    7. Нажать на кнопку Submit.
    """
    browser = webdriver.Chrome()
    try:
        browser.get(link)
        x = int(browser.find_element(By.ID, "input_value").text)
        y = calc(x)
        input_field = browser.find_element(By.ID, "answer")
        input_field.send_keys(y)
        checkbox = browser.find_element(By.XPATH, "//*[@id=\"robotCheckbox\"]")
        radiobox = browser.find_element(By.XPATH, "//*[@id=\"robotsRule\"]")
        checkbox.click()
        radiobox.click()
        submit = browser.find_element(By.CSS_SELECTOR, "button")
        submit.click()

    finally:
        time.sleep(5)
        browser.quit()

        
click_on_boxes(link)
