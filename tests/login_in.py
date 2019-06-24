import unittest
from selenium import webdriver
from pages.header import Header
from pages.log_in import LogIn
from locators import urls

import time


class LoginInTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        #options.add_argument('headless')
        options.add_argument('incoginito')
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get(urls.home_page)

    def test_login_in(self):
        x = Header(self.driver)
        x.click_sign_in()
        LogIn(self.driver).log_in()
        user_name = Header(self.driver).get_user_name()
        current_url = Header(self.driver).get_current_url()
        self.assertEqual(user_name, "Test Test")
        self.assertEqual(current_url, urls.my_account)

    def test_login_in_incorrect_email(self):
        x = Header(self.driver)
        x.click_sign_in()
        LogIn(self.driver)

    def tearDown(self):
        self.driver.close()

    if __name__ == '__main__':
        unittest.main()
