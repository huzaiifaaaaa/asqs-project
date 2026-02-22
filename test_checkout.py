import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config

if not os.path.exists("evd"):
    os.makedirs("evd")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
wait = WebDriverWait(driver, config.EXPLICIT_WAIT)

def js_click(element):
    driver.execute_script("arguments[0].click();", element)

try:
    driver.get(config.LOGIN_URL)
    try:
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Close Welcome Banner']"))).click()
    except:
        pass

    wait.until(EC.visibility_of_element_located((By.ID, "email"))).send_keys(config.TEST_EMAIL)
    driver.find_element(By.ID, "password").send_keys(config.TEST_PASSWORD)
    js_click(driver.find_element(By.ID, "loginButton"))

    wait.until(EC.presence_of_element_located((By.ID, "navbarAccount")))
    
    basket_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Show the shopping cart"]')))
    js_click(basket_btn)

    checkout_btn = wait.until(EC.element_to_be_clickable((By.ID, "checkoutButton")))
    js_click(checkout_btn)

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Add a new address']"))).click()
    
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder*='country']"))).send_keys(config.COUNTRY)
    driver.find_element(By.CSS_SELECTOR, "input[placeholder*='name']").send_keys(config.FULL_NAME)
    driver.find_element(By.CSS_SELECTOR, "input[placeholder*='mobile']").send_keys(config.MOBILE_NUMBER)
    driver.find_element(By.CSS_SELECTOR, "input[placeholder*='ZIP']").send_keys(config.ZIP_CODE)
    driver.find_element(By.ID, "address").send_keys(config.STREET_ADDRESS)
    driver.find_element(By.CSS_SELECTOR, "input[placeholder*='city']").send_keys(config.CITY)
    
    address_submit = wait.until(EC.element_to_be_clickable((By.ID, "submitButton")))
    js_click(address_submit)

    address_radio = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "mat-radio-button")))
    js_click(address_radio)
    
    continue_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Proceed to payment selection']")))
    js_click(continue_btn)

    delivery_radio = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "mat-radio-button")))
    js_click(delivery_radio)
    js_click(driver.find_element(By.CSS_SELECTOR, "button[aria-label='Proceed to delivery method selection']"))

    print("Expanding payment panel...")
    payment_panel = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "mat-expansion-panel-header")))
    js_click(payment_panel)
    
    print("Filling card details...")
    name_xpath = "//mat-label[contains(text(),'Name')]/ancestor::mat-form-field//input"
    card_xpath = "//mat-label[contains(text(),'Card Number')]/ancestor::mat-form-field//input"
    month_xpath = "//mat-label[contains(text(),'Expiry Month')]/ancestor::mat-form-field//select"
    year_xpath = "//mat-label[contains(text(),'Expiry Year')]/ancestor::mat-form-field//select"

    wait.until(EC.visibility_of_element_located((By.XPATH, name_xpath))).send_keys(config.CARD_NAME)
    driver.find_element(By.XPATH, card_xpath).send_keys(config.CARD_NUMBER)
    driver.find_element(By.XPATH, month_xpath).send_keys(config.EXPIRY_MONTH)
    driver.find_element(By.XPATH, year_xpath).send_keys(config.EXPIRY_YEAR)
    
    js_click(driver.find_element(By.ID, "submitButton"))

    card_radio = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "mat-radio-button")))
    js_click(card_radio)
    js_click(driver.find_element(By.CSS_SELECTOR, "button[aria-label='Proceed to review']"))

    final_checkout = wait.until(EC.element_to_be_clickable((By.ID, "checkoutButton")))
    js_click(final_checkout)

    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Thank you for your purchase')]")))
    driver.save_screenshot("evd/checkout_complete.png")
    print("Test Passed: Full End-to-End Checkout completed successfully!")
finally:
    time.sleep(3)
    driver.quit()