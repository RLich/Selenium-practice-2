from selenium.webdriver.chrome.webdriver import WebDriver
from Config.cfg_att import Config
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import random
import string

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

    def waiter(self, wd):
        wd = self.wd
        wait = WebDriverWait(wd, 10)
        return wait

    def enter_catalog(self):
        wd = self.wd
        wait = self.waiter(wd)
        xpath = "//ul[@id='box-apps-menu']//span[@class='name']"
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath)))
        box_apps = wd.find_elements_by_xpath(xpath)
        for box_app in box_apps:
            if box_app.text == "Catalog":
                box_app.click()
                break

    def add_new_product(self):
        wd = self.wd
        wd.find_elements_by_xpath(("//ul[@class='list-inline pull-right']//a[@class='btn btn-default']"))[1].click()

    def enable_new_product(self):
        wd = self.wd
        wd.find_element_by_xpath("//div[@class='btn-group btn-block btn-group-inline']/label[@class='btn btn-default']").click()

    def set_category_only_to(self, category_name):
        wd = self.wd
        wd.find_element_by_xpath("//div[@class='form-control']//input[@data-name='Root']").click()
        wd.find_element_by_xpath("//div[@class='form-control']//input[@data-name='%s']"%category_name).click()

    def random_string(self, min_len, max_len):
        symbols = string.ascii_letters + string.digits + " " + string.punctuation
        return "".join([random.choice(symbols) for i in range(random.randrange(min_len, max_len))])

    def random_numbers(self, min_len, max_len):
        return "".join([random.choice(string.digits) for i in range(random.randrange(min_len, max_len))])

    def set_product_name_to(self, product_name):
        wd = self.wd
        product_name_box = wd.find_element_by_name("name[en]")
        product_name_box.clear()
        product_name_box.send_keys(product_name)

    def move_to_prices(self):
        wd = self.wd
        wd.find_element_by_partial_link_text("Prices").click()

    def set_price(self):
        wd = self.wd
        price_box = wd.find_element_by_xpath("//div[@class='input-group']//input[@name='prices[USD]']")
        price_box.clear()
        price_box.send_keys(self.random_numbers(1,10))

    def destroy(self):
        self.wd.quit()