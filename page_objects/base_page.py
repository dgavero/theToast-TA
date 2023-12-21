import logging
from selenium.webdriver.support.wait import WebDriverWait
from page_utilities.LogUtil import Logger
from page_utilities import configReader
from selenium.webdriver.common.by import By
from telnetlib3 import EC
from selenium.webdriver.support import expected_conditions as EC



log = Logger(__name__, logging.INFO)


class base_page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def click(self, locator):
        xpath_click_locator = configReader.readConfig("locators", locator)
        id_click_locator = configReader.readConfig("locators", locator)
        name_click_locator = configReader.readConfig("locators", locator)

        if str(locator).endswith("_XPATH"):
            self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath_click_locator)))
            self.driver.find_element(By.XPATH, xpath_click_locator).click()
        elif str(locator).endswith("_ID"):
            self.wait.until(EC.visibility_of_element_located((By.ID, id_click_locator)))
            self.driver.find_element(By.ID, id_click_locator).click()
        elif str(locator).endswith("_NAME"):
            self.wait.until(EC.visibility_of_element_located((By.NAME, name_click_locator)))
            self.driver.find_element(By.NAME, name_click_locator).click()
        log.logger.info("Clicking on an Element " + str(locator))

    def type(self, locator, value):
        xpath_type_locator = configReader.readConfig("locators", locator)
        id_type_locator = configReader.readConfig("locators", locator)
        name_type_locator = configReader.readConfig("locators", locator)

        if str(locator).endswith("_XPATH"):
            self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath_type_locator)))
            self.driver.find_element(By.XPATH, xpath_type_locator).send_keys(value)
        elif str(locator).endswith("_ID"):
            self.wait.until(EC.visibility_of_element_located((By.ID, id_type_locator)))
            self.driver.find_element(By.ID, id_type_locator).send_keys(value)
        elif str(locator).endswith("_NAME"):
            self.wait.until(EC.visibility_of_element_located((By.NAME, name_type_locator)))
            self.driver.find_element(By.NAME, name_type_locator).send_keys(value)
        log.logger.info("Clicking on an Element " + str(locator))

    def getText(self, locator):
        xpath_text_locator = configReader.readConfig("locators", locator)
        id_text_locator = configReader.readConfig("locators", locator)
        name_text_locator = configReader.readConfig("locators", locator)
        text = None

        if str(locator).endswith("_XPATH"):
            self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath_text_locator)))
            text = self.driver.find_element(By.XPATH, xpath_text_locator).text
        elif str(locator).endswith("_ID"):
            self.wait.until(EC.visibility_of_element_located((By.ID, id_text_locator)))
            text = self.driver.find_element(By.ID, id_text_locator).text
        elif str(locator).endswith("_NAME"):
            self.wait.until(EC.visibility_of_element_located((By.NAME, name_text_locator)))
            text = self.driver.find_element(By.NAME, name_text_locator).text
        log.logger.info("Getting text from an Element " + str(locator))
        return text
