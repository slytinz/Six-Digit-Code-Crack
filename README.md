# GOAL: Break in to my own account by guesing the 6-digit verification code #

### Issue: ###
- Whenever you click on ```Forgot Password```, a verification code is sent in an email to the user. Currently, there is no limitations on how many times good/malicious user can input the verification code. We must provide proof that this can occur.

### Solutions: ###
1. Connecting to website using golang script or python (prefereably golang)
2. Coding up a loop that will for 000000 to 999999 and break out when correct combination is found
    - Submit possible combination


### Pseudo-code: ###
```
create variable "guess" == 000000

while guess != 999999:
    ++guess
    submit guess

    if submission == valid:
        exit
```
## ==============GOLANG============== ##
### THOUGHT PROCESS ###
1. Make an http GET request to website to check on endpoint
2. Loop will go through the million possibilities to find the verification code. 
    - Within the loop, we make new requests to the http to check. We use this request to check if we recieve a status code "200 OK"

**Referenced:** https://pkg.go.dev/net/http



## ==============PYTHON============== ##
**Tools:** Selenium & openpyxl

SELENIUM == Task is to open web page, retrieve the relevant html and populate needed information. Web scraping tool.

**REQUIREMENTS**
- Python 3.9
- pip

**SETUP**
1. Install selenium ```pip install selenium``` or ```pip3 install selenium```
2. Run the code ```pip install selenium```
3. Install the Google Chrome and the corresponding webdriver (https://chromedriver.chromium.org/downloads)
4. Place webdriver wherever you please on your machine. Once placed, copy the path that contains the webdriver.
5. On the file **verify_script.py** , paste the path of the webdriver onto ```PATH:``` 
<!-- 5. Insert the website you would like to utilize this tool on -->


openpyxl == Works with exel sheet to keep track of possible solutions(??)

https://stackoverflow.com/questions/50487345/write-a-auto-fill-and-submit-web-form-program
