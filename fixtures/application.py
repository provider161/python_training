from selenium.webdriver.firefox.webdriver import WebDriver
from fixtures.session import SessionHelper
from fixtures.group import GroupHelper
from fixtures.contact import ContactHelper

class Application:

    def __init__(self):
        self.wd = WebDriver()
        #self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.wd.get("http://localhost:8888/addressbook/index.php")

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_homepage(self):
        wd = self.wd
        wd.get("http://localhost:8888/addressbook/index.php")

    def destroy(self):
        self.wd.quit()