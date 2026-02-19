import pytest
import os
import time
import logging
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Options: chrome, edge, firefox")

@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("--browser").lower()
    current_dir = os.path.dirname(os.path.abspath(__file__)) 
    project_root = os.path.dirname(current_dir) 
    drivers_path = os.path.join(project_root, "drivers")

    driver = None
    if browser == "chrome":
        opts = webdriver.ChromeOptions()
        prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
        opts.add_experimental_option("prefs", prefs)
        opts.add_argument("--disable-features=SafeBrowsingPasswordCheck")
        opts.add_argument("--incognito")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=opts)
    elif browser == "edge":
        exe_path = os.path.join(drivers_path, "msedgedriver.exe")
        opts = webdriver.EdgeOptions()
        opts.add_argument("--inprivate")
        driver = webdriver.Edge(service=EdgeService(exe_path), options=opts)
    elif browser == "firefox":
        exe_path = os.path.join(drivers_path, "geckodriver.exe")
        opts = webdriver.FirefoxOptions()
        opts.add_argument("-private")
        opts.set_preference("browser.tabs.remote.autostart", False)
        opts.set_preference("fission.autostart", False)
        driver = webdriver.Firefox(service=FirefoxService(exe_path), options=opts)

    driver.maximize_window()
    driver.implicitly_wait(10)
    if request.cls is not None:
        request.cls.driver = driver
    
    yield driver
    time.sleep(1)
    driver.quit()

# --- Custom Per-Test Logging Logic ---
@pytest.fixture(scope="function", autouse=True)
def test_logger(request):
    """Creates a separate log file for every test case in reports/logs/"""
    log_dir = "reports/logs"
    os.makedirs(log_dir, exist_ok=True)
    
    # Sanitize test name for filename (remove brackets and special chars)
    test_name = request.node.name.replace("[", "_").replace("]", "_").replace("-", "_")
    log_file = os.path.join(log_dir, f"{test_name}.log")
    
    # Setup logger
    logger = logging.getLogger(test_name)
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(log_file, mode='w')
    formatter = logging.Formatter('%(asctime)s - %(message)s', datefmt='%H:%M:%S')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    # Attach to the test class so the test can use it
    request.cls.logger = logger
    
    yield logger
    
    # Clean up handlers to close the file correctly
    handler.close()
    logger.removeHandler(handler)

# --- Screenshot Logic for HTML Report ---
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' and report.failed:
        driver = getattr(item.instance, 'driver', None)
        if driver:
            os.makedirs("reports/screenshots", exist_ok=True)
            timestamp = datetime.now().strftime("%H%M%S")
            file_name = f"{item.name}_{timestamp}.png".replace("[","_").replace("]","_")
            full_path = os.path.join("reports", "screenshots", file_name)
            driver.save_screenshot(full_path)
            
            if pytest_html:
                relative_path = os.path.join("screenshots", file_name)
                html = '<div><img src="%s" alt="screenshot" style="width:300px;height:200px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % relative_path
                extra.append(pytest_html.extras.html(html))
    report.extra = extra