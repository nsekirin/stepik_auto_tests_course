from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert "login" in current_url, f"Current URL '{current_url}' does not contain 'login'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        confirm_password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)

        email_field.send_keys(email)
        password_field.send_keys(password)
        confirm_password_field.send_keys(password)
        register_button.click()

