import time
import unittest

from selenium import webdriver

class mySeleniumTest(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome("Web Driver Local Path \\chromedriver.exe")
        self.driver.get("Your Test URL")
        self.driver.maximize_window()

    def test_mtTest2(self):

        #Sisteme login olma
        self.driver.find_element_by_id("email").send_keys(" ")
        self.driver.find_element_by_id("password").send_keys(" ")
        self.driver.find_element_by_class_name("MuiButton-label").click()
        time.sleep(10)

        #MT Ekranına giriş
        mtButton = self.driver.find_element_by_class_name("musteri")
        mtButton.click()
        time.sleep(5)
        okButton = self.driver.find_element_by_class_name("ui-dialog-buttonset")
        okButton.click()
        time.sleep(10)

        #Statü kontroller elemanlarının alınması
        ready = self.driver.find_element_by_id("agent-status-available")
        acw = self.driver.find_element_by_id("agent-status-acw")
        sBreak = self.driver.find_element_by_id("agent-status-shortbreak")
        lunch = self.driver.find_element_by_id("agent-status-lunch")
        training = self.driver.find_element_by_id("agent-status-training")
        meeting = self.driver.find_element_by_id("agent-status-meeting")

        #Statü kontrollerinin yapılması
       
        ready.click()
        time.sleep(5)
        sBreak.click()
        time.sleep(5)
        lunch.click()
        time.sleep(5)
        training.click()
        time.sleep(5)
        meeting.click()
        time.sleep(5)
        acw.click()
        time.sleep(5)
        '''
        toc = time.perf_counter()
        tic = time.perf_counter()
        print("İşlem Süresi:",toc - tic)
        '''
