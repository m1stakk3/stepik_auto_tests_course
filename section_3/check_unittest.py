import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestFineElement(unittest.TestCase):
    """
    1. Возьмите тесты из шага — https://stepik.org/lesson/138920/step/11?unit=196194
    2. Создайте новый файл
    3. Создайте в нем класс с тестами, который должен наследоваться от unittest. TestCase по аналогии с предыдущим шагом
    4. Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
    5. Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
    6. Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
    7. Запустите получившиеся тесты из файла
    8. Просмотрите отчёт о запуске и найдите последнюю строчку
    9. Отправьте эту строчку в качестве ответа на это задание
    """

    def test_fine_element_first(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input")
        last_name = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input")
        email = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input")
        req_fields = [first_name, last_name, email]
        for field in req_fields:
            field.send_keys("Sample")
        button = browser.find_element(By.CSS_SELECTOR, ".btn")
        button.click()
        result = browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual("Congratulations! You have successfully registered!",
                         result,
                         "Полученное сообщение не найдено")

    def test_fine_element_second(self):
        time.sleep(5)
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input")
        last_name = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input")
        email = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input")
        req_fields = [first_name, last_name, email]
        for field in req_fields:
            field.send_keys("Sample")
        button = browser.find_element(By.CSS_SELECTOR, ".btn")
        button.click()
        result = browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual("Congratulations! You have successfully registered!",
                         result,
                         "Полученное сообщение не найдено")


if __name__ == "__main__":
    unittest.main()
