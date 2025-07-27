from bot_model import Webdriver
from utils.f_content import get_content

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def acess_page(browser, name):
    browser.get("https://www.imdb.com/pt/")
    try:
        search_bar = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="suggestion-search"]'))
        )
        search_bar.send_keys(name, Keys.ENTER)
    except:
        print("Ocorreu um erro.")