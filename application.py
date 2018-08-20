from selenium.webdriver.chrome.webdriver import WebDriver
from Config.cfg_att import Config



class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(1)

    def open_admin_panel_page(self):
        wd = self.wd
        wd.get(Config.admin_panel)

    def login(self, username, password):
        wd = self.wd
        username_box = wd.find_element_by_name
        username_box("username").clear()
        username_box("username").send_keys(username)

        password_box = wd.find_element_by_name
        password_box("password").clear()
        password_box("password").send_keys(password)

    def destroy(self):
        self.wd.quit()