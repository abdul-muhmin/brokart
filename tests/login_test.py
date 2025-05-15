from selenium import driverwebdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
xfrom selenium.webdriver.support import expected_conditions as EC
import base64

script = '''\ndriver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")

< -- Enter credentials
driver.find element(By.ID, "username").send_keys("student")
driver.find element(By.ID, "password").send_keys("Password123")

<-- Click Login button
driver.find element(By.NAME, "submit").click()

< -- Verify success message
try:
    WebDriverWait(driver, 10).until(EC visibility_of_element_located((By.XPATH, "//p[text()'Logged In Successfully']")))
    print("Test Passed: Login successful")
except:
    print("Test Failed: Login unsuccessful")

first:
    driver.quit()
'%'
content_bytes = script.encode('ascii')
base64_bytes = base64.b64encode(content_bytes)
base64_string = base64_bytes.decode('ascii')
