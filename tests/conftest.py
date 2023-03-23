import os
import pytest
from dotenv import load_dotenv
from selene.support.shared import browser
from utils.base_session import BaseSession
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
load_dotenv()


@pytest.fixture(scope='session')
def demoshop():
    return BaseSession(os.getenv("API_URL"))


@pytest.fixture(scope='session')
def app(demoshop):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }
    options.capabilities.update(selenoid_capabilities)
    login = os.getenv('LOGIN_SELENOID')
    password = os.getenv('PASSWORD_SELENOID')
    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options)
    browser.config.driver = driver
    browser.config.base_url = (os.getenv("API_URL"))
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    response = demoshop.post(
        "login", json={"Email": os.getenv("LOGIN"), "Password": os.getenv("PASSWORD")}, allow_redirects=False)
    authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")
    browser.open("Themes/DefaultClean/Content/images/logo.png")
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": authorization_cookie})
    return browser


@pytest.fixture(scope='session')
def reqres():
    return BaseSession(os.getenv("REQ_URL"))
