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
    app.open_admin_panel_page()
    app.login(Config.username, Config.password)
    app.enter_catalog()
    app.add_new_product()
    app.enable_new_product()
    time.sleep(3)

