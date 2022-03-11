from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 10 секунд, пока цена не станет равна 100
price = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
button = browser.find_element(By.CSS_SELECTOR, "#book")
button.click()

x = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x.text
print(x)
answer = calc(x)
print(answer)
form = browser.find_element(By.CSS_SELECTOR, "#answer")
form.send_keys(answer)

ans_button = browser.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
ans_button.click()