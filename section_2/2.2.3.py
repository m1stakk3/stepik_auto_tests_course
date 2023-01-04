import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link1 = "http://suninjuly.github.io/selects1.html"
link2 = "http://suninjuly.github.io/selects2.html"


def dropdown_list(link):
    """
    1. Открыть страницу https://suninjuly.github.io/selects1.html
    2. Посчитать сумму заданных чисел
    3. Выбрать в выпадающем списке значение равное расчитанной сумме
    4. Нажать кнопку "Submit"
    """

    browser = webdriver.Chrome()
    try:
        browser.get(link)

        num1 = browser.find_element(By.ID, "num1").text
        num2 = browser.find_element(By.ID, "num2").text
        summa = int(num1) + int(num2)

        select = Select(browser.find_element(By.ID, "dropdown"))
        select.select_by_value(str(summa))

        submit = browser.find_element(By.CSS_SELECTOR, ".btn")
        submit.click()

        time.sleep(1)
        print("Тест выполнен!")

    finally:
        time.sleep(5)
        browser.quit()


dropdown_list(link2)

