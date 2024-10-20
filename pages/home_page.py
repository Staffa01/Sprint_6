from .base_page import BasePage
from selenium.webdriver.common.by import By
import allure
from data import Url

class HomePage(BasePage):
    ACCORDION_ID = 'accordion__heading-'
    ACCORDION_EXPAND = 'accordion__panel-'
    ACCORDION_LOKATOR_ID = None
    ACCORDION_LOKATOR_EXPAND = None
    @allure.step('Создание локатора выпадашки')
    def genrate_accordion_locators(self, accordion_index):
        self.ACCORDION_LOKATOR_ID = (By.ID, f"{self.ACCORDION_ID}{accordion_index}")
        self.ACCORDION_LOKATOR_EXPAND = (By.XPATH, f".//div[@id='{self.ACCORDION_EXPAND}{accordion_index}']/p") 
    
    @allure.step('Открытие главной страницы')
    def open_home_page(self):
        self.open_page(Url.base_url)

    @allure.step('Скролл до выпадашки')
    def scroll_to_accordion(self):
        self.scroll_to_element(self.ACCORDION_LOKATOR_ID)

    @allure.step('Нажатие на выпадашку')
    def click_to_accordion(self):
        self.click_to_element(self.ACCORDION_LOKATOR_ID)

    @allure.step('Получение значения атрибута aria-expanded')
    def get_accordion_expanded_value(self):
        return self.get_attribute_value(self.ACCORDION_LOKATOR_ID, 'aria-expanded')
    
    @allure.step('Получение текста выпадашки')
    def get_expanded_accordion_text(self):
        return self.get_text_element_with_wait(self.ACCORDION_LOKATOR_EXPAND)
        
    
    