import pytest
from selenium import webdriver
import script

if __name__ == "__main__":
    script.load_dotenv()
    script.handling_error()
    browser = script.init_brower()
    script.login(browser)
    script.go_to_account(browser)
    script.change_name_from_account(browser)
