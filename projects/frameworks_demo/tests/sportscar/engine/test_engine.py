from pytest import mark


@mark.smoke
@mark.engine
@mark.ui
def test_engine_functions_as_expected(chrome_browser):
    chrome_browser.get('https://www.artofmanliness.com')
    assert True
