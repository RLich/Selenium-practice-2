import time

import pytest

from Config.cfg_att import Config
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_buy_products(app):
    catalog_name = " XiaomiLepsze"

    app.open_page(Config.home_page)
    app.enter_selected_category(catalog_name)
    time.sleep(2)