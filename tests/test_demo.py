import pytest


def test_user_is_logged_in(main_page):
    assert main_page.get_title() == 'PRODUCTS'


def test_cart_is_empty(main_page):
    assert main_page.cart_icon_content() == ''


@pytest.fixture(scope='module')
def get_inventory_items(main_page):
    return main_page.inventory_items()


def test_inventory_number(get_inventory_items):
    assert len(get_inventory_items) == 6


def test_inventory_ordered_alphabetically(get_inventory_items):
    assert get_inventory_items == sorted(get_inventory_items)


_ids = {item_index: f'Product_{item_index + 1}' for item_index in range(6)}


@pytest.mark.parametrize('index_', _ids.keys(), ids=_ids.values())
def test_image_is_present(main_page, index_):
    assert main_page.image_is_present(index_)


@pytest.mark.parametrize('index_', _ids.keys(), ids=_ids.values())
def test_red_font_for_item_title(main_page, index_):
    assert main_page.font_color(index_) == 'red'


@pytest.mark.parametrize('index_', _ids.keys(), ids=_ids.values())
def test_item_title_capitalized(main_page, index_):
    res = main_page.item_title_name(index_).split()
    assert res


@pytest.mark.parametrize('index_', _ids.keys(), ids=_ids.values())
def test_add_to_cart_red_font(main_page, index_):
    res = main_page.font_color(index_, 'add_to_cart')
    assert res == 'red'


@pytest.fixture(scope='module')
def select_single_item(main_page):
    main_page.select_item()


@pytest.mark.unit
def test_add_item_to_the_cart(main_page, select_single_item):
    item_selected = main_page.item_text()
    assert item_selected == 'REMOVE'


def test_black_color_remove_btn(main_page, select_single_item):
    item_selected = main_page.font_color(object_element='add_to_cart')
    assert item_selected == 'black'


@pytest.mark.unit
def test_cart_label_is_one(main_page, select_single_item):
    assert main_page.cart_icon_content() == '1'


@pytest.fixture(scope='module')
def item_values_on_main_page(main_page) -> dict:
    return {'title': main_page.item_title_name(), 'price': main_page.item_price()}


@pytest.fixture(scope='module')
def click_cart_icon(main_page, select_single_item, item_values_on_main_page) -> dict:
    """Clicks on cart icon and returns the dictionary of item values on main page"""
    main_page.click_cart_icon()
    return item_values_on_main_page


def test_cart_page_is_active(click_cart_icon, cart_page):
    assert cart_page.get_title() == "YOUR CART"


def test_quantity_field_is_one(click_cart_icon, cart_page):
    assert cart_page.quantity_field_content() == '1'


def test_item_name_on_cart_page_matches_main_page_name(click_cart_icon, cart_page):
    title_from_cart_page = cart_page.item_title_name()
    title_from_main_page = click_cart_icon['title']
    assert title_from_cart_page == title_from_main_page


def test_item_price_match(click_cart_icon, cart_page):
    price_from_cart_page = cart_page.item_price()
    price_from_main_page = click_cart_icon['price']
    assert price_from_cart_page == price_from_main_page

# @pytest.fixture(scope='module')
# def click_remove_btn(click_cart_icon, cart_page, main_page):
#     main_page.select_item()
#
# def test_1(click_remove_btn):
#     pass



