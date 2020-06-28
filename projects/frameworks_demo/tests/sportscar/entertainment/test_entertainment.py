from pytest import mark


@mark.ui
@mark.entertainment
def test_entertainment_functions_as_expected(chrome_browser):
    chrome_browser.get('https://www.siriusxm.com/')
    assert True
