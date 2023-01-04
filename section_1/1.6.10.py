from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration1.html"


def required_fields(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        req_fields = browser.find_elements(By.CSS_SELECTOR, "input[required]")
        for field in req_fields:
            field.send_keys("Sample")
            time.sleep(1)
        button = browser.find_element(By.CSS_SELECTOR, ".btn")
        button.click()
        time.sleep(2)
        result = browser.find_element(By.TAG_NAME, "h1").text
        assert result == "Congratulations! You have successfully registered!"

    finally:
        browser.quit()
        time.sleep(5)


def non_required_fields(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        req_fields = browser.find_elements(By.TAG_NAME, "input")
        for field in req_fields[3:]:
            field.send_keys("Sample")
        button = browser.find_element(By.CSS_SELECTOR, ".btn")
        button.click()
        time.sleep(2)
        result = browser.find_element(By.TAG_NAME, "h1").text
        assert result != "Congratulations! You have successfully registered!"

    finally:
        browser.quit()
        time.sleep(5)


def all_fields(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        req_fields = browser.find_elements(By.TAG_NAME, "input")
        for field in req_fields:
            field.send_keys("Sample")
        button = browser.find_element(By.CSS_SELECTOR, ".btn")
        button.click()
        time.sleep(2)
        result = browser.find_element(By.TAG_NAME, "h1").text
        assert result == "Congratulations! You have successfully registered!"

    finally:
        browser.quit()
        time.sleep(5)



print(required_fields(link))