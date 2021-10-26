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
    ubox = browser.find_element(By.NAME, "email")
    pbox = browser.find_element(By.NAME, "password")
    ubox.send_keys(os.getenv('PANDASCORE_EMAIL'))
    pbox.send_keys(os.getenv('PANDASCORE_PASSWORD'))
    login_button = browser.find_element(By.TAG_NAME, "input")
    login_button.submit()
    
def go_to_account(browser):
    wait = WebDriverWait(browser, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Account')]")))
    account_button = browser.find_element(By.XPATH, "//a[contains(text(),'Account')]")
    account_button.click()

def get_new_name():
    print("Type your new name :")
    return input()

def change_name_from_account(browser):
    WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, "//html[@id='html']/body/div/div/div[2]/div/div/div/form/div/input"))).click()
    namebox = browser.find_element(By.XPATH, "//html[@id='html']/body/div/div/div[2]/div/div/div/form/div/input")
    print("Your name is :", namebox.get_attribute("value"))
    namebox.clear()
    namebox.send_keys(get_new_name())
    retype_password = browser.find_element(By.XPATH, "//html[@id='html']/body/div/div/div[2]/div/div/div/form/div[7]/input")
    retype_password.send_keys(os.getenv('PANDASCORE_PASSWORD'))
    sendform = browser.find_element(By.XPATH, "//html[@id='html']/body/div/div/div[2]/div/div/div/form/div[8]/button")
    sendform.click()

def infinit_loop():
    while True:
       c = 1

if __name__ == "__main__":
    load_dotenv()
    browser = init_brower()
    login(browser)
    go_to_account(browser)
    change_name_from_account(browser)
