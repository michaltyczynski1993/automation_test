from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import locators
from Functional import generator as g
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import testData

class Crawler(object):

    def __init__(self):
        self.options = Options()
        self.driver = webdriver.Chrome(service=Service('C:\TestFiles\chromedriver.exe'), options=self.options)
        self.driver.implicitly_wait(30)


class InteriaCrawler(Crawler):

    def go_to_main(self):
        """ go to main page """
        self.driver.get("https://www.interia.pl/")

    def close_rodo_popup(self):
        """ close rodo popup for firts time visitors """
        pop_up_bttn = self.driver.find_element(*locators.RODO_POPUP)
        pop_up_bttn.click()

    def loginpage_link(self):
        login_link = self.driver.find_element(*locators.LOGINPAGE_LINK)
        login_link.click()

    def register_button(self):
        register_button = self.driver.find_element(*locators.REGISTER_BUTTON)
        register_button.click()

    def choose_register_option(self):
        """ choose free account option """
        if self.driver.title == "Załóż konto pocztowe – Poczta w Interia – rejestracja konta email":
            choose_button = self.driver.find_element(*locators.REGISTER_OPTION)
            choose_button.click()

    def fill_register_form(self):
        # set name text field
        name = self.driver.find_element(*locators.NAME)
        new_name = g.name_generator()
        name.send_keys(new_name)

        # set surname text field
        surname = self.driver.find_element(*locators.SURNAME)
        new_surname = g.last_name_generator()
        surname.send_keys(new_surname)

        # set birth date
        birth_day = self.driver.find_element(*locators.BIRTHDAY)
        birth_day.send_keys("10")
        birth_month = self.driver.find_element(*locators.BIRTH_MONTH).click()
        act = ActionChains(self.driver)
        act.send_keys(Keys.ARROW_DOWN).perform()
        act.send_keys(Keys.ENTER).perform()
        birth_year = self.driver.find_element(*locators.BIRTH_YEAR)
        birth_year.send_keys("1990")
        gender_arrowbttn = self.driver.find_element(*locators.GENDER_ARROW_BTTN)
        gender_arrowbttn.click()
        act.send_keys(Keys.ARROW_DOWN).perform()
        act.send_keys(Keys.ENTER).perform()
        act.send_keys(Keys.TAB).perform()

        # enter username and password
        user_name = self.driver.find_element(*locators.USERNAME)
        newUsername = "a" + g.user_generator()
        user_name.send_keys(newUsername)
        loginU = user_name.get_attribute('value')
        testData.username = loginU
        time.sleep(2)
        password = self.driver.find_element(*locators.PASSWORD)
        newPassword = g.password_generator()
        testData.password = newPassword
        password.send_keys(newPassword)
        rePassword = self.driver.find_element(*locators.REPASSWORD)
        rePassword.send_keys(newPassword)

        # click checkbox for policies
        self.driver.find_element(*locators.POLICY_WRAPPER).click()
        self.driver.find_element(*locators.POLICY_CHECK1).click()
        self.driver.find_element(*locators.POLICY_CHECK2).click()
        self.driver.find_element(*locators.POLICY_CHECK3).click()
        self.driver.find_element(*locators.POLICY_CHECK4).click()
        time.sleep(2)
        # click create account button
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locators.CREATE_ACCOUNT_BUTTON)).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locators.RECAPTCHA)).click()

    def print_welcome_msg_title(self):
        """ print first message title from mailbox and login data """
        text = self.driver.find_element(*locators.TITLE).text
        print("Twoja wiadomość powitalna to:", text)
        self.driver.quit()
        print("Login :", testData.username)
        print("Hasło: ", testData.password)

    def interia_login(self, username, password):
        # enter user data like username and login
        username_field = self.driver.find_element(*locators.LOGIN_USERNAME)
        username_field.send_keys(username)
        password_field = self.driver.find_element(*locators.LOGIN_PASSWORD)
        password_field.send_keys(password)
        # click submit button
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locators.LOGIN_SUBMIT_BTTN)).click()

    def go_to_login_page(self):
        self.driver.get("https://poczta.interia.pl/logowanie/#iwa_source=sg_ikona")