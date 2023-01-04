import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By


def load_file():
    """
    1. Открыть страницу http://suninjuly.github.io/file_input.html
    2. Заполнить текстовые поля: имя, фамилия, email
    3. Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    4. Нажать кнопку "Submit"
    """

    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "empty.txt")

    try:
        browser.get(link)

        # константы из переменных, к котором в дальнейшем буду обращаться
        firstname = browser.find_element(By.XPATH, "//input[@name=\"firstname\"]")
        lastname = browser.find_element(By.XPATH, "//input[@name=\"lastname\"]")
        email = browser.find_element(By.XPATH, "//input[@name=\"email\"]")
        file = browser.find_element(By.ID, "file")
        submit = browser.find_element(By.CSS_SELECTOR, ".btn")

        # ввод данных в поля
        for _ in [firstname, lastname, email]:
            _.send_keys("Sample")
        file.send_keys(file_path)
        submit.click()

        # завершение теста
        time.sleep(1)
        print("Тест завершен.")

    finally:
        time.sleep(5)
        browser.quit()


load_file()
