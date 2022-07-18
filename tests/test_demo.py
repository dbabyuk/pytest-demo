import pytest


def test_user_is_logged_in(main_page):
    assert main_page.get_title() == 'PRODUCTS'


@pytest.mark.unit
def test_cart_is_empty(main_page):
    assert main_page.cart_icon_content() == ''


@pytest.fixture(scope='module')
def get_inventory_items(main_page):
    return main_page.inventory_items()


def test_inventory_number(get_inventory_items):
    assert len(get_inventory_items) == 6


def test_inventory_ordered_alphabetically(get_inventory_items):
    assert get_inventory_items == sorted(get_inventory_items)


@pytest.mark.parametrize('index_', range(6))
def test_image_is_present(main_page, index_):
    assert main_page.image_is_present(index_)


@pytest.mark.parametrize('index_', range(6))
def test_red_font_for_item_title(main_page, index_):
    assert main_page.font_color(index_) == 'red'


@pytest.mark.parametrize('index_', range(6))
def test_item_title_capitalized(main_page, index_):
    res = main_page.item_title_format(index_).split()
    assert res


@pytest.mark.parametrize('index_', range(6))
def test_add_to_cart_red_font(main_page, index_):
    res = main_page.font_color(index_, 'add_to_cart')
    assert res == 'red'

