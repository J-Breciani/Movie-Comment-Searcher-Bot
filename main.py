from src.utils.f_content import organize_content
from src.bots.bot import Bot
from src.bots.bot_model import Webdriver

browser = Webdriver().criar_webdriver()


movies_list = organize_content()

for item in movies_list:
    run = Bot(item)
    run.define_text()
    run.get_comments(browser)


