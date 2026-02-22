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
    driver.get(config.LOGIN_URL)
    try:
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Close Welcome Banner']"))).click()
    except:
        pass

    wait.until(EC.visibility_of_element_located((By.ID, "email"))).send_keys(config.TEST_EMAIL)
    driver.find_element(By.ID, "password").send_keys(config.WRONG_PASSWORD)

    login_btn = driver.find_element(By.ID, "loginButton")
    driver.execute_script("arguments[0].click();", login_btn)

    try:
        error_msg = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Invalid email or password')]")))
        print("Test Passed: 'Invalid email or password' error message displayed.")
    except:
        print("Test Failed: Error message not found!")

    if "/login" in driver.current_url:
        print("Test Passed: User remained on the login page.")
    else:
        print("Test Failed: User was redirected away from login page despite error!")
    
    driver.save_screenshot("evd/login_negative_test.png")
finally:
    driver.quit()