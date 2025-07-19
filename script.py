from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome with bot evasion
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options)
driver.maximize_window()

# Open Stripe test checkout page
driver.get("https://checkout.stripe.com/c/pay/ppage_1RmRgtLE4wKZaCzD4UhZGTPC#fidkdWxOYHwnPyd1blpxYHZxWjA0V1VRQF9JQDFyTl9kRn9BTDJIRjZiUX01clFRUV1EXGZfQ2dQb3xkPF9DSF11X08yYWBLSH1ETnREVUhuc05Ma2RjMX9dVzRBX2Iyd3N9TU53SzVyQE9RNTVUS1FqNjxyXycpJ2hsYXYnP34nYnBsYSc%2FJ2A9YWYwMjMxKDJkNjMoMTZjPCg9YDY1KGNkMjM9MmFmND1nZDY8YDJhYycpJ2hwbGEnPyc0Z2E9PTc8YygzNDI8KDFmNjIoPDdgZChkZDJkYWQ1PDFgY2cwMDZnNTcnKSd2bGEnPyc2MTYyNDw2YyhmMjIzKDEyPWMoZzU0MihjMjwwYDxnYTFnNTw3M2M0N2AneCknZ2BxZHYnP15YKSdpZHxqcHFRfHVgJz8naHBpcWxabHFgaCcpJ3dgY2B3d2B3SndsYmxrJz8nbXFxdXY%2FKipgZmpoaGB3ZmAocmxxbSh2cXdsdWAodmx9K3Ngd2ZgaStkdXUnKSdpamZkaWAnP2twaWl4JSUl")

# Wait for iframes
WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, "iframe")))

# Switch into iframe containing card number input
iframes = driver.find_elements(By.TAG_NAME, "iframe")

for frame in iframes:
    driver.switch_to.frame(frame)
    try:
        card_input = driver.find_element(By.NAME, "cardNumber")
        card_input.send_keys("4242424242424242")
        driver.find_element(By.NAME, "exp-date").send_keys("1230")
        driver.find_element(By.NAME, "cvc").send_keys("123")
        driver.find_element(By.NAME, "postal").send_keys("12345")
        break
    except Exception as e:
        print(e)
        driver.switch_to.default_content()
        continue

driver.switch_to.default_content()

# Click the "Pay" button
buttons = driver.find_elements(By.TAG_NAME, "button")
for btn in buttons:
    if "pay" in btn.text.lower():
        btn.click()
        print(f"Clicked button {btn.id}")
        break

# Wait for confirmation screen (adjust selector depending on your page)
time.sleep(60)  # Replace with WebDriverWait in production

print("Test completed. Check browser for confirmation.")

driver.quit()
