from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from argparse import ArgumentParser
import sys
import chromedriver_binary
import time

from write_csv import WriteCSV

CSV_FILE = './url.csv'

class Selenium():
    def __init__(self, args):
        self.weite_instance = WriteCSV()
        if '-i' in args or '--ignore-space-at-eol' in args:
            self.linefeed_option = True
        else:
            self.linefeed_option = False
    
    def remove_linefeed(self, obj):
        if type(obj) != list:
            replace_obj = obj.replace('\n','')
            return replace_obj
        replace_list = []
        for line in obj:
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
            print('Open: ' + URL[url_line])
            driver.get(URL[url_line])
            html = self.fetch_html(driver)
            if self.linefeed_option == True:
                html = self.remove_linefeed(html)
            self.weite_instance.write_csv(html)
            time.sleep(5)

        html = self.fetch_html(driver)
        driver.quit()
        return driver
        
if __name__ == '__main__':
    usage = 'Usage: python {} FILE [--ignore-space-at-eol] [--help]\n'.format(__file__)
    option = 'Optional arguments: \n\
    -h, --help                   show this help message and exit\n\
    -i, --ignore-space-at-eol    register HTML remove linefeed'
    args = sys.argv
    if '-h' in args or '--help' in args:
        print(usage + option)
        exit(1)
    instance = Selenium(args)
    instance.main()
