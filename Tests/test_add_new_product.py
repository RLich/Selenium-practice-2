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
    price = app.random_number(1, 5)
    quantity = app.random_number(1, 5)

    # Wejście do panelu administratora, logowanie
    app.open_admin_panel_page(Config.admin_panel)
    app.login(Config.username, Config.password)

    # Przejście do katalogu w panelu administratora, dodanie nowego produktu poprzez wykonanie czynności:
    # Ustawienia produktu na aktywny i przypisanie go do wybranego katalogu, nadanie nazwy
    # Przejście do zakładki Prices, ustalenie okreslonej ceny
    # Przejście do zakładki Stock, ustawienie okreslonej ilości egzemplarzy i zatwierdzenie produktu
    app.enter_admin_catalog()
    app.add_new_product()
    app.enable_new_product()
    app.set_category_only_to(category_name)
    app.set_product_name_to(product_name)
    app.move_to_prices()
    app.set_price(price)
    app.move_to_stock()
    app.set_quantity(quantity)
    app.submit_product()

    # Wejście na frontową stronę katalogu i przejście do zdefiniowanej kategorii
    app.enter_front_end_catalog()
    app.enter_selected_category(category_name)

    # Sprawdzenie, czy produkt o właściwej nazwie znajduje się w wybranej kategorii
    # Sprawdzenie, czy produkt posiada sticker "NEW"
    # Zapisanie stanu koszyka przed dodaniem do niego produktu
    assert app.get_product_name(product_name)
    assert app.get_product_sticker(product_name) == "NEW"
    cart_before_shopping = app.get_number_of_products_in_cart()

    # Przejście do okna produktu i sprawdzenie, czy ilość dostępnych egzemplarzy jest zgodna z ustawieniami
    # Dodanie produktu do koszyka
    app.enter_product(product_name)
    assert app.get_product_stock_status() == quantity + " pcs"
    app.add_product_to_cart()

    # Zamknięcie okna produktu i zapisanie stanu koszyka po dodaniu produktu
    # Porównanie ilości produktów w koszyku po i przed dodaniem jednego produktu
    app.close_product_window()
    cart_after_shopping = app.get_number_of_products_in_cart()
    assert cart_after_shopping > cart_before_shopping