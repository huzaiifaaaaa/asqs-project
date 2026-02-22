import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config
import os

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

    wait.until(EC.presence_of_element_located((By.ID, "navbarAccount")))
    time.sleep(1)

    print("Attempting to open product modal...")
    product_card = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "mat-grid-tile:nth-child(1) mat-card")))
    driver.execute_script("arguments[0].scrollIntoView();", product_card)
    
    try:
        product_card.click()
    except:
        js_click(product_card)

    print("Checking for modal visibility...")
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "mat-dialog-container")))
    
    review_area = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea[aria-label='Text field to review a product']")))
    review_area.click()
    review_area.send_keys("Team Cereal Killers: Quality Check!")
    
    submit_review = driver.find_element(By.ID, "submitButton")
    js_click(submit_review)

    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Cereal Killers')]")))
    driver.save_screenshot("evd/review_success.png")
    print("Test Passed: Review successfully posted and modal was opened!")
except Exception as e:
    driver.save_screenshot("evd/review_fail_state.png")
    print(f"Test Failed: {e}")
    raise
finally:
    time.sleep(2)
    driver.quit()