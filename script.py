import selenium 
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
from selenium.webdriver.support import expected_conditions as EC
load_dotenv()
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementNotSelectableException

if __name__ == "__main__":
    global browser
    s=Service(ChromeDriverManager().install())
    # browser = webdriver.Chrome("chromedriver.exe")
    browser = webdriver.Chrome(service=s)
    browser.get(os.getenv('PANDASCORE_URL'))
    ubox = browser.find_element_by_name("email")
    pbox = browser.find_element_by_name("password")
    
    ubox.send_keys(os.getenv('PANDASCORE_EMAIL'))
    pbox.send_keys(os.getenv('PANDASCORE_PASSWORD'))

    login_button = browser.find_element_by_tag_name("input")
    login_button.submit()
    wait = WebDriverWait(browser, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Account')]")))
    account_button = browser.find_element(By.XPATH, "//a[contains(text(),'Account')]")
    account_button.click()
    WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, "//html[@id='html']/body/div/div/div[2]/div/div/div/form/div/input"))).click()
    namebox = browser.find_element(By.XPATH, "//html[@id='html']/body/div/div/div[2]/div/div/div/form/div/input")
    namebox.clear()
    namebox.send_keys(os.getenv('PANDASCORE_NEWNAME'))
    retype_password = browser.find_element(By.XPATH, "//html[@id='html']/body/div/div/div[2]/div/div/div/form/div[7]/input")
    retype_password.send_keys(os.getenv('PANDASCORE_PASSWORD'))
    sendform = browser.find_element(By.XPATH, "//html[@id='html']/body/div/div/div[2]/div/div/div/form/div[8]/button")
    sendform.click()

    while True:
       c = 1