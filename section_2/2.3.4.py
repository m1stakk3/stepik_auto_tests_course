import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


def accept_alert():
    """
    1. Открыть страницу http://suninjuly.github.io/alert_accept.html
    2. Нажать на кнопку
    3. Принять confirm
    4. На новой странице решить капчу для роботов, чтобы получить число с ответом
    """

    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    try:
        browser.get(link)

        # first page actions
        button = browser.find_element(By.TAG_NAME, "button")
        button.click()
        alert = browser.switch_to.alert
        alert.accept()

        # second page actions
        x = int(browser.find_element(By.ID, "input_value").text)
        input_field = browser.find_element(By.ID, "answer")
        submit = browser.find_element(By.XPATH, "//button")

        y = calc(x)
        input_field.send_keys(y)
        submit.click()

    finally:
        time.sleep(5)
        browser.quit()


accept_alert()
