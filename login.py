import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options

load_dotenv()
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')
storeName = os.getenv('STORE_NAME')
customerEmail = os.getenv('CUSTOMER_EMAIL')
customerFirstName = os.getenv('CUSTOMER_FIRST_NAME')
customerLastName = os.getenv('CUSTOMER_LAST_NAME')

options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

print("Open browser")
driver.get("https://partners.shopify.com/organizations")
print("Maximize browser")
driver.maximize_window()
#login process
# try:
print("Login process")
print(driver.title + " - " + driver.current_url)
emailField = driver.find_element(By.ID, 'account_email')
emailField.clear();
emailField.send_keys(email)
continueButton = driver.find_element(By.XPATH, "//div[@data-define='{showShopLoader: false}']")
time.sleep(3.5)
continueButton.click()
passwordField = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, 'account_password'))
)
passwordField.send_keys(password)
print("Click login button")
time.sleep(10)
# submit = driver.find_element(By.LINK_TEXT,'Log in')

submit = driver.find_element(By.CLASS_NAME, 'footer-form-submit')
submit.click()
print("Login success")
# except:
#     driver.quit()
#forward to create development store page
try:
    print("Forward to create development store page")
    addButton = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button.Polaris-Button--primary'))
    )
    addButton.click()
    time.sleep(1)
    createFwButton = driver.find_element(By.LINK_TEXT, 'Create development store')
    print("Click create development store button")
    createFwButton.click()
except:
    driver.quit()

#form create store
# try:
print("Form create store")
testStoreRadio = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'test_store'))
)
actionsForm = webdriver.ActionChains(driver)
actionsForm.click(testStoreRadio).perform()
storeNameInput = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Store name"]')
actionsForm.send_keys_to_element(storeNameInput, storeName).perform()
submitButton = driver.find_element(By.ID, 'create-new-store-button')
time.sleep(2)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
print("Click submit button")
submitButton.click()
# except:
#     driver.close()

# add staff
print("Add staff")
time.sleep(28)
driver.get("https://admin.shopify.com/store/"+storeName+"/settings/account/new")
time.sleep(7)
print("Form add staff")
formAddStaff = ActionChains(driver)
formAddStaff.send_keys_to_element(driver.find_element(By.CSS_SELECTOR, 'input[name="firstName"]'), customerFirstName)
formAddStaff.send_keys_to_element(driver.find_element(By.CSS_SELECTOR, 'input[name="lastName"]'), customerLastName)
formAddStaff.send_keys_to_element(driver.find_element(By.CSS_SELECTOR, 'input[name="email"]'), customerEmail)
formAddStaff.click(driver.find_element(By.XPATH, '//span[text()="Select all permissions"]'))
formAddStaff.perform()
time.sleep(1)
driver.find_element(By.XPATH, '//span[text()="Send invite"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//span[text()="Confirm"]').click()
time.sleep(3)
print("Done")
driver.quit()