import pytest
from selenium import webdriver
from pages.home_page import HomePage
from data import Url, Questions
import allure


class TestHomePage:
    driver = None
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    index = ['0','1','2','3','4','5','6','7']
    @allure.title('Проверка выпадашек в разделе "Вопросы о важном"')
    @pytest.mark.parametrize('accordion_index', index)
    def test_home_page_accordion_buttons_expand(self, accordion_index):
        home_page = HomePage(self.driver)
        home_page.open_page(Url.base_url)
        accordion_locator_id, accordion_locator_text = home_page.genrate_accordion_locators(accordion_index)
        home_page.scroll_to_element(accordion_locator_id)
        home_page.click_to_element(accordion_locator_id)
        attribute_element = home_page.get_attribute_value(accordion_locator_id, 'aria-expanded')
        assert attribute_element == 'true'
        text_element = home_page.get_text_element_with_wait(accordion_locator_text)
        assert text_element == Questions.question[accordion_index]
        

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()