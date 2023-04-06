
from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest

from Drivers.Utilities.BaseClass import BaseClass
from PageObjectModel.HomePage import Home

class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):
        homepage= Home(self.driver)
        homepage.getName().send_keys(getData[0])
        homepage.getEmail().send_keys(getData[1])
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(), getData[2])

        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text

        assert ("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=[("Fita","Academy","Male"),("karthick","Kamal","Male")])
    def getData(self, request):
        return request.param