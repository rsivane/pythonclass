
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest

from Drivers.Utilities.BaseClass import BaseClass
from PageObjectModel.CheckOutPage import  CheckOutPage
from PageObjectModel.HomePage import Home


class TestOne(BaseClass):
   def test_e2eTesting(self):
    homepage = Home(self.driver)
    homepage_shop = homepage.shopItems()
    homepage_shop.findProductsFromList()

    '''
    products = self.driver.find_elements(By.XPATH,"//div[@class='card h-100']")

    for product in products :
        productName = product.find_element(By.XPATH, "div/h4/a").text
        if productName == "Blackberry":
            product.find_element(By.XPATH, "div/button").click()
'''

    self.driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
    self.driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
    self.driver.find_element(By.ID,"country").send_keys("ind")
    wait = WebDriverWait(self.driver,10)
    wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
    self.driver.find_element(By.LINK_TEXT,"India").click()
    self.driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
    self.driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()
    successText = self.driver.find_element(By.CLASS_NAME,"alert-success").text
    assert "Success! Thank you!" in successText

