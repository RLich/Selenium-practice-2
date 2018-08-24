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

    # Wejście na stronę główną sklepu, przejście do wybranej kategorii
    # Zapisanie ilości produktów w koszyku
    app.open_page(Config.home_page)
    app.enter_selected_category(catalog_name)
    cart_before_shopping = app.get_number_of_products_in_cart()

    # Otwarcie okna pierwszego produktu, dodanie go do koszyka i zamknięcie okna
    app.enter_product("Mi A1")
    app.add_product_to_cart()
    app.close_product_window()

    # Otwarcie okna drugiego produktu, dodanie go do koszyka i zamknięcie okna
    app.enter_product("Mi Mix 2S")
    app.add_product_to_cart()
    app.close_product_window()

    # Otwarcie okna trzeciego produktu, dodanie go do koszyka i zamknięcie okna
    app.enter_product("Mi 8")
    app.add_product_to_cart()
    app.close_product_window()

    # Porównanie stanu koszyka przed i po włożeniu do niego produktów oraz upewnienie się, że ich liczba wynosi "3"
    assert cart_before_shopping < app.get_number_of_products_in_cart()
    assert app.get_number_of_products_in_cart() == "3"

    # Wejście do koszyka, wypełnienie danych klienta i potwierdzenie zakupu
    app.enter_cart()
    app.fill_customer_details()
    app.confirm_order()

    # Potwierdzenie wyskoczenia błędu "HTTP ERROR 500"
    # Powrót do sklepu i potwierdzenie "przesłania" zamówienia - koszyk powinien być pusty
    assert app.get_error_code() == "HTTP ERROR 500"
    app.open_page(Config.home_page)
    assert app.get_number_of_products_in_cart() == "0"