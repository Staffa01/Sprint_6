from .base_page import BasePage
from data import Url
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure
import allure

class OrderPage(BasePage):
    ORDER_BUTTON_HEADER = By.XPATH, "//div[contains(@class,'Header_Nav')]/button[text()='Заказать']"
    ORDER_BUTTON_FOOTER = By.XPATH, ("//div[contains(@class,'Home_FinishButton')]/button[text()='Заказать']")
    USER_NAME = (By.XPATH, ".//input[@placeholder='* Имя']")
    USER_SURNAME = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    USER_ADDRESS = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    USER_STATION = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    USER_PHONE = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    USER_STATION_EXPAND_BUTTON = (By.XPATH, "//button[@value='1']")
    ORDER_NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']")
    ORDER_DATE = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    ORDER_DATE_CALENDAR = (By.XPATH,"//div[contains(@class,'keyboard-selected')]")
    ORDER_RENT = (By.XPATH, ".//div[text()='* Срок аренды']")
    ORDER_RENT_DROPDOWN = (By.XPATH, ".//div[@class = 'Dropdown-menu']/div[text() ='сутки']")
    ORDER_COLOR = (By.XPATH, ".//input[@id='grey']")
    ORDER_COMMENT = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    ORDER_CONFIRM_BUTTON = (By.XPATH, "//button[contains(@class,'Button_Middle')and text()='Заказать']")
    ORDER_CONFIRM_MODAL = (By.XPATH, ".//div[contains(@class, 'Order_ModalHeader')]")
    ORDER_YES_BUTTON = (By.XPATH, ".//button[text()='Да']")
    ORDER_YANDEX_LOGO = (By.XPATH, "//a[contains(@class,'Header_LogoYandex')]")
    ORDER_SCOOTER_LOGO = (By.XPATH, "//a[contains(@class,'Header_LogoScooter')]")

    @allure.step('Ожидание перехода на новую страницу')
    def check_current_url_with_wait(self, url):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.url_to_be(url))

    @allure.step('Заполнение станции метро в форме заказа')
    def fill_station_form(self):
        self.driver.find_element(*self.USER_STATION).click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.USER_STATION_EXPAND_BUTTON))
        self.driver.find_element(*self.USER_STATION_EXPAND_BUTTON).click()    
        
    @allure.step('Заполнение формы заказа')    
    def fill_order_forms(self, user_data):
        self.send_keys_to_element(self.USER_NAME, user_data['USER_NAME'])
        self.send_keys_to_element(self.USER_SURNAME, user_data['USER_SURNAME'])
        self.send_keys_to_element(self.USER_ADDRESS, user_data['USER_ADDRESS'])
        self.fill_station_form()
        self.send_keys_to_element(self.USER_PHONE, user_data['USER_PHONE'])

    @allure.step('Заполнение формы аренды')
    def fill_rent_form(self, user_data):
        self.click_to_element(self.ORDER_DATE)
        self.click_to_element(self.ORDER_DATE_CALENDAR)
        self.click_to_element(self.ORDER_RENT)
        self.click_to_element(self.ORDER_RENT_DROPDOWN)
        self.click_to_element(self.ORDER_COLOR)
        self.send_keys_to_element(self.ORDER_COMMENT, user_data['USER_COMENT'])

        
