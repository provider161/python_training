from selenium.webdriver.firefox.webdriver import WebDriver
from fixtures.session import SessionHelper
from fixtures.group import GroupHelper

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_homepage(self):
        wd = self.wd
        wd.get("http://localhost:8888/addressbook/index.php")

    def destroy(self):
        self.wd.quit()
