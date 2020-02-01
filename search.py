from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import chromedriver_binary
import time

class Selenium():
    def __init__(self):
        pass
    
    def start_up(self):
        options = Options()
        options.add_argument('--headless')

        driver = webdriver.Chrome(options=options)

        driver.get("https://www.google.com/")
        time.sleep(5)

        print(driver.page_source)
        driver.quit()
        return driver



if __name__ == "__main__":
    instance = Selenium()
    instance.start_up()
