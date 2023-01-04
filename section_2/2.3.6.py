import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


def accept_alert():
    """
    1. Открыть страницу http://suninjuly.github.io/redirect_accept.html
    2. Нажать на кнопку
    3. Переключиться на новую вкладку
    4. Пройти капчу для робота и получить число-ответ
    """

    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    try:
        browser.get(link)

        # first page actions
        button = browser.find_element(By.CLASS_NAME, "trollface")
        button.click()

        # list of windows
        windows = browser.window_handles
        # select 2 window to switch
        browser.switch_to.window(windows[1])

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
