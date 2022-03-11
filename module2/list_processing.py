from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # спарсим номера и посчитаем сумму
    num1 = browser.find_element(By.CSS_SELECTOR, "#num1")
    num1 = num1.text
    num2 = browser.find_element(By.CSS_SELECTOR, "#num2")
    num2 = num2.text
    answer = int(num1) + int(num2)
    answer = str(answer)
    print(answer)
    # выбирем ответ
    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_value(answer)
    # нажмем кнопку
    button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
