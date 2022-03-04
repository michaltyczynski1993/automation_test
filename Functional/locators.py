from selenium.webdriver.common.by import By
# main site
RODO_POPUP = (By.CLASS_NAME, "rodo-popup-agree")
LOGINPAGE_LINK = (By.XPATH, "//*[@class = 'switch-mail']")

# login page
REGISTER_BUTTON = (By.XPATH, "//*[@class = 'btn btn--bordered']")

# register option site
REGISTER_OPTION = (By.XPATH, "//a[contains(@href, '#/nowe-konto')]/button[1]")

# register form fields
NAME = (By.XPATH, "//div[@class = 'register-form__inputs']/div[1]/input")
SURNAME = (By.XPATH, "//div[@class = 'register-form__inputs']/div[2]/input")
BIRTHDAY = (By.XPATH, "//div[@class = 'register-form__inputs__birthday']/div[1]/input")
BIRTH_MONTH = (By.XPATH, "//div[@class = 'register-form__inputs__birthday']/div[2]/div[2]")
BIRTH_YEAR = (By.NAME, "birthdayYear")
GENDER_ARROW_BTTN = (By.XPATH, "//div[@class = 'register-form__inputs']/div[4]/div[2]")
USERNAME = (By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div/form/div[1]/div[5]/div[""1]/input")
PASSWORD = (By.XPATH, "//*[@id='password']")
REPASSWORD = (By.XPATH, "//*[@id='rePassword']")

# Policy CheckBoxes
POLICY_WRAPPER = (By.XPATH, "//*[@class = 'checkbox-wrapper']/div")
POLICY_CHECK1 = (By.XPATH, "//*[@class = 'agreements-container agreements-container--expanded']/div[1]")
POLICY_CHECK2 = (By.XPATH, "//*[@class = 'agreements-container agreements-container--expanded']/div[2]")
POLICY_CHECK3 = (By.XPATH, "//*[@class = 'agreements-container agreements-container--expanded']/div[3]")
POLICY_CHECK4 = (By.XPATH, "//*[@class = 'agreements-container agreements-container--expanded']/div[4]")
CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[@class = 'btn']")
RECAPTCHA = (By.XPATH, "//div[@class = 'msglist-item__message'][1]/div[@class = 'msglist-item__link']")

# Mailbox
TITLE = (By.XPATH, "//*[@class = 'message-header__subject']/span")