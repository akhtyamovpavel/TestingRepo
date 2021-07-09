from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
import time



@pytest.fixture(scope='session')
def chrome_driver():
    options = webdriver.ChromeOptions()
    # options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
    options.add_argument('window-size=800x600')

    driver = webdriver.Chrome(chrome_options=options)
    return driver


def test_loading_main_page(chrome_driver):
    chrome_driver.get('http://localhost:5000/pavel/')

    chrome_driver.save_screenshot('test.png')
    elements = chrome_driver.find_elements(By.CSS_SELECTOR, '#my_name')
    time.sleep(10)
    assert len(elements) == 1
    assert elements[0].text == 'pavel'
