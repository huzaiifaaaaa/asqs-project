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

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
wait = WebDriverWait(driver, config.EXPLICIT_WAIT)

try:
    driver.get(config.LOGIN_URL)
    
    try:
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Close Welcome Banner']"))).click()
        driver.find_element(By.CSS_SELECTOR, "a[aria-label='dismiss cookie message']").click()
    except:
        pass

    wait.until(EC.visibility_of_element_located((By.ID, "email"))).send_keys(config.TEST_EMAIL)
    driver.find_element(By.ID, "password").send_keys(config.TEST_PASSWORD)

    login_btn = driver.find_element(By.ID, "loginButton")
    driver.execute_script("arguments[0].click();", login_btn)

    wait.until(EC.url_contains("/search"))
    driver.save_screenshot("evd/login_success.png")
    print("Login verified.")
finally:
    driver.quit()