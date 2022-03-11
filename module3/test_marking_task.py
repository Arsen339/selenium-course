import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By

links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"

]


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

# выполнение через параметры. число запусков = числу параметров
@pytest.mark.parametrize('site_link', links)
def test_guest_should_see_login_link(browser, site_link):
    browser.implicitly_wait(5)
    answer = math.log(int(time.time()))
    answer = str(answer)
    link = f"{site_link}"
    browser.get(link)
    answer_field = browser.find_element(By.CSS_SELECTOR, ".ember-text-area")
    answer_field.send_keys(answer)
    button = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
    button.click()
    feedback = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint")
    assert "Correct!" == feedback.text
