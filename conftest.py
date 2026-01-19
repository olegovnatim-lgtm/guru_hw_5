import pytest
from selenium.webdriver.chrome.options import Options
from selene import browser

@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--window-size=1920,1080')