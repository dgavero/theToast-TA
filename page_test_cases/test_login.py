import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import pytest
from page_objects.login_page import login_page
from page_test_cases.base_tests import base_tests


class Test_MerchantLogin(base_tests):

    @pytest.mark.parametrize("username, password", [
        ("batman2023@yopmail.com", "Diluc123456789!"),
        #("user2", "password2"),
    ])
    def test_merchantLogins(self, username, password):
        login = login_page(self.driver)
        login.merchantLogin(username, password)

        expected_text = "Dashboard"
        actual_text = login.getText("dashboard_title_XPATH")
        assert actual_text == expected_text, f"Failed Login - Expected '{expected_text}' but got '{actual_text}"


