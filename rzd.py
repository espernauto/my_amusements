from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ChromeOptions
import time, re, logging, subprocess

class Rzdtemp():
    def __init__(self, logger):
        self.logger = logger
    def setUp(self):
        options = ChromeOptions()
        options.add_argument("--headless=new")
        self.driver = webdriver.Chrome(options = options)
        self.driver.implicitly_wait(30)
        self.base_url = "http://ticket.rzd.ru/"
        self.verificationErrors = []

    def test_rzdtemp(self, city1, city2, date):

        self.logger.info('Вход...')

        driver = self.driver
        driver.get(self.base_url)
        
        driver.find_element(By.ID, "direction-from").clear()
        driver.find_element(By.ID, "direction-from").send_keys(city1)
        driver.find_element(By.CSS_SELECTOR, "div[class='rzd-direction rzd-direction-from'] li:nth-child(2)")
        time.sleep(1)
        driver.find_element(By.ID, "direction-to").clear()
        driver.find_element(By.ID, "direction-to").send_keys(city2)
        driver.find_element(By.CSS_SELECTOR, "div[class='rzd-direction rzd-direction-to'] li:nth-child(2)")
        time.sleep(1)
        driver.find_element(By.ID, "datepicker-from").clear()
        driver.find_element(By.ID, "datepicker-from").send_keys(date)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".rzd-button-wrapper.rzd-cell.rzd-cell-15").click()
        
        #driver.find_element(By.ID, "direction-from").clear()
        driver.find_element(By.ID, "direction-from").send_keys(city1)
        driver.find_element(By.CSS_SELECTOR, "div[class='rzd-direction rzd-direction-from'] li:nth-child(2)")
        time.sleep(1)
        #driver.find_element(By.ID, "direction-to").clear()
        driver.find_element(By.ID, "direction-to").send_keys(city2)
        
        driver.find_element(By.CSS_SELECTOR, "div[class='rzd-direction rzd-direction-to'] li:nth-child(2)")
        time.sleep(1)
        driver.find_element(By.ID, "datepicker-from").clear()
        driver.find_element(By.ID, "datepicker-from").send_keys(date)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".rzd-button-wrapper.rzd-cell.rzd-cell-15").click()
        #time.sleep(10)
        
        self.logger.info('Поиск нужных билетов...')
        #rawhtml = driver.find_element(By.ID, '.rzd-button-wrapper.rzd-cell.rzd-cell-15').get_attribute("innerHTML")
        
        try:
            driver.find_element(By.CSS_SELECTOR, "rzd-search-results-card-railway-flat-card")
            subprocess.run(['notify-send', "У нас билетик"])
        except NoSuchElementException:
            subprocess.run(['notify-send', "Билетов нет"])
            pass

    def tearDown(self):
        self.logger.info('Закрываем браузер...')
        self.driver.close()
        self.driver.quit()
        
print("Введите город отправления")
city1 = input()
print("Введите город назначения")
city2 = input()
print("Введите дату")
date = input()
logger = logging.getLogger('log')
rzd = Rzdtemp(logger)
rzd.setUp()
rzd.test_rzdtemp(city1, city2, date)
rzd.tearDown()
