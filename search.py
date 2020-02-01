from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import chromedriver_binary
import time

from write_csv import WriteCSV

CSV_FILE = "./url.csv"

class Selenium():
    def __init__(self):
        self.weite_instance = WriteCSV()
    
    def remove_linefeed(self, list_obj):
        replace_list = []
        for line in list_obj:
            replace_list.append(line.replace('\n',''))
        return replace_list

    def fetch_html(self, driver):
        return driver.page_source

    def get_url(self):
        with open(CSV_FILE, mode='r', encoding='utf-8') as url_file:
            target_url = list(url_file)
        target_url = self.remove_linefeed(target_url)
        return target_url

    def main(self):
        options = Options()
        options.add_argument('--headless')

        driver = webdriver.Chrome(options=options)

        URL = self.get_url()
        for url_line in range(len(URL)):
            print("Open: " + URL[url_line])
            driver.get(URL[url_line])
            html = self.fetch_html(driver)
            self.weite_instance.write_csv(html)
            time.sleep(5)

        html = self.fetch_html(driver)
        driver.quit()
        return driver

if __name__ == "__main__":
    instance = Selenium()
    instance.main()
