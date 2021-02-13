import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from PageObjects.search import DuckDuckGo


class TestDuckDuckGo:
    # Search Page Test Data
    global word,url
    word = "python"
    url = "https://duckduckgo.com/"

    @pytest.fixture()
    def browser(self):
        driver = webdriver.Chrome(executable_path="C:/Users/mm195/Desktop/YMLILGEE/Programs/Gecko Driver/chromedriver_win32/chromedriver.exe")
        driver.get(url)
        driver.implicitly_wait(15)
        # Return the driver object at the end of setup
        yield driver

        # For cleanup, quit the driver
        driver.quit()

    def test_search_001(self,browser):
        self.search = DuckDuckGo(browser)
        self.search.set_search_term(word)
        self.search.click_search_button()

    def test_page_title_002(self,browser):
        self.home = DuckDuckGo(browser)
        self.home.set_search_term(word)
        self.home.click_search_button()
        self.home.verify_page_title()




