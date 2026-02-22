This README is tailored specifically for your project structure as seen in your file explorer. It presents **Team Cereal Killers** as a professional security-minded automation team.

---

# ASQS Project: Automated Quality & Security Testing

## Team Cereal Killers

This repository contains a robust Selenium-based automation suite for the **OWASP Juice Shop**. The suite is designed to validate core business logic (Happy Paths) while probing for common security vulnerabilities and session management flaws.

### 📂 Repository Structure

Based on the project layout:

* **`config.py`**: Centralized configuration for URLs, credentials, and wait times.
* **`test_login.py` / `test_signup.py`**: Basic authentication flow verification.
* **`test_checkout.py`**: Full End-to-End (E2E) flow from product selection to payment.
* **`test_review.py`**: Validation of social features and modal interactions.
* **`test_session.py` / `test_basket.py`**: Verification of session persistence and basket state.
* **`test_change_password.py`**: Security setting updates and account management.
* **Negative Tests**: `test_login_negative.py` and `test_signup_negative.py` probe for proper error handling and input validation.
* **`evd/`**: Automated screenshot directory for evidence of test passes/fails.

---

### 🚀 Getting Started

#### 1. Prerequisites

* **Python 3.13+**
* **Google Chrome** & **ChromeDriver** (Ensure versions match).
* **OWASP Juice Shop** instance running at `http://localhost:3000` or `https://juice-shop.herokuapp.com/#`

#### 2. Environment Setup

```bash
# Navigate to project directory
cd asqs-project

# Activate virtual environment
source venv/bin/activate

# Install dependencies (if not already installed)
pip install selenium

```

#### 3. Configuration

Ensure `config.py` is updated with your local settings. This prevents hardcoding credentials across multiple files.

---

### 🧪 Test Suite Overview

| Category | Test File | Description |
| --- | --- | --- |
| **Authentication** | `test_signup.py` | Validates new user registration and form submission. |
|  | `test_login.py` | Validates successful user authentication. |
| **Functional** | `test_checkout.py` | E2E test: Add to basket -> Address selection -> Payment. |
|  | `test_review.py` | Handles modal pop-ups and posting product reviews. |
| **Session** | `test_session.py` | Verifies basket items persist across logout/login cycles. |
| **Security** | `test_change_password.py` | Validates secure credential updating functionality. |
| **Negative** | `test_login_negative.py` | Rejection of unauthorized access and SQLi attempts. |

---

### 🛠 Technical Challenges & Solutions

* **Synchronization**: Utilized `WebDriverWait` and `expected_conditions` to handle the asynchronous nature of the Angular frontend, avoiding flaky `time.sleep` calls.
* **Interception Handling**: Implemented JavaScript-based clicks (`execute_script`) to bypass transparent overlays and Angular Material "ripples" that physically block standard Selenium clicks.
* **Input Reliability**: Employed `ActionChains` for complex input scenarios, such as typing inside Material Design textareas (Reviews) where standard `send_keys` can fail.
* **Evidence Collection**: Every script includes a `try-except` block that automatically saves a screenshot to the `evd/` folder upon failure, providing immediate visual debugging.

---

### 📊 Running the Tests

To run an individual test case, use:

```bash
python3 test_{file_name}.py

```