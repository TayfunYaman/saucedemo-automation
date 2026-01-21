import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class InventoryModule:
    def __init__(self,driver):
        self.driver = driver


    def product_check(self):
        all_products = self.driver.find_elements(By.CSS_SELECTOR,"[data-test='inventory-item']")
        return all_products


    def get_product_prices(self):
        all_products = self.driver.find_elements(By.CSS_SELECTOR,"[data-test='inventory-item']")
        price_list = []
        for product in all_products:
            price = product.find_element(By.CSS_SELECTOR, "[data-test='inventory-item-price']").text
            price = float(price.replace("$", ""))
            price_list.append(price)
        return price_list

    def get_product_names(self):
        all_products = self.driver.find_elements(By.CSS_SELECTOR,"[data-test='inventory-item']")
        name_list = []
        for product in all_products:
            name = product.find_element(By.CSS_SELECTOR, "[data-test='inventory-item-name']").text
            name_list.append(name)
        return name_list

    def get_product_picture_names(self):
        all_products = self.driver.find_elements(By.CSS_SELECTOR,"[data-test='inventory-item']")
        image_name_list = []
        for product in all_products:
            image = product.find_element(By.TAG_NAME, "img")
            image_name = image.get_attribute("src")
            image_name_list.append(image_name)
        return image_name_list

    def sort_products(self,sort_option):
        self.driver.find_element(By.CSS_SELECTOR,"[data-test='product-sort-container']").click()
        self.driver.find_element(By.CSS_SELECTOR,f"[value='{sort_option}']").click()
        if sort_option == "az" or sort_option == "za":
            return self.get_product_names()
        else:
            return self.get_product_prices()

    def item_page_via_name(self):
        inventory_product_names = self.get_product_names()
        inventory_item_names = []
        for i in range(len(inventory_product_names)):
            products = self.driver.find_elements(By.CSS_SELECTOR, "[data-test='inventory-item-name']")
            products[i].click()
            item_name = self.driver.find_element(By.CSS_SELECTOR, "[data-test='inventory-item-name']").text
            inventory_item_names.append(item_name)
            self.driver.find_element(By.CSS_SELECTOR, "[data-test='back-to-products']").click()
        return inventory_item_names, inventory_product_names


    def item_page_via_picture(self):
        inventory_product_image_names = self.get_product_picture_names()
        inventory_item_image_names = []
        for i in range(len(inventory_product_image_names)):
            products = self.driver.find_elements(By.CSS_SELECTOR, "[data-test='inventory-item-name']")
            products[i].click()
            item_name = self.driver.find_element(By.CSS_SELECTOR, "[data-test='inventory-item-name']").text
            inventory_item_image_names.append(item_name)
            self.driver.find_element(By.CSS_SELECTOR, "[data-test='back-to-products']").click()
        return inventory_item_image_names, inventory_product_image_names
