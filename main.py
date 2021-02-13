# This is a sample Python script.

# importing webdriver from selenium
from selenium import webdriver

# Here Chrome will be used
driver = webdriver.Chrome(executable_path="C:/Users/mm195/Desktop/YMLILGEE/Programs/Gecko Driver/chromedriver_win32/chromedriver.exe")


# URL of website
url = "https://www.geeksforgeeks.org/"

# Opening the website
driver.get(url)

# Getting current URL source code
get_title = driver.title

# Printing the title of this URL
print(get_title)

