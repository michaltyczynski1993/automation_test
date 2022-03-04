from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support import expected_conditions as EC
import testData
from selenium.webdriver.chrome.service import Service
import locators

class UserLogin(unittest.TestCase):

    def setUp(self):
        self.ser = Service("C:\TestFiles\chromedriver.exe")
        self.op = webdriver.ChromeOptions()
        self.prefs = {"profile.default_content_setting_values.notifications": 2}
        self.op.add_experimental_option("prefs", self.prefs)
        self.driver = webdriver.Chrome(service=self.ser, options=self.op)
        self.driver.implicitly_wait(30)
        if not testData.username:
            self.userName = "aWISshNhvGbxM3rI@interia.pl"
        else:
            self.userName = testData.username
        if not testData.password:
            self.password = "baA3kDa08lVEO3H0ZHrh"
        else:
            self.password = testData.password
        self.driver.get("https://poczta.interia.pl/logowanie/#iwa_source=sg_ikona")

    def tearDown(self):
        self.driver.quit()

    def test_validLogin(self):
        # close pop up
        locators.closeRodo(self.driver)
        # enter user name and password
        userField = self.driver.find_element(By.XPATH, "//input[@class = 'account-input' and @name = 'email']")
        userField.send_keys(self.userName)
        passwordField = self.driver.find_element(By.XPATH, "//input[@class = 'account-input' and @name = 'password']")
        passwordField.send_keys(self.password)
        # click submit button
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[text() = 'Zaloguj się']"))).click()
        print("Pozytywne Logowanie do konta na Interia.pl: ", self.driver.title == "Poczta w Interii")
        assert self.driver.title == "Poczta w Interii"


    def test_invalidLogin(self):
        # close pop up
        locator.closeRodo(self.driver)
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


if __name__ == '__main__':
    unittest.main()
