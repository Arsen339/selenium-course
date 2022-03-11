from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # нажмем на кнопку
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()
    # заполним confirm-форму
    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x.text
    answer = calc(x)
    print(answer)
    form = browser.find_element(By.CSS_SELECTOR, "#answer")
    form.send_keys(answer)

    ans_button = browser.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
    ans_button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
