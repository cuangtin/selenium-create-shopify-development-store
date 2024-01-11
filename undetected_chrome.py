import os
import time
import undetected_chromedriver as webdriver
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent

userAgent = UserAgent().random
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--start-maximized')
options.add_argument('--disable-popup-blocking')
options.add_argument(f'user-agent={userAgent}')
options.add_argument('--start-maximized')
options.add_argument('--enable-javascript')
options.add_argument('--disable-gpu')
options.add_argument('--incognito')
options.add_argument('--disable-popup-blocking')
options.add_argument('--force-device-scale-factor=0.8')

webdriver.TARGET_VERSION = 120
print('Add options')
driver = webdriver.Chrome(options=options, driver_executable_path=r'./chromedriver', use_subprocess=True, headless=True)
print("Open browser")
driver.get("https://partners.shopify.com/organizations")
driver.maximize_window()
try:
    print("Login page")
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
    time.sleep(4)
    submit = driver.find_element(By.CLASS_NAME, 'footer-form-submit')
    submit.click()
    print("Login success")
except:
    driver.quit()

try:
    print("Partner dashboard")
    addButton = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button.Polaris-Button--primary'))
    )
    addButton.click()
    time.sleep(1)
    createFwButton = driver.find_element(By.LINK_TEXT, 'Create development store')
    print("Click create development store button")
    createFwButton.click()
except:
    driver.get("https://partners.shopify.com/2023805/stores/new?store_type=test_store")

try:
    print("Create store page")
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
    submitButton.click()
    print("Create store processing... ~ 28s")
except:
    driver.quit()

time.sleep(28)
print("Add staff page")
driver.get("https://admin.shopify.com/store/"+storeName+"/settings/account/new")
time.sleep(7)
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
