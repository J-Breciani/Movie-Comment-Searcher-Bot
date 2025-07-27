from bot_model import Webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def acess_page_link(browser, link):
    browser.get(link)