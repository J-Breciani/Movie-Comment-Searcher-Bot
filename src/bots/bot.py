from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from bot_model import Webdriver
from utils.f_content import get_content
from bots_entry.bot_per_link import acess_page_link
from bots_entry.bot_per_title import acess_page

browser = Webdriver.criar_webdriver()
list_of_interest = get_content()
for name in list_of_interest:
    if "http" in name:
        acess_page_link(browser, name)
    else: 
        ...
