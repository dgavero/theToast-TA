import time

from page_objects.base_page import base_page


class login_page(base_page):

    def __init__(self, driver):
        super().__init__(driver)

    def merchantLogin(self, username, password):
        self.type("login_usernamefield_ID", username)
        self.type("login_passwordfield_ID", password)
        self.click("login_submitBTN_ID")
        self.click("yourlisting_title_XPATH")

        # expected_text = "Dashboard"
        # actual_text = self.getText("dashboard_title_XPATH")
        # assert actual_text == expected_text, f"Failed Login - Expected '{expected_text}' but got '{actual_text}"

