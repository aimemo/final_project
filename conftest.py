import pytest
# from urllib import request
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from fixtures.pages.application import Application


# Options repository
def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://berpress.github.io/online-grocery-store/",
                     help="Products Shop url")


@pytest.fixture(scope="session")
def app(request):
    url = request.config.getoption("--url")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    app = Application(driver, url)
    yield app
    app.quit()



