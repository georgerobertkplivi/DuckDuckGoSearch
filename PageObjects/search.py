from selenium.webdriver.common.by import By
from selenium import webdriver

class DuckDuckGo:
    #Search Page Locators
    search_box_xpath = "//input[@id='search_form_input_homepage']"
    search_button_xpath = "//input[@id='search_button_homepage']"


    def __init__(self,driver):
        self.driver = driver

    def set_search_term(self,word):
        browser = self.driver
        browser.find_element(By.XPATH,self.search_box_xpath).clear()
        browser.find_element(By.XPATH, self.search_box_xpath).send_keys(word)

    def click_search_button(self):
        browser = self.driver
        browser.find_element(By.XPATH,self.search_button_xpath).click()

    def verify_page_title(self):
        browser = self.driver
        act_page_title = browser.title
        page_title = "python at DuckDuckGo"
        assert page_title in act_page_title


    def close_browser(self):
        browser = self.driver
        browser.close()





