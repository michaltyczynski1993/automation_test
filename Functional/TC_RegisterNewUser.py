from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support import expected_conditions as EC
import testData
from selenium.webdriver.chrome.service import Service
from Functional import generator as g
import time


class RegisterUser(unittest.TestCase):
    def setUp(self):
        self.ser = Service("C:\TestFiles\chromedriver.exe")
        self.op = webdriver.ChromeOptions()
        self.prefs = {"profile.default_content_setting_values.notifications": 2}
        self.op.add_experimental_option("prefs", self.prefs)
        self.driver = webdriver.Chrome(service=self.ser, options=self.op)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def test_registerNewUser(self):
        # go to main page
        self.driver.get("https://www.interia.pl/")
        # close pop up rodo
        popUpBttn = self.driver.find_element(By.CLASS_NAME, "rodo-popup-agree")
        popUpBttn.click()
        # click login page link
        self.driver.find_element(By.XPATH, "//*[@class = 'switch-mail']").click()
        # click restister button
        self.driver.find_element(By.XPATH, "//*[@class = 'btn btn--bordered']").click()
        # when user is on site 'załóż konto' click on correct 'wybieram' button
        if self.driver.title == "Załóż konto pocztowe – Poczta w Interia – rejestracja konta email":
            self.driver.find_element(By.XPATH,
                                     "//*[@id='mainApp']/div/div/div/div/div[2]/div/div/div[1]/a/button").click()
        # set name text field
        name = self.driver.find_element(By.XPATH, "//div[@class = 'register-form__inputs']/div[1]/input")
        newName = g.name_generator()
        name.send_keys(newName)
        # set surname text field
        surname = self.driver.find_element(By.XPATH, "//div[@class = 'register-form__inputs']/div[2]/input")
        newSurname = g.last_name_generator()
        surname.send_keys(newSurname)
        # set birth date
        birthDay = self.driver.find_element(By.XPATH, "//div[@class = 'register-form__inputs__birthday']/div[1]/input")
        birthDay.send_keys("10")
        birthMonth = self.driver.find_element(By.XPATH,
                                              "//div[@class = 'register-form__inputs__birthday']/div[2]/div[2]").click()
        act = ActionChains(self.driver)
        act.send_keys(Keys.ARROW_DOWN).perform()
        act.send_keys(Keys.ENTER).perform()
        birthYear = self.driver.find_element(By.NAME, "birthdayYear")
        birthYear.send_keys("1990")
        genderArrowbttn = self.driver.find_element(By.XPATH, "//div[@class = 'register-form__inputs']/div[4]/div[2]")
        genderArrowbttn.click()
        act.send_keys(Keys.ARROW_DOWN).perform()
        act.send_keys(Keys.ENTER).perform()
        act.send_keys(Keys.TAB).perform()
        # enter username and password
        userName = self.driver.find_element(By.XPATH,
                                            "/html/body/div[1]/div/div/div/div/div[2]/div/form/div[1]/div[5]/div[1]/input")
        newUsername = "a" + g.user_generator()
        userName.send_keys(newUsername)
        loginU = userName.get_attribute('value')
        time.sleep(2)
        password = self.driver.find_element(By.XPATH, "//*[@id='password']")
        newPassword = g.password_generator()
        password.send_keys(newPassword)
        rePassword = self.driver.find_element(By.XPATH, "//*[@id='rePassword']")
        rePassword.send_keys(newPassword)
        # click checkbox for policies
        self.driver.find_element(By.XPATH, "//*[@class = 'checkbox-wrapper']/div").click()
        self.driver.find_element(By.XPATH,
                                 "//*[@class = 'agreements-container agreements-container--expanded']/div[1]").click()
        self.driver.find_element(By.XPATH,
                                 "//*[@class = 'agreements-container agreements-container--expanded']/div[2]").click()
        self.driver.find_element(By.XPATH,
                                 "//*[@class = 'agreements-container agreements-container--expanded']/div[3]").click()
        self.driver.find_element(By.XPATH,
                                 "//*[@class = 'agreements-container agreements-container--expanded']/div[4]").click()
        time.sleep(2)
        # click create account button
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class = 'btn']"))).click()
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//div[@class = 'msglist-item__message'][1]/div[@class = 'msglist-item__link']"
                                        ))).click()
        # print welcome message
        text = self.driver.find_element(By.XPATH, "//*[@class = 'message-header__subject']/span").text
        print("Twoja wiadomość powitalna to:", text)
        self.driver.quit()
        testData.username = loginU
        testData.password = newPassword
        print(newName)
        print(newSurname)
        print(newPassword)
        print("Login :", testData.username)
        print("Hasło: ", testData.password)


if __name__ == '__main__':
    loader = unittest.TestLoader()
    loader.sortTestMethodsUsing = None
    unittest.main(testLoader=loader)
