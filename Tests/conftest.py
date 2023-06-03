import pytest

from selenium import webdriver
from Config.config import TestData
from selenium.webdriver.chrome.service import Service

@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        s = Service(TestData.CHROME_EXECUTABLE_PATH)
        web_driver = webdriver.Chrome(service=s)
        #web_driver.maximize_window()
        web_driver.set_window_size(1920,1200)
    if request.param == "safari":
        web_driver = webdriver.Safari()
        web_driver.maximize_window()
    request.cls.driver = web_driver
    yield
    web_driver.quit()