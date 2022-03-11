from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # найдем картинку
    pic = browser.find_element(By.CSS_SELECTOR, "#treasure")
    # получим атрибут
    pic_attribute = pic.get_attribute("valuex")
    # вычислим функцию и запишем в форму
    answer = calc(pic_attribute)
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(answer)
    # отметим checkbox
    box = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    box.click()

    # отметим radiobutton
    radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radiobutton.click()
    # нажмем кнопку
    button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
    button.click()




finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
