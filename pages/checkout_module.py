import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CheckModule:
    def __init__(self,driver):
        self.driver = driver


    def get_cart_badge_number(self):
        try:
            cart_badge_element_number = self.driver.find_element(By.CSS_SELECTOR,"[data-test='shopping-cart-badge']").text
        except:
            cart_badge_element_number = 0
        return int(cart_badge_element_number)


    def get_checkout_page(self):
        cart_badge_element_number = self.get_cart_badge_number()
        while int(cart_badge_element_number) == 0:
            self.driver.find_element(By.CLASS_NAME, "btn_primary").click()
            cart_badge_element_number = self.get_cart_badge_number()
        self.driver.find_element(By.CSS_SELECTOR,"[data-test='shopping-cart-link']").click()
        self.driver.find_element(By.CSS_SELECTOR,"[data-test='checkout']").click()
        current_url = self.driver.current_url
        return current_url


    def fill_the_form(self, username, lastname, postalcode):
        self.get_checkout_page()
        self.driver.find_element(By.CSS_SELECTOR,"[data-test='firstName']").send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR,"[data-test='lastName']").send_keys(lastname)
        self.driver.find_element(By.CSS_SELECTOR,"[data-test='postalCode']").send_keys(postalcode)
        self.driver.find_element(By.CSS_SELECTOR,"[data-test='continue']").click()
        try:
            current_error = self.driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
        except:
            current_error = "None"
        current_url = self.driver.current_url
        return current_url, current_error


    def cart_overview(self):
        info_list = []
        try:
            cart_details = self.driver.find_elements(By.CLASS_NAME,"summary_info")
            for detail in cart_details:
                info = detail.text
                info_list.append(info)
        except:
            pass
        return len(info_list)

    def complete_order(self):
        self.driver.find_element(By.CSS_SELECTOR,"[data-test='finish']").click()
        current_url = self.driver.current_url
        return current_url

    def confirmation_message(self):
        try:
            confirmation_message = self.driver.find_element(By.CSS_SELECTOR,"[data-test='complete-header']").text
        except:
            confirmation_message = "None"
        return confirmation_message