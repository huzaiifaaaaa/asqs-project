That’s a smart organizational move for the team. It ensures that the CI/CD pipeline or a teammate can simply clone and run without manual edits.

Here is the updated **README.md** with the Branch Management section appended:

---

# ASQS Project: Automated Quality & Security Testing

## Team Cereal Killers

This repository contains a robust Selenium-based automation suite for the **OWASP Juice Shop**. The suite is designed to validate core business logic (Happy Paths) while probing for common security vulnerabilities and session management flaws.

### 📂 Repository Structure

* **`config.py`**: Centralized configuration for URLs, credentials, and wait times.
* **`test_login.py` / `test_signup.py`**: Basic authentication flow verification.
* **`test_checkout.py`**: Full End-to-End (E2E) flow from product selection to payment.
* **`test_review.py`**: Validation of social features and modal interactions.
* **`test_session.py` / `test_basket.py`**: Verification of session persistence and basket state.
* **`test_change_password.py`**: Security setting updates and account management.
* **Negative Tests**: `test_login_negative.py` and `test_signup_negative.py` probe for proper error handling.
* **`evd/`**: Automated screenshot directory for evidence of test passes/fails.

---

### 🌿 Branch Management

To streamline testing across different environments, the repository is organized into two primary branches. **No manual changes to `config.py` are required** if you clone the specific branch intended for your environment:

| Branch | Environment | Target URL | Purpose |
| --- | --- | --- | --- |
| **`local`** | Local Machine | `http://localhost:3000` | For development and local debugging. |
| **`deployed`** | Hosted site | `https://juice-shop.herokuapp.com/#` | For testing against a live, hosted instance. |

**Switching branches:**

```bash
git checkout local      # To test on your own machine
git checkout deployed   # To test against the public/deployed instance

```

---

### 🚀 Getting Started

#### 1. Prerequisites

* **Python 3.13+**
* **Google Chrome** & **ChromeDriver** (Ensure versions match).
* **OWASP Juice Shop** instance (local or remote).

#### 2. Environment Setup

```bash
# Navigate to project directory
cd asqs-project

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install selenium

```

---

### 🧪 Test Suite Overview

For **Team Cereal Killers**, the repository is structured to provide full coverage of the OWASP Juice Shop's functional and security requirements.

| Category | Test File | Description |
| --- | --- | --- |
| **Authentication** | `test_signup.py` | Validates new user registration and account creation logic. |
|  | `test_login.py` | Confirms successful authentication with valid user credentials. |
| **Functional (E2E)** | `test_checkout.py` | Full E2E flow: Product selection -> Basket -> Address -> Payment -> Delivery. |
|  | `test_basket.py` | Verifies that items are correctly added and held in the shopping cart. |
|  | `test_review.py` | Tests UI modal interaction and the ability to post product reviews. |
| **Session** | `test_session.py` | Verifies that the user session and basket items persist across logout/login. |
| **Security** | `test_change_password.py` | Validates that the account security settings correctly update user credentials. |
| **Negative (Security)** | `test_signup_negative.py` | Tests form resilience against invalid data or duplicate user registration. |
|  | `test_login_negative.py` | Rejects unauthorized access. |

---

### 🛠 Technical Challenges & Solutions

* **Synchronization**: Utilized `WebDriverWait` and `expected_conditions` to handle the asynchronous nature of the Angular frontend.
* **Interception Handling**: Implemented JavaScript-based clicks (`execute_script`) to bypass transparent overlays and Material "ripples."
* **Input Reliability**: Employed `ActionChains` for complex input scenarios in Material Design textareas.
* **Evidence Collection**: Scripts automatically save a screenshot to the `evd/` folder upon failure for immediate visual debugging.

---

### 📊 Running the Tests

To run an individual test case:

```bash
python3 test_{file_name}.py

```