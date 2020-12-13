import time
import unittest

from selenium import webdriver

class mySeleniumTest(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome("C:\\Users\\AloTech\\PycharmProjects\\SeleniumTest\\chromedriver.exe")
        self.driver.get("https://staging1.alo-tech.com/v2/tr/login2.html")
        self.driver.maximize_window()

    def test_mtTest2(self):

        #Sisteme login olma
        self.driver.find_element_by_id("email").send_keys("test@test.com")
        self.driver.find_element_by_id("password").send_keys("123123")
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
        tic = time.perf_counter()
        ready.click()
        toc = time.perf_counter()
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

        print("İşlem Süresi:",toc - tic)
