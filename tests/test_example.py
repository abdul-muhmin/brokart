from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Replace with your actual browser driver path
driver = webdriver.Chrome(executable_path="path/to/chromedriver")

# Navigate to the website where you want to perform the actions
driver.get("https://www.example.com")  # Replace with your actual URL

# Wait for the element to be clickable
wait = WebDriverWait(driver, 10)  # Adjust the timeout if needed
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Submit')]--><!--
--><!--
--><!--
-->"))) 

# Click the element
element.click()

# Example of creating Fibonacci series
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Example usage of the function
n = 10  # Specify the number of Fibonacci numbers to generate
for i in range(n):
    print(fibonacci(i))

# Close the browser
driver.quit()