from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://www.imdb.com/pt/title/tt5950044/?ref_=nv_srb_trend_title_2')
def get_comments(browser):
        comments_section = WebDriverWait(browser, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-testid="user-reviews-summary-featured-review-card"]')))
        for comment in comments_section:
            print(comment.text)
            print()
get_comments(browser)