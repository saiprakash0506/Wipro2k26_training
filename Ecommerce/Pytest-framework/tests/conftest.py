import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("--browser").lower()
    if browser_name == "chrome":
        opts = webdriver.ChromeOptions()
        opts.add_argument("--incognito")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=opts)
    elif browser_name == "firefox":
        opts = webdriver.FirefoxOptions()
        opts.add_argument("-private")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=opts)
    elif browser_name == "edge":
        opts = webdriver.EdgeOptions()
        opts.add_argument("-inprivate")
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=opts)
    
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture()
def log_in_setup(request):
    driver = request.cls.driver
    driver.get("https://www.saucedemo.com/")
    current_row = request.node.callspec.params.get("test_info")
    driver.find_element(By.ID, "user-name").send_keys(current_row['username'])
    driver.find_element(By.ID, "password").send_keys(current_row['password'])
    driver.find_element(By.ID, "login-button").click()
    time.sleep(1)