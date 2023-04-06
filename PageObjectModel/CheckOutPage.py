from selenium.webdriver.common.by import By
from selenium import webdriver

class CheckOutPage:
  products = (By.XPATH, "//div[@class='card h-100']")
  def __init__(self, driver):
    self.driver = driver

  def findProductsFromList(self):
    all_products = self.driver.find_elements(*CheckOutPage.products)
    for item in all_products:
      if item.text == "Blackberry":
        item.find_element(By.XPATH, "div/button").click()


