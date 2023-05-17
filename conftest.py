import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def pytest_addoption(parser):
    parser.addoption(
        '--browser_name', action='store', default='chrome', help='default in chrome'
    )



@pytest.fixture(scope='class')
def invoke(request):
    global Driver
    browsername = request.config.getoption("browser_name")
    if browsername == 'chrome':
        ser = Service('C:\\Users\\DELL\\Desktop\\Driver\\chromedriver.exe')
        Driver = webdriver.Chrome(service=ser)
        Driver.maximize_window()
        Driver.get("https://www.youtube.com")
        request.cls.Driver = Driver
    else:
        pass
    # yield
    # Driver.close()





