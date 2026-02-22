import time

BASE_URL = "https://juice-shop.herokuapp.com/#"
SIGNUP_URL = f"{BASE_URL}/register"
LOGIN_URL = f"{BASE_URL}/login"
BASKET_URL = f"{BASE_URL}/basket"

TIMESTAMP = int(time.time())
TEST_EMAIL = f"cereal_killer_2026@test.com"
TEST_PASSWORD = "Security_2026!"
SECURITY_ANSWER = "Software Quality"

INVALID_EMAIL = "not-an-email"
WEAK_PASSWORD = "123"
WRONG_PASSWORD = "WrongPassword123!"

SEARCH_TERM = "Apple"
PRODUCT_NAME = "Apple Juice (1000ml)"

FULL_NAME = "Team Cereal Killers"
MOBILE_NUMBER = "1234567890"
ZIP_CODE = "90570"
STREET_ADDRESS = "Pentti Kaiteran katu 1, Oulu"
CITY = "Oulu"
COUNTRY = "Finland"
CARD_NAME = "Huzaifa"
CARD_NUMBER = "1111222233334444"
EXPIRY_MONTH = "12"
EXPIRY_YEAR = "2029"

IMPLICIT_WAIT = 10
EXPLICIT_WAIT = 15