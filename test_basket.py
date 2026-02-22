from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import config
import os
import time

if not os.path.exists("evd"):
    os.makedirs("evd")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
wait = WebDriverWait(driver, config.EXPLICIT_WAIT)

try:
    driver.get(config.LOGIN_URL)
    try:
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Close Welcome Banner']"))).click()
    except: pass

    wait.until(EC.visibility_of_element_located((By.ID, "email"))).send_keys(config.TEST_EMAIL)
    driver.find_element(By.ID, "password").send_keys(config.TEST_PASSWORD)
    driver.execute_script("arguments[0].click();", driver.find_element(By.ID, "loginButton"))

    search_icon = wait.until(EC.element_to_be_clickable((By.ID, "searchQuery")))
    search_icon.click()
    
    search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#mat-input-1")))
    search_input.send_keys(config.SEARCH_TERM + Keys.ENTER)

    add_to_basket_xpath = f"//div[contains(text(), '{config.PRODUCT_NAME}')]/../../..//button[@aria-label='Add to Basket']"
    add_btn = wait.until(EC.element_to_be_clickable((By.XPATH, add_to_basket_xpath)))
    driver.execute_script("arguments[0].click();", add_btn)

    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Placed Apple Juice')]")))
        print(f"Success: {config.PRODUCT_NAME} added to basket.")
    except:
        print("Confirmation snackbar not seen.")

    basket_badge = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.fa-layers-counter")))
    if basket_badge.text == "1":
        print("Test Passed: Basket badge count is 1.")
    else:
        print(f"Test Failed: Basket badge count is {basket_badge.text}")
    driver.save_screenshot("evd/add_to_basket_success.png")
finally:
    time.sleep(2)
    driver.quit()