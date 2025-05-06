import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "https://suninjuly.github.io/alert_accept.html"

browser = webdriver.Chrome()
browser.get(link)

browser.find_element(By.TAG_NAME, "button").click()
alert = browser.switch_to.alert
alert.accept()
x_element = browser.find_element(By.ID, "input_value")
x = int(x_element.text)
y = calc(x)
answer = browser.find_element(By.ID, "answer")
answer.send_keys(y)
submit_button = browser.find_element(By.TAG_NAME, "button")
submit_button.click()

time.sleep(30)
browser.quit()