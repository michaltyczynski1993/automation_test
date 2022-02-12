import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support import expected_conditions as EC
import testData
from selenium.webdriver.chrome.service import Service

class UserLogin(unittest.TestCase):

    def setUp(self):
        self.ser = Service("C:\TestFiles\chromedriver.exe")
        self.op = webdriver.ChromeOptions()
        self.prefs = {"profile.default_content_setting_values.notifications": 2}
        self.op.add_experimental_option("prefs", self.prefs)
        self.driver = webdriver.Chrome(service = self.ser, options = self.op)
        self.driver.implicitly_wait(30)
        if not testData.username:
            self.userName = "aWISshNhvGbxM3rI@interia.pl"
        else:
            self.userName = testData.username
        if not testData.username:
            self.password = "baA3kDa08lVEO3H0ZHrh"
        else:
            self.password = testData.password
        self.driver.get("https://poczta.interia.pl/logowanie/#iwa_source=sg_ikona")

    def tearDown(self):
        self.driver.quit()

    def test_validLogin(self):
        #close pop up
        popUpBttn = self.driver.find_element(By.CLASS_NAME, "rodo-popup-agree")
        popUpBttn.click()
        #enter user name and password
        userField = self.driver.find_element(By.XPATH, "//input[@class = 'account-input' and @name = 'email']")
        userField.send_keys(self.userName)
        passwordField = self.driver.find_element(By.XPATH, "//input[@class = 'account-input' and @name = 'password']")
        passwordField.send_keys(self.password)
        #click submit button
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[text() = 'Zaloguj się']"))).click()
        print("Pozytywne Logowanie do konta na Interia.pl: ", self.driver.title == "Poczta w Interii")
        assert self.driver.title == "Poczta w Interii"

    def test_invalidLogin(self):
        # close pop up
        popUpBttn = self.driver.find_element(By.CLASS_NAME, "rodo-popup-agree")
        popUpBttn.click()
        # enter user name and password
        userField = self.driver.find_element(By.XPATH, "//input[@class = 'account-input' and @name = 'email']")
        userField.send_keys(self.userName)
        passwordField = self.driver.find_element(By.XPATH, "//input[@class = 'account-input' and @name = 'password']")
        passwordField.send_keys(self.password+str(123))
        # click submit button
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[text() = 'Zaloguj się']"))).click()
        print("Negatywne Logowanie do konta na Interia.pl: ", self.driver.title != "Poczta w Interii")
        assert self.driver.title != "Poczta w Interii"
    # def test_printFirstMessage(self):
    #     # close pop up
    #     popUpBttn = self.driver.find_element(By.CLASS_NAME, "rodo-popup-agree")
    #     popUpBttn.click()
    #     # enter user name and password
    #     userField = self.driver.find_element(By.XPATH, "//input[@class = 'account-input' and @name = 'email']")
    #     userField.send_keys(self.userName)
    #     passwordField = self.driver.find_element(By.XPATH, "//input[@class = 'account-input' and @name = 'password']")
    #     passwordField.send_keys(self.password)
    #     # click submit button
    #     WebDriverWait(self.driver, 20).until(
    #         EC.element_to_be_clickable((By.XPATH, "//*[text() = 'Zaloguj się']"))).click()
    #     print("Pozytywne logowanie w celu pozyskania wiadomości: ", self.driver.title == "Poczta w Interii")
    #     assert self.driver.title == "Poczta w Interii"
    #     time.sleep(5)
    #     WebDriverWait(self.driver, 20).until(
    #         EC.element_to_be_clickable((By.XPATH, "//div[@class = 'msglist-item__message'][1]/div[@class = 'msglist-item__link']"))).click()
    #     text = self.driver.find_element(By.XPATH, "//*[@class = 'message-header__subject']/span").text
    #     print(text)
if __name__ == '__main__':
    unittest.main()