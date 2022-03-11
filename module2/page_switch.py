from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # нажмем на кнопку
    button = browser.find_element(By.CSS_SELECTOR, ".trollface.btn.btn-primary")
    button.click()
    # узнаем имя новой вкладки и перейдем на нее
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x.text
    print(x)
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
