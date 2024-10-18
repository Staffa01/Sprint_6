
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        # self.timeout = 10

    @allure.step('Отрытие страницы {url}')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Поиск элемента {locator}')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(locator))
        return self.driver.find_element(*locator)
    
    @allure.step('Клик по элементу {locator}')
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator))
        self.driver.find_element(*locator).click()
    
    @allure.step('Скролл до элемента {locator}')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Получение атрибута {attribute} элемента {locator}')
    def get_attribute_value(self, locator, attribute):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(locator))
        # element = self.driver.find_element(locator)
        return element.get_attribute(attribute)
    
    @allure.step('Получение текста элемента {locator}')
    def get_text_element_with_wait(self, locator):
        print(locator)
        element = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(locator))
        return element.text
    
    @allure.step('Ввод текста {keys} в элемент {locator}')
    def send_keys_to_element(self, locator, keys):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator))
        self.driver.find_element(*locator).send_keys(keys)

    @allure.step('Переход на вторую вкладку')
    def set_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
    