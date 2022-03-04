import unittest
from crawler import InteriaCrawler

class RegisterUser(unittest.TestCase):
    def setUp(self):
        self.crawler = InteriaCrawler()

    def test_registerNewUser(self):
        self.crawler.go_to_main()
        self.crawler.close_rodo_popup()
        self.crawler.loginpage_link()
        self.crawler.register_button()
        self.crawler.choose_register_option()
        self.crawler.fill_register_form()
        self.crawler.print_welcome_msg_title()


if __name__ == '__main__':
    loader = unittest.TestLoader()
    loader.sortTestMethodsUsing = None
    unittest.main(testLoader=loader)
