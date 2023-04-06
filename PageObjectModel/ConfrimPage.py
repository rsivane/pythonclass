from selenium.webdriver.common.by import By
from selenium import webdriver

from PageObjectModel import HomePage


class ConfrimPage:
    shop = (By.XPATH, "//button[@class='btn btn-success']")
    def __init__(self, driver):
        


