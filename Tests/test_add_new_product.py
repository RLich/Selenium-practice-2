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
    app.open_page(Config.admin_panel)
    app.login(Config.username, Config.password)

    # Przejście do katalogu w panelu administratora i dodanie nowego produktu poprzez wykonanie czynności:
        # Ustawienia produktu na aktywny i przypisanie go do wybranego katalogu, nadanie nazwy
        # Przejście do zakładki Prices, ustalenie okreslonej ceny
        # Przejście do zakładki Stock, ustawienie okreslonej ilości egzemplarzy i zatwierdzenie produktu
    app.enter_admin_catalog()
    app.add_new_product(category_name, product_name, price, quantity)

    # Wejście na frontową stronę katalogu i przejście do zdefiniowanej kategorii
    app.enter_shop_catalog()
    app.enter_selected_category(category_name)

    # Sprawdzenie, czy produkt o właściwej nazwie znajduje się w wybranej kategorii
    # Sprawdzenie, czy produkt posiada sticker "NEW"
    # Zapisanie stanu koszyka przed dodaniem do niego produktu
    assert app.check_product_name_with(product_name)
    assert app.get_product_sticker(product_name) == "NEW"
    cart_before_shopping = app.get_number_of_products_in_cart()

    # Przejście do okna produktu i sprawdzenie, czy ilość dostępnych egzemplarzy jest zgodna z ustawieniami
    # Dodanie produktu do koszyka i zamknięcie okna produktu
    app.enter_product(product_name)
    assert app.get_product_stock_status() == quantity + " pcs"
    app.add_product_to_cart()
    app.close_product_window()

    # Porównanie ilości produktów w koszyku przed i po dodaniu jednego produktu
    assert cart_before_shopping < app.get_number_of_products_in_cart()
    assert app.get_number_of_products_in_cart() == "1"