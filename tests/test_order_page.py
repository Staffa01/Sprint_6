import pytest
from selenium import webdriver
import allure
from pages.order_page import OrderPage
from data import Url, UserData


class TestOrderPage:
    driver = None
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Тест оформления самоката')
    @pytest.mark.parametrize('button_locator, user_data',[
        [OrderPage.ORDER_BUTTON_HEADER, UserData.first_user],
        [OrderPage.ORDER_BUTTON_FOOTER, UserData.second_user]
        ])

    def test_order_scooter(self,button_locator,user_data):
        order_page = OrderPage(self.driver)
        order_page.open_page(Url.base_url)
        order_page.scroll_to_element(button_locator)
        order_page.click_to_element(button_locator)
        order_page.check_current_url_with_wait(Url.order_url)
        order_page.fill_order_forms(user_data)
        order_page.click_to_element(OrderPage.ORDER_NEXT_BUTTON)
        order_page.fill_rent_form(user_data)
        order_page.click_to_element(OrderPage.ORDER_CONFIRM_BUTTON)
        order_page.click_to_element(OrderPage.ORDER_YES_BUTTON)
        order_page.find_element_with_wait(OrderPage.ORDER_CONFIRM_MODAL)
        assert order_page.find_element_with_wait(OrderPage.ORDER_CONFIRM_MODAL).is_displayed() == True

    @allure.title('Тест перехода по нажатию на логотиплого самоката')
    def test_scooter_logo(self):
        order_page = OrderPage(self.driver)
        order_page.open_page(Url.order_url)
        order_page.click_to_element(OrderPage.ORDER_SCOOTER_LOGO)
        order_page.check_current_url_with_wait(Url.base_url)
        assert self.driver.current_url == Url.base_url

    @allure.title('Тест перехода по нажатию на логотип Яндекса')
    def test_yandex_logo(self):
        order_page = OrderPage(self.driver)
        order_page.open_page(Url.order_url)
        order_page.click_to_element(OrderPage.ORDER_YANDEX_LOGO)
        order_page.set_next_tab()
        order_page.check_current_url_with_wait(Url.dzen_url)
        assert self.driver.current_url == Url.dzen_url

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
        

