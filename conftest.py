import pytest
from selenium import webdriver
from data import Url

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Url.main_page)
    yield driver
    driver.quit()
