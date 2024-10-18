from .base_page import BasePage
from selenium.webdriver.common.by import By
import allure

class HomePage(BasePage):
    ACCORDION_ID = 'accordion__heading-'
    ACCORDION_EXPAND = 'accordion__panel-'
    @allure.step('Создание локатора выпадашки')
    def genrate_accordion_locators(self, accordion_index):
        accordion_locator_id =(By.ID, f"{self.ACCORDION_ID}{accordion_index}")
        accordion_locator_text = (By.XPATH, f".//div[@id='{self.ACCORDION_EXPAND}{accordion_index}']/p") 
        return accordion_locator_id, accordion_locator_text
    
    