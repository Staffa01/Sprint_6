import pytest
from selenium import webdriver
from pages.home_page import HomePage
from data import Questions
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
        home_page.open_home_page()
        home_page.genrate_accordion_locators(accordion_index)
        home_page.scroll_to_accordion()
        home_page.click_to_accordion()
        assert home_page.get_accordion_expanded_value() == 'true'
        assert home_page.get_expanded_accordion_text() == Questions.question[accordion_index]
        
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()