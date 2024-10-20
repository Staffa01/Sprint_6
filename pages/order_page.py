from .base_page import BasePage
from data import Url
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
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

    @allure.step('Ожидание перехода на страницу оформления заказа')
    def check_open_order_url_with_wait(self):
        self.chec_new_page_open_with_wait(Url.order_url)

    @allure.step('Заполнение станции метро в форме заказа')
    def fill_station_form(self):
        self.click_to_element(self.USER_STATION)
        self.click_to_element(self.USER_STATION_EXPAND_BUTTON)
        
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

    @allure.step('Нажатие на кнопку "Далее"')
    def click_to_order_next_button(self):
        self.click_to_element(self.ORDER_NEXT_BUTTON)

    @allure.step('Нажатие на кнопку "Заказать" в экране аренды')
    def click_to_order_confirm_button(self):
        self.click_to_element(self.ORDER_CONFIRM_BUTTON)
    
    @allure.step('Нажатие на кнопку "Да"')
    def click_to_order_yes_button(self):
        self.click_to_element(self.ORDER_YES_BUTTON)

    @allure.step('Проверка открытия окна подтверждение заказа')
    def find_confirm_modal(self):
        element = self.find_element_with_wait(self.ORDER_CONFIRM_MODAL)
        return element.is_displayed()
    
    @allure.step('Ожидание перехода на главную страницу')
    def check_open_home_url_with_wait(self):
        return self.chec_new_page_open_with_wait(Url.base_url)
    
    @allure.step('Ожидание перехода на страницу Дзена')
    def check_open_dzen_url_with_wait(self):
        return self.chec_new_page_open_with_wait(Url.dzen_url)

    @allure.step('Открытие страницы заказа')
    def open_order_page(self):
        self.open_page(Url.order_url)

    @allure.step('Открытие главной страницы')
    def open_home_page(self):
        self.open_page(Url.base_url)

    @allure.step('Нажатие на логотип Самокат')
    def click_scooter_logo(self):
        self.click_to_element(self.ORDER_SCOOTER_LOGO)

    @allure.step('Нажатие на логотип Яндекс')
    def click_jandex_logo(self):
        self.click_to_element(self.ORDER_YANDEX_LOGO)