import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')
customerName = os.getenv('CUSTOMER_NAME')

driver = webdriver.Firefox()
driver.get("https://www.shopify.com/partners")
# driver.maximize_window()

loginButton = driver.find_element(By.LINK_TEXT, 'Log in')
loginButton.click()

#login process
try:
    emailField = driver.find_element(By.ID, 'account_email')
    emailField.clear();
    emailField.send_keys(email)
    continueButton = driver.find_element(By.XPATH, "//div[@data-define='{showShopLoader: false}']")
    time.sleep(3)
    continueButton.click()
    passwordField = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, 'account_password'))
    )
    passwordField.send_keys(password)
    time.sleep(3)
    submit = driver.find_element(By.CSS_SELECTOR,'div.footer-form-submit')
    submit.click()
except:
    driver.quit()
#forward to create development store page
try:
    addButton = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button.Polaris-Button--primary'))
    )
    addButton.click()
    time.sleep(1)
    createFwButton = driver.find_element(By.LINK_TEXT, 'Create development store')
    createFwButton.click()
except:
    driver.quit()

#form create store
try:
    testStoreRadio = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, 'test_store'))
    )
    actionsForm = webdriver.ActionChains(driver)
    actionsForm.click(testStoreRadio).perform()
    storeName = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Store name"]')
    actionsForm.send_keys_to_element(storeName, customerName).perform()
    time.sleep(5)
    actionsForm.click(driver.find_element(By.ID, 'create-new-store-button')).perform()
except:
    driver.close()

# new store admin page
posButton = WebDriverWait(driver, 120).until(
    EC.presence_of_element_located((By.LINK_TEXT, 'Point of Sale'))
).click()
staffPage = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.LINK_TEXT, 'Staff'))
).click()

# staff page
addStaffButton = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.LINK_TEXT, 'Add staff'))
).click()
