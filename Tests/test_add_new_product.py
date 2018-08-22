import pytest
from Config.cfg_att import Config
from application import Application
import time

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_new_product(app):
    category_name = "Rafał"

    app.open_admin_panel_page()
    app.login(Config.username, Config.password)

    app.enter_catalog()
    app.add_new_product()
    app.enable_new_product()
    app.set_category_only_to(category_name)
    app.set_product_date_validation()
    time.sleep(3)

