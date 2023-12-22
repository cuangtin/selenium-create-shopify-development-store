import os
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

load_dotenv()

#authenticate
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')

driver = webdriver.Firefox()
driver.get("https://www.shopify.com/partners")
# driver.maximize_window()

#foward to login page
loginButton = driver.find_element(By.LINK_TEXT, "Log in")
loginButton.click()

actions = ActionChains(driver);
emailField = driver.find_element(By.ID, "account_email")
emailField.clear();
actions.send_keys_to_element(emailField, email)
# actions.click(continueButton)
actions.perform()
continueButton = driver.find_element(By.XPATH, "//div[@data-define='{showShopLoader: false}']")
print(continueButton.text)
actions.click(continueButton).perform()
# passwordField = WebDriverWait(driver, 5).until(
#         EC.presence_of_element_located((By.ID, "account_password"))
# )
# passwordField.send_keys(password)

# submit = driver.find_element(By.NAME, "commit")
# submit.send_keys(Keys.RETURN)

# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()