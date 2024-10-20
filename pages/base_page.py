
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(locator))
        return self.driver.find_element(*locator)
    
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator))
        self.driver.find_element(*locator).click()
    
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_attribute_value(self, locator, attribute):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(locator))
        return element.get_attribute(attribute)
    
    def get_text_element_with_wait(self, locator):
        element = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(locator))
        return element.text
    
    def send_keys_to_element(self, locator, keys):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator))
        self.driver.find_element(*locator).send_keys(keys)

    def set_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
    
    def chec_new_page_open_with_wait(self, url):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.url_to_be(url))
    