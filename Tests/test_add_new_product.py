import time

import pytest

from Config.cfg_att import Config
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_new_product(app):
    category_name = "Rafał"
    product_name = app.random_string (5, 10)

    app.open_admin_panel_page()
    app.login(Config.username, Config.password)

    app.enter_admin_catalog()
    app.add_new_product()
    app.enable_new_product()
    app.set_category_only_to(category_name)
    app.set_product_name_to(product_name)
    app.move_to_prices()
    app.set_price()
    app.move_to_stock()
    app.set_quantity()
    app.submit_product()
    time.sleep(3)

