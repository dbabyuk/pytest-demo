import pytest


class TestFirstPart:

    def test_user_is_logged_in(self, main_page):
        assert main_page.get_title() == 'PRODUCTS'

    def test_cart_is_empty(self, main_page):
        assert main_page.cart_icon_content() == ''

    @pytest.fixture(scope='class')
    def get_inventory_items(self, main_page):
        return main_page.inventory_items()

    def test_inventory_number(self, get_inventory_items):
        assert len(get_inventory_items) == 6

    def test_inventory_ordered_alphabetically(self, get_inventory_items):
        assert get_inventory_items == sorted(get_inventory_items)


_ids = {item_index: f'Product_{item_index + 1}' for item_index in range(6)}


class TestSecondPart:

    @pytest.fixture(scope='class', params=_ids.keys(), ids=_ids.values())
    def parametrized_index(self, request):
        return request.param

    def test_image_is_present(self, main_page, parametrized_index):
        assert main_page.image_is_present(parametrized_index)

    def test_red_font_for_item_title(self, main_page, parametrized_index):
        assert main_page.font_color(parametrized_index) == 'red'

    def test_item_title_capitalized(self, main_page, parametrized_index):
        res = main_page.item_title_name(parametrized_index).split()
        assert res

    def test_add_to_cart_red_font(self, main_page, parametrized_index):
        res = main_page.font_color(parametrized_index, 'add_to_cart')
        assert res == 'red'

    @pytest.fixture(scope='class', params=_ids.keys(), ids=_ids.values())
    def select_single_item(self, main_page, request) -> int:
        """Selects a parametrized item by index and returns the index value"""
        main_page.add_or_remove_item(index_=request.param)
        yield request.param
        if main_page.item_text(index_=request.param) == 'REMOVE':
            main_page.add_or_remove_item(index_=request.param)

    def test_add_item_to_the_cart(self, main_page, select_single_item):
        item_selected = main_page.item_text(index_=select_single_item)
        assert item_selected == 'REMOVE'

    def test_black_color_remove_btn(self, main_page, select_single_item):
        item_selected = main_page.font_color(index_=select_single_item, object_element='add_to_cart')
        assert item_selected == 'black'

    def test_cart_label_is_one(self, main_page, select_single_item):
        assert main_page.cart_icon_content() == '1'

    @pytest.fixture(scope='class')
    def item_values_on_main_page(self, main_page, select_single_item) -> dict:
        return {'title': main_page.item_title_name(index_=select_single_item),
                'price': main_page.item_price(index_=select_single_item)}

    @pytest.fixture(scope='class')
    def click_cart_icon(self, main_page, select_single_item, item_values_on_main_page, cart_page) -> dict:
        """Clicks on cart icon and returns the dictionary of item values on main page"""
        main_page.click_cart_icon()
        yield item_values_on_main_page
        if cart_page.get_title() == "YOUR CART":
            cart_page.continue_shopping()

    def test_cart_page_is_active(self, click_cart_icon, cart_page):
        assert cart_page.get_title() == "YOUR CART"

    def test_quantity_field_is_one(self, click_cart_icon, cart_page):
        assert cart_page.quantity_field_content() == '1'

    def test_item_name_on_cart_page_matches_main_page_name(self, click_cart_icon, cart_page):
        title_from_cart_page = cart_page.item_title_name()
        title_from_main_page = click_cart_icon['title']
        assert title_from_cart_page == title_from_main_page

    def test_item_price_match(self, click_cart_icon, cart_page):
        price_from_cart_page = cart_page.item_price()
        price_from_main_page = click_cart_icon['price']
        assert price_from_cart_page == price_from_main_page

    @pytest.fixture(scope='class')
    def click_remove_btn(self, click_cart_icon, cart_page):
        cart_page.add_or_remove_item()

    def test_no_products_in_the_cart(self, click_remove_btn, cart_page):
        assert not cart_page.product_items_are_present()

    def test_cart_icon_without_labels(self, click_remove_btn, cart_page):
        assert cart_page.cart_icon_content() == ''

    @pytest.fixture(scope='function')
    def click_continue_shopping(self, click_remove_btn, cart_page):
        cart_page.continue_shopping()

    def test_initial_browser_state(self, click_continue_shopping, main_page):
        assert main_page.get_title() == 'PRODUCTS' and main_page.cart_icon_content() == ''
