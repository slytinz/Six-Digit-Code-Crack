"""
------ Pseudocode:

create variable "guess" == 000000

while guess != 999999:
    ++guess
    submit guess

    if submission == valid
        exit

"""
import selenium
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
WebDriverWait(driver,10000).until(EC.visibility_of_element_located((By.TAG_NAME,'body')))

# Inserts email we want to reset password for
email = '/html/body/div/div/div/main/div[2]/div[3]/div/div[2]/div[1]/div/form/div[1]/div/div[1]/div/input'
input_email = driver.find_element_by_xpath(email)
input_email.click()
# TODO: Erase email before pushing
input_email.send_keys("")
input_email.send_keys(Keys.ENTER)

# TODO: THIS SECTION IS FOR VERIFICATION CODE


time.sleep(5)

driver.quit()




# def generate():
#     guess = 000000
#     submission = False

#     while guess < 999999:
#         if submission == True:
#             break
