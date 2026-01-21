import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CartModule:
    def __init__(self,driver):
        self.driver = driver

    def get_cart_badge_number(self):
        try:
            cart_badge_element_number = self.driver.find_element(By.CSS_SELECTOR,"[data-test='shopping-cart-badge']").text
        except:
            cart_badge_element_number = 0
        return int(cart_badge_element_number)

    def add_to_cart_inventory_page(self):
        products = self.driver.find_elements(By.CSS_SELECTOR, "[data-test='inventory-item']")
        element_count = len(products)
        button_name_list = []
        for product in products:
            product.find_element(By.CLASS_NAME,"btn_inventory").click()
            button_name = product.find_element(By.CLASS_NAME,"btn_inventory").text
            button_name_list.append(button_name)
        remove_count = button_name_list.count("Remove")
        cart_badge_element_number = self.get_cart_badge_number()
        return element_count, int(cart_badge_element_number), remove_count


    def add_to_cart_inventory_item_page(self):
        inventory_product_elements = self.driver.find_elements(By.CSS_SELECTOR,"[data-test='inventory-item']")
        inventory_product_elements_count = len(inventory_product_elements)
        button_name_list = []
        for i in range(len(inventory_product_elements)):
            products = self.driver.find_elements(By.CSS_SELECTOR, "[data-test='inventory-item-name']")
            products[i].click()
            self.driver.find_element(By.CSS_SELECTOR,"[data-test='add-to-cart']").click()
            try:
                button_name = self.driver.find_element(By.CSS_SELECTOR, "[data-test='remove']").text
                if button_name == "Remove":
                    button_name_list.append(button_name)
            except:
                pass
            self.driver.find_element(By.CSS_SELECTOR, "[data-test='back-to-products']").click()
        remove_count = button_name_list.count("Remove")
        cart_badge_element_number = self.get_cart_badge_number()
        return inventory_product_elements_count, int(cart_badge_element_number), remove_count


    def remove_from_cart_inventory_page(self):
        inventory_product_elements = self.driver.find_elements(By.CSS_SELECTOR, "[data-test='inventory-item']")
        remove_list = self.driver.find_elements(By.CLASS_NAME,"btn_secondary")
        remove_count = len(remove_list)
        for product in inventory_product_elements:
            product.find_element(By.CLASS_NAME, "btn_secondary").click()
        inventory_product_elements_count = len(inventory_product_elements)
        cart_badge_element_number = self.get_cart_badge_number()
        add_to_cart_list = self.driver.find_elements(By.CLASS_NAME,"btn_primary")
        add_to_cart_count = len(add_to_cart_list)
        return inventory_product_elements_count, int(cart_badge_element_number), remove_count, add_to_cart_count


    def remove_from_cart_inventory_item_page(self):
        inventory_product_elements = self.driver.find_elements(By.CSS_SELECTOR,"[data-test='inventory-item']")
        inventory_product_elements_count = len(inventory_product_elements)
        add_to_cart_list = []
        remove_from_cart_list = []
        for i in range(len(inventory_product_elements)):
            products = self.driver.find_elements(By.CSS_SELECTOR, "[data-test='inventory-item-name']")
            products[i].click()
            try:
                button_name = self.driver.find_element(By.CSS_SELECTOR, "[data-test='remove']").text
                self.driver.find_element(By.CSS_SELECTOR, "[data-test='remove']").click()
                if button_name == "Remove":
                    remove_from_cart_list.append(button_name)
            except:
                pass
            # self.driver.find_element(By.CSS_SELECTOR,"[data-test='remove']").click()
            try:
                button_name = self.driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart']").text
                if button_name == "Add to cart":
                    add_to_cart_list.append(button_name)
            except:
                pass
            self.driver.find_element(By.CSS_SELECTOR, "[data-test='back-to-products']").click()
        remove_count = len(remove_from_cart_list)
        add_to_cart_count = len(add_to_cart_list)
        cart_badge_element_number = self.get_cart_badge_number()
        return inventory_product_elements_count, int(cart_badge_element_number), remove_count, add_to_cart_count




    def remove_element_from_cart_page(self):
        cart_badge_element_number = self.get_cart_badge_number()
        while int(cart_badge_element_number) == 0:
            self.driver.find_element(By.CLASS_NAME, "btn_primary").click()
            cart_badge_element_number = self.get_cart_badge_number()
        self.driver.find_element(By.CSS_SELECTOR,"[data-test='shopping-cart-link']").click()
        self.driver.find_element(By.CLASS_NAME,"btn_secondary").click()
        try:
            empty_card = self.driver.find_element(By.CLASS_NAME,"removed_cart_item")
            cart_status = "Empty"
        except:
            cart_status = "Not Empty"
        cart_badge_element_number = self.get_cart_badge_number()
        return cart_badge_element_number, cart_status


