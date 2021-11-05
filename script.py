import selenium
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementNotSelectableException
from selenium.webdriver.chrome.options import Options

def init_brower():
    """[summary]
        Initialise the selinium browser with the right URL.
    Returns:
        [WebDriver]: [for Chrome, paht is pandascore loging page]
    """
    global browser
    s=Service(ChromeDriverManager().install())
    # browser = webdriver.Chrome("chromedriver.exe")
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-dev-shm-usage')
    browser = webdriver.Chrome(service=s, options=chrome_options)
    browser.get(os.getenv('PANDASCORE_URL'))
    return browser

def login(browser):
    """[summary]
        Log in the user. Using email and password from .env.
    Args:
        browser ([WebDriver]): [for Chrome, path must be pandascore loging page]
    """
    ubox = browser.find_element(By.NAME, "email")
    pbox = browser.find_element(By.NAME, "password")
    ubox.send_keys(os.getenv('PANDASCORE_EMAIL'))
    pbox.send_keys(os.getenv('PANDASCORE_PASSWORD'))
    login_button = browser.find_element(By.TAG_NAME, "input")
    login_button.submit()
    return 0
    
def go_to_account(browser):
    """[summary]
        Change path to the account page.
    Args:
        browser ([WebDriver]): [for Chrome, path must be pandascore loging page]
    """
    try:

        wait = WebDriverWait(browser, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Account')]")))
    except:
        print("Please, check your log information.")
        exit()
    account_button = browser.find_element(By.XPATH, "//a[contains(text(),'Account')]")
    account_button.click()
    return 0

def get_new_name():
    """[summary]
        Getting a new name from input.
    Returns:
        [not defined]: [new name of the user.]
    """
    print("Type your new name :")
    return input()

def get_current_name(namebox):
    """[summary]

    Args:
        namebox ([WebElement]): [name box from Account page]

    Returns:
        [string]: [Value of the name box.]
    """
    current_name = namebox.get_attribute("value")
    print("Your name is :", current_name)
    return current_name

def get_namebox(browser):
    """[summary]

    Args:
        browser ([type]): [for Chrome, path must be pandascore Account page]

    Returns:
        [WebElement]: [name box element in Account page.]
    """
    namebox = browser.find_element(By.XPATH, "//html[@id='html']/body/div/div/div[2]/div/div/div/form/div/input")
    return namebox

def change_name_from_account(browser):
    """[summary]
        Change your user name from an input after printing your previous one.
    Args:
        browser ([WebDriver]): [for Chrome, path mush be Account pandascore page. User must be logged in.]
    """
    WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, "//html[@id='html']/body/div/div/div[2]/div/div/div/form/div/input"))).click()
    namebox = get_namebox(browser)
    previous_name = get_current_name(namebox)
    namebox.clear()
    new_name = get_new_name()
    namebox.send_keys(new_name)
    retype_password = browser.find_element(By.XPATH, "//html[@id='html']/body/div/div/div[2]/div/div/div/form/div[7]/input")
    retype_password.send_keys(os.getenv('PANDASCORE_PASSWORD'))
    sendform = browser.find_element(By.XPATH, "//html[@id='html']/body/div/div/div[2]/div/div/div/form/div[8]/button")
    sendform.click()
    return [previous_name, new_name]

def handling_error():
    """[summary]
        Check if .env variables are not empty.
    """
    print(os.getenv('PANDASCORE_EMAIL'))
    print(os.getenv('PANDASCORE_PASSWORD'))
    print(os.getenv('PANDASCORE_URL'))
    if os.getenv('PANDASCORE_PASSWORD') == "" or os.getenv('PANDASCORE_EMAIL') == "" or os.getenv('PANDASCORE_URL') == "":
        print("Please, check your .env variables.")
        exit()
    return 0

if __name__ == "__main__":
    load_dotenv()
    handling_error()
    browser = init_brower()
    print(browser)
    login(browser)
    go_to_account(browser)
    change_name_from_account(browser)
