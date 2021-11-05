import pytest
from selenium import webdriver
import script

if __name__ == "__main__":
    script.load_dotenv()
    assert script.handling_error() == 0, "error handling not finalised"
    browser = script.init_brower()
    assert browser != None, "browser not initialised"
    assert script.login(browser) == 0, "login crashed"
    assert script.go_to_account(browser) == 0, "account page not found"
    names = script.change_name_from_account(browser)
    assert names[0] != names[1], "name did not change"
