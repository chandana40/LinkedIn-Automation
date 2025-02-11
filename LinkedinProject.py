from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://www.linkedin.com/login")
time.sleep(2)

name = driver.find_element(By.NAME, "session_key")
name.send_keys("sushmithau93@gmail.com")
time.sleep(2)

password = driver.find_element(By.NAME, "session_password")
password.send_keys("P@ssW0rd")
time.sleep(2)
print("TestCase:1 completed Successfully")

driver.find_element('xpath', '//*[@type="submit"]').click()
time.sleep(2)
print("TestCase:2 completed Successfully")

driver.get("https://www.linkedin.com/search/results/people/?keywords=Employee%20at%20go&origin=SWITCH_SEARCH_VERTICAL&page=80")
time.sleep(2)
print("TestCase:3 completed Successfully")

all_buttons = driver.find_elements(By.TAG_NAME, "button")
connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]

for btn in connect_buttons:
    driver.execute_script("arguments[0].click();", btn)
    time.sleep(2)
    print("TestCase:4 completed Successfully")

    send = driver.find_element(By.XPATH, "//button[@aria-label='Send without a note']")
    driver.execute_script("arguments[0].click();", send)
    time.sleep(2)
    if btn.text == "Connect":
        print("TestCase:5 completed Successfully")
    elif btn.text != "Connect":
        print("No Connect button found")
driver.close()
