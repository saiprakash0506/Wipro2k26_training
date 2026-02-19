import pytest
import csv
import os
import time
from selenium.webdriver.common.by import By

def get_csv_data(file_path):
    rows = []
    if not os.path.exists(file_path): return rows
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            clean_row = [item.strip() for item in row]
            if len(clean_row) > 3: clean_row = [clean_row[0], clean_row[1], ",".join(clean_row[2:])]
            rows.append(clean_row)
    return rows

@pytest.mark.usefixtures("setup")
class TestNegativeLogin:
    
    csv_path = os.path.join("data", "invalidlogin_data.csv")

    @pytest.mark.parametrize("u, p, error", get_csv_data(csv_path))
    def test_00_neg_logins(self, u, p, error):
        driver = self.driver
        log = self.logger # Access the per-test log file

        log.info(f"--- STARTING TEST CASE: {u} ---")
        driver.get("https://www.saucedemo.com/")
        time.sleep(1.5) # Slow down

        # 1. Locate
        user_field = driver.find_element(By.ID, "user-name")
        pass_field = driver.find_element(By.ID, "password")
        login_btn = driver.find_element(By.ID, "login-button")

        # 2. Positive Assertions
        log.info(f"Entering username: {u}")
        user_field.send_keys(u)
        time.sleep(1)
        assert user_field.get_attribute("value") == u
        log.info("POSITIVE ASSERT: Username field verified.")

        log.info(f"Entering password: {p}")
        pass_field.send_keys(p)
        time.sleep(1)
        assert pass_field.get_attribute("value") == p
        log.info("POSITIVE ASSERT: Password field verified.")

        # 3. Action
        log.info("Clicking login button...")
        login_btn.click()
        time.sleep(1.5)

        # 4. Negative Assertions
        error_element = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
        actual_error = error_element.text
        log.info(f"Actual error displayed: {actual_error}")

        # Space-proof comparison
        assert error.lower().replace(" ", "") in actual_error.lower().replace(" ", ""), \
            f"Expected {error} but got {actual_error}"
        
        log.info("NEGATIVE ASSERT: Error message validation successful.")
        log.info("--- TEST CASE COMPLETED PASSED ---")