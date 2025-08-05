from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.bots.bot_model import Webdriver
from src.bots.bots_entry.bot_per_link import acess_page_link
from src.bots.bots_entry.bot_per_title import acess_page

class Bot(Webdriver):
    def __init__(self, texto):
        self.texto = texto
    
    def define_text(self):
        if "http" in self.texto:
            acess_page_link(self.browser, self.texto)
        else:
            acess_page(self.browser, self.texto)
    
    def get_comments(self):
        comments_section = WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-testid="user-reviews-summary-featured-review-card"]' ))
        )
        for comment in comments_section:
            print(comment.text)
            print()
        
    