from selenium.webdriver.common.by import By
import PageObjectModel.CheckOutPage
from Drivers.Utilities.BaseClass import BaseClass


class Home(BaseClass):
    def __init__(self, driver):
        self.driver = driver
    button_shop = (By.XPATH,"//a[text()='Shop']")
    button_Home = (By.LINK_TEXT,"Home")
    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    check = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")

    def shopItems(self):
       self.driver.find_element(*Home.button_shop).click()
       checkoutpage = PageObjectModel.CheckOutPage.CheckOutPage(self.driver)
       return checkoutpage

    def getName(self):
        return self.driver.find_element(*Home.name)

    def getEmail(self):
        return self.driver.find_element(*Home.email)

    def getCheckBox(self):
        return self.driver.find_element(*Home.check)

    def getGender(self):
        return self.driver.find_element(*Home.gender)

    def submitForm(self):
        return self.driver.find_element(*Home.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*Home.successMessage)
