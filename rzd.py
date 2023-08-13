from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time, re, logging
#import winsound


class Rzdtemp():
    def __init__(self, logger):
        self.logger = logger
    def setUp(self):
        binary = r'/snap/bin/firefox'
        options = Options()
        options.binary = binary
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://ticket.rzd.ru/"
        self.verificationErrors = []

    def test_rzdtemp(self):

        self.logger.info('Вход...')

        driver = self.driver
        driver.get(self.base_url)
        
        el = '25.08.2023'
        
        driver.find_element(By.ID, "direction-from").clear()
        driver.find_element(By.ID, "direction-from").send_keys('Москва')
        driver.find_element(By.CSS_SELECTOR, "div[class='rzd-direction rzd-direction-from'] li:nth-child(2)")
        time.sleep(1)
        driver.find_element(By.ID, "direction-to").clear()
        driver.find_element(By.ID, "direction-to").send_keys('Санкт-Петербург')
        driver.find_element(By.CSS_SELECTOR, "div[class='rzd-direction rzd-direction-to'] li:nth-child(2)")
        time.sleep(1)
        driver.find_element(By.ID, "datepicker-from").clear()
        driver.find_element(By.ID, "datepicker-from").send_keys(el)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".rzd-button-wrapper.rzd-cell.rzd-cell-15").click()
        
        #driver.find_element(By.ID, "direction-from").clear()
        driver.find_element(By.ID, "direction-from").send_keys('Москва')
        driver.find_element(By.CSS_SELECTOR, "div[class='rzd-direction rzd-direction-from'] li:nth-child(2)")
        time.sleep(1)
        #driver.find_element(By.ID, "direction-to").clear()
        driver.find_element(By.ID, "direction-to").send_keys('Санкт-Петербург')
        
        driver.find_element(By.CSS_SELECTOR, "div[class='rzd-direction rzd-direction-to'] li:nth-child(2)")
        time.sleep(1)
        driver.find_element(By.ID, "datepicker-from").clear()
        driver.find_element(By.ID, "datepicker-from").send_keys(el)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".rzd-button-wrapper.rzd-cell.rzd-cell-15").click()
        time.sleep(5)
        
        self.logger.info('Поиск нужных билетов...')
        #rawhtml = driver.find_element(By.ID, '.rzd-button-wrapper.rzd-cell.rzd-cell-15').get_attribute("innerHTML")
        
        try:
            driver.find_element(By.CSS_SELECTOR, "ui-kit-button[class='search-more-button-long tst-searchMore-searchCmmtNoTrain ng-star-inserted'] button[type='button']")
            #subprocess.run(['notify-send', "У нас билетик"]
        except NoSuchElementException:
            subprocess.run(['notify-send', "У нас билетик"])

    def tearDown(self):
        self.logger.info('Закрываем браузер...')
        self.driver.close()
        self.driver.quit()
        
logger = logging.getLogger('log')
rzd = Rzdtemp(logger)
rzd.setUp()
rzd.test_rzdtemp()
rzd.tearDown()
