from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config
import os

if not os.path.exists("evd"):
    os.makedirs("evd")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
wait = WebDriverWait(driver, config.EXPLICIT_WAIT)

try:
    driver.get(config.SIGNUP_URL)

    try:
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Close Welcome Banner']"))).click()
        driver.find_element(By.CSS_SELECTOR, "a[aria-label='dismiss cookie message']").click()
    except:
        pass

    email_input = driver.find_element(By.ID, "emailControl")
    pass_input = driver.find_element(By.ID, "passwordControl")
    repeat_input = driver.find_element(By.ID, "repeatPasswordControl")

    email_input.send_keys(config.INVALID_EMAIL)
    pass_input.send_keys(config.WEAK_PASSWORD)
    repeat_input.send_keys(config.WEAK_PASSWORD)
    
    driver.find_element(By.NAME, "securityQuestion").click()

    try:
        email_error = wait.until(EC.visibility_of_element_located((By.XPATH, "//mat-error[contains(text(), 'Email address is invalid')]")))
        pass_error = wait.until(EC.visibility_of_element_located((By.XPATH, "//mat-error[contains(text(), 'Password must be')]")))
        print("Validation errors successfully displayed.")
    except:
        print("Error: Validation messages did not appear!")

    register_btn = driver.find_element(By.ID, "registerButton")
    is_disabled = not register_btn.is_enabled()
    
    if is_disabled:
        print("Test Passed: Register button is correctly disabled for invalid input.")
    else:
        print("Test Failed: Register button is enabled despite invalid input!")

    driver.save_screenshot("evd/signup_negative_test.png")
finally:
    driver.quit()