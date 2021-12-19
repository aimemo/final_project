import pytest
import logging

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from fixtures.pages.application import Application

logger = logging.getLogger("moodle")


# Options repository
def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://berpress.github.io/online-grocery-store/",
        help="Products Shop url"
    ),
    parser.addoption(
        "--headless",
        action="store",
        default="false",
        help="Enter 'True', if you want running tests in headless mode,\n"
             "Enter 'False', if you don't want it"
    )


@pytest.fixture(scope="function")
def app(request):
    url = request.config.getoption("--url")
    headless = request.config.getoption("--headless")
    chrome_options = Options()
    if headless:
        chrome_options.headless = True
    else:
        chrome_options.headless = False
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.set_window_size(1920, 1080)
    logger.info(f"Start app on {url}")
    app = Application(driver, url)
    yield app
    app.quit()
