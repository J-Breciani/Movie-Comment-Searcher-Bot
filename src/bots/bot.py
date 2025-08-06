from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.bots.bot_model import Webdriver
from src.bots.bots_entry.bot_per_link import acess_page_link
from src.bots.bots_entry.bot_per_title import acess_page

class Bot(Webdriver):
    def __init__(self, texto, browser='chrome', headless=False):
        super().__init__(browser, headless)  # Chama o __init__ de Webdriver
        self.texto = texto
        self.driver = self.criar_webdriver()

    def click_on_movie(self):
        movie_list = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.ipc-metadata-list.ipc-metadata-list--dividers-after.sc-bf2a2581-3.cxxcAH.ipc-metadata-list--base'))
        )
        movie_list.find_element(By.TAG_NAME, 'li').click()
    
    def define_text(self):
        if "http" in self.texto:
            acess_page_link(self.driver, self.texto)
        else:
            acess_page(self.driver, self.texto)
            self.click_on_movie()
    
    
    def get_comments(self):
        comments_section = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-testid="user-reviews-summary-featured-review-card"]' ))
        )
        for comment in comments_section:
            print(comment.text)
            print()
        
    