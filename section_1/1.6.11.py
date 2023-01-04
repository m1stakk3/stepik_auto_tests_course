from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()


try:
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
    assert "Congratulations! You have successfully registered!" == result

except NoSuchElementException:
    print("Game over!")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
