from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver, email_id, password_text):

    wait = WebDriverWait(driver, 20)

    email = wait.until(
        EC.visibility_of_element_located((By.ID, "email"))
    )
    email.clear()
    email.send_keys(email_id)

    continue_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    continue_btn.click()

    if email_id.strip() == "":
        print("Empty email test completed.")
        return

    password = wait.until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    password.clear()
    password.send_keys(password_text)

    login_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    login_btn.click()