import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


def wait_text():
    """
    1. Открыть страницу http://suninjuly.github.io/explicit_wait2.html
    2. Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    3. Нажать на кнопку "Book"
    4. Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
    """

    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    try:
        browser.get(link)

        # wait text
        WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
        book = browser.find_element(By.ID, "book")
        book.click()

        # solve example
        x = int(browser.find_element(By.ID, "input_value").text)
        y = calc(x)

        # input answer into field
        input_field = browser.find_element(By.ID, "answer")
        browser.execute_script("return arguments[0].scrollIntoView(true);", input_field)
        input_field.send_keys(str(y))

        # press submit button
        submit = browser.find_element(By.XPATH, "//button[@id=\"solve\"]")
        submit.click()

    finally:
        time.sleep(5)
        browser.quit()


wait_text()
