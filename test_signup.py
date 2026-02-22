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

    driver.find_element(By.ID, "emailControl").send_keys(config.TEST_EMAIL)
    driver.find_element(By.ID, "passwordControl").send_keys(config.TEST_PASSWORD)
    driver.find_element(By.ID, "repeatPasswordControl").send_keys(config.TEST_PASSWORD)
    
    driver.find_element(By.NAME, "securityQuestion").click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "mat-option:nth-child(1)"))).click()
    driver.find_element(By.ID, "securityAnswerControl").send_keys(config.SECURITY_ANSWER)

    register_btn = driver.find_element(By.ID, "registerButton")
    driver.execute_script("arguments[0].click();", register_btn)
    
    wait.until(EC.url_contains("/login"))
    driver.save_screenshot("evd/signup_success.png")
    print(f"Signup successful for: {config.TEST_EMAIL}")
finally:
    driver.quit()