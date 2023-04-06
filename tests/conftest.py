import pytest
from selenium import webdriver



def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
@pytest.fixture(scope="class")
def setup(request):

     browser_name = request.config.getoption("browser_name")
     if browser_name == "chrome":
          driver = webdriver.Chrome("C:\\Users\\karthick.k\\PycharmProjects\\pythonProjectnewClass\\Drivers\\chromedriver.exe")

     elif browser_name == "edge":
          driver = webdriver.Edge("C:\\Users\\karthick.k\\PycharmProjects\\pythonProjectnewClass\\Drivers\\msedgedriver.exe")


     driver.implicitly_wait(4)
     driver.get("https://rahulshettyacademy.com/angularpractice/")
     driver.maximize_window()
     request.cls.driver = driver
     yield
     driver.close()