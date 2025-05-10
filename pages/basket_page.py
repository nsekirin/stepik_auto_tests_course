from selenium.common import NoSuchElementException

from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket is not empty, but should be"

    def should_be_text_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), \
            "There is no text about empty basket"

    def is_not_element_present(self, how, what, timeout=4):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return True
        return False

    def is_element_present(self, how, what, timeout=4):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
