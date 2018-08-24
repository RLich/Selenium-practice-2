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
    cart_before_shopping = app.get_number_of_products_in_cart()

    app.enter_product("Mi A1")
    app.add_product_to_cart()
    app.close_product_window()

    app.enter_product("Mi Mix 2S")
    app.add_product_to_cart()
    app.close_product_window()

    app.enter_product("Mi 8")
    app.add_product_to_cart()
    app.close_product_window()

    assert cart_before_shopping < app.get_number_of_products_in_cart()

    app.enter_cart()

    app.fill_customer_details()

    assert app.get_error_code() == "HTTP ERROR 500"