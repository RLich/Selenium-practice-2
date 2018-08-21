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

        wd.find_element_by_name("login").submit()

    def enter_catalog(self):
        wd = self.wd
        box_apps = wd.find_elements_by_xpath("//ul[@id='box-apps-menu']//span[@class='name']")
        for box_app in box_apps:
            if box_app.text == "Catalog":
                box_app.click()
                break

    def add_new_product(self):
        wd = self.wd
        fa_fa_font_buttons = wd.find_elements_by_xpath("//ul[@class='list-inline pull-right']//i[@class='fa fa-plus']")
        for fa_fa_font_button in fa_fa_font_buttons:
            if fa_fa_font_button.text == " Add New Product":
                fa_fa_font_button.click()
                break

    def destroy(self):
        self.wd.quit()