import unittest
import testData
from crawler import InteriaCrawler

class UserLogin(unittest.TestCase):

    def setUp(self):
        if not testData.username:
            self.user_name = "aWISshNhvGbxM3rI@interia.pl"
        else:
            self.user_name = testData.username
        if not testData.password:
            self.password = "baA3kDa08lVEO3H0ZHrh"
        else:
            self.password = testData.password
        self.crawler = InteriaCrawler()

    def tearDown(self):
        self.crawler.driver.quit()

    def test_validLogin(self):
        self.crawler.go_to_login_page()
        self.crawler.close_rodo_popup()
        self.crawler.interia_login(self.user_name, self.password)
        print("Pozytywne Logowanie do konta na Interia.pl: ", self.crawler.driver.title == "Poczta w Interii")
        assert self.crawler.driver.title == "Poczta w Interii"


    def test_invalidLogin(self):
        self.crawler.go_to_login_page()
        self.crawler.close_rodo_popup()
        self.crawler.interia_login(self.user_name, self.password + str(123))
        print("Negatywne Logowanie do konta na Interia.pl: ", self.crawler.driver.title != "Poczta w Interii")
        assert self.crawler.driver.title != "Poczta w Interii"


if __name__ == '__main__':
    unittest.main()
