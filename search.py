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

        driver.get(URL)
        time.sleep(5)
        html = self.fetch_html(driver)
        driver.quit()
        return driver

    def fetch_html(self, driver):
        return driver.page_source



if __name__ == "__main__":
    instance = Selenium()
    instance.start_up()
