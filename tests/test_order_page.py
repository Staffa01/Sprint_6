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
        order_page.open_home_page()
        order_page.scroll_to_element(button_locator)
        order_page.click_to_element(button_locator)
        order_page.check_open_order_url_with_wait()
        order_page.fill_order_forms(user_data)
        order_page.click_to_order_next_button()
        order_page.fill_rent_form(user_data)
        order_page.click_to_order_confirm_button()
        order_page.click_to_order_yes_button()
        assert order_page.find_confirm_modal() == True

    @allure.title('Тест перехода по нажатию на логотиплого самоката')
    def test_scooter_logo(self):
        order_page = OrderPage(self.driver)
        order_page.open_order_page()
        order_page.click_scooter_logo()
        assert order_page.check_open_home_url_with_wait() == True

    @allure.title('Тест перехода по нажатию на логотип Яндекса')
    def test_yandex_logo(self):
        order_page = OrderPage(self.driver)
        order_page.open_order_page()
        order_page.click_jandex_logo()
        order_page.set_next_tab()
        assert order_page.check_open_dzen_url_with_wait() == True

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
        

