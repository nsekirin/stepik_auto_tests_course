import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "https://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
browser.get(link)

browser.find_element(By.TAG_NAME, "button").click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)
browser.find_element(By.ID, "answer").send_keys(y)
browser.find_element(By.TAG_NAME, "button").click()

print(browser.switch_to.alert.text)
time.sleep(30)


