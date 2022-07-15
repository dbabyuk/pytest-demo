

def test_user_is_logged_in(main_page):
    assert main_page.get_title() == 'PRODUCTS'
