import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config

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

    wait.until(EC.presence_of_element_located((By.ID, "navbarAccount")))
    time.sleep(1)

    print("Navigating to Change Password page...")
    driver.get("http://localhost:3000/#/privacy-security/change-password")

    print("Filling form...")
    current_pwd = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#currentPassword")))
    current_pwd.send_keys(config.TEST_PASSWORD)
    
    driver.find_element(By.CSS_SELECTOR, "input#newPassword").send_keys(config.TEST_PASSWORD)
    driver.find_element(By.CSS_SELECTOR, "input#newPasswordRepeat").send_keys(config.TEST_PASSWORD)
    
    change_btn = wait.until(EC.element_to_be_clickable((By.ID, "changeButton")))
    js_click(change_btn)

    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Your password was successfully changed')]")))
    
    if not os.path.exists("evd"): os.makedirs("evd")
    driver.save_screenshot("evd/password_changed.png")
    print("Test Passed: Password change verified!")
except Exception as e:
    if not os.path.exists("evd"): os.makedirs("evd")
    driver.save_screenshot("evd/password_error.png")
    print(f"Test Failed: {e}")
    raise
finally:
    time.sleep(2)
    driver.quit()