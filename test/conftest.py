import pytest
from selene.support.shared import config
from selene.support.shared import browser
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

from utils import attach


@pytest.fixture
def set_options_in_browser(get_driver_config):
    config.window_width = 1920
    config.window_height = 1080
    config.base_url = 'https://demoqa.com/'
    browser.config.driver = get_driver_config
    yield
    attach.add_screenshot()
    attach.add_html()
    attach.add_logs()
    attach.add_video()

    browser.quit()


@pytest.fixture
def get_driver_config():
    option = Options()
    chrome_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    option.capabilities.update(chrome_capabilities)
    return webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=option)

