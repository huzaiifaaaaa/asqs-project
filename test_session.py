import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config

if not os.path.exists("evd"): os.makedirs("evd")

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, config.EXPLICIT_WAIT)

def js_click(element):
    driver.execute_script("arguments[0].click();", element)

try:
    driver.get(config.LOGIN_URL)
    try:
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Close Welcome Banner']"))).click()
    except: pass

    wait.until(EC.visibility_of_element_located((By.ID, "email"))).send_keys(config.TEST_EMAIL)
    driver.find_element(By.ID, "password").send_keys(config.TEST_PASSWORD)
    js_click(driver.find_element(By.ID, "loginButton"))

    add_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Add to Basket']")))
    js_click(add_btn)
    print("Item added to basket.")
    
    time.sleep(1)

    account_btn = wait.until(EC.presence_of_element_located((By.ID, "navbarAccount")))
    js_click(account_btn)
    
    logout_btn = wait.until(EC.element_to_be_clickable((By.ID, "navbarLogoutButton")))
    js_click(logout_btn)
    print("Logged out successfully.")

    driver.get(config.LOGIN_URL)
    wait.until(EC.visibility_of_element_located((By.ID, "email"))).send_keys(config.TEST_EMAIL)
    driver.find_element(By.ID, "password").send_keys(config.TEST_PASSWORD)
    js_click(driver.find_element(By.ID, "loginButton"))

    print("Checking for basket persistence...")
    badge = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.fa-layers-counter")))
    current_count = badge.text
    assert int(current_count) > 0, f"Basket was lost! Found count: {current_count}"
    driver.save_screenshot("evd/session_success.png")
    print(f"Test Passed: Session persistence verified! Items in basket: {current_count}")
except Exception as e:
    driver.save_screenshot("evd/session_error.png")
    print(f"Test Failed: {e}")
    raise
finally:
    time.sleep(2)
    driver.quit()