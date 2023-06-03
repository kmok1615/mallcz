from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import pytest

from Tests.test_base import BaseTest
from Config.config import TestData

# Main Function
class Test_MallCZ_Carousel(BaseTest):
        
    @pytest.mark.mallcz00
    def test_carousel01(self):

        ## Case 01: allegro: Check if there is 15 items in this carousel
        self.driver.get(TestData.MALLCZ_URL)
        time.sleep(4)
        carousel01_elem = self.driver.find_element(By.CLASS_NAME, "hooper-list")

        ## Scroll to 1st carousel
        self.driver.execute_script("arguments[0].scrollIntoView();",carousel01_elem)

        ## Check number of items in carousel
        carousel01_item = carousel01_elem.find_elements(By.CLASS_NAME, "product-box-simple__box")
        carousel01_item_num = len(carousel01_item)
        print("Carousel item number: ", carousel01_item_num)
        if carousel01_item_num == 15:
            print("Test PASSED")
            assert True
        else:
            print("Test FAILED")
            assert False

    @pytest.mark.mallcz00
    def test_carousel02(self):

        ## Case 02: nejlepsi: Check if there is 15 items in this carousel
        self.driver.get(TestData.MALLCZ_URL)
        time.sleep(4)
        carousel02_elem = self.driver.find_element(By.CLASS_NAME, "hooper-list")

        ## Scroll to 2nd carousel
        self.driver.execute_script("arguments[1].scrollIntoView();",carousel02_elem)

        ## Check number of items in carousel
        carousel02_item = carousel02_elem.find_elements(By.CLASS_NAME, "product-box-simple__box")
        carousel02_item_num = len(carousel02_item)
        print("Carousel item number: ", carousel02_item_num)
        if carousel02_item_num == 15:
            print("Test PASSED")
            assert True
        else:
            print("Test FAILED")
            assert False

    @pytest.mark.mallcz00
    def test_carousel03(self):

        ## Case 03: doma jako: Check if there is 15 items in this carousel
        self.driver.get(TestData.MALLCZ_URL)
        time.sleep(4)
        carousel03_elem = self.driver.find_element(By.CLASS_NAME, "hooper-list")

        ## Scroll to 3rd carousel
        self.driver.execute_script("arguments[2].scrollIntoView();",carousel03_elem)

        ## Check number of items in carousel
        carousel03_item = carousel03_elem.find_elements(By.CLASS_NAME, "product-box-simple__box")
        carousel03_item_num = len(carousel03_item)
        print("Carousel item number: ", carousel03_item_num)
        if carousel03_item_num == 15:
            print("Test PASSED")
            assert True
        else:
            print("Test FAILED")
            assert False


    @pytest.mark.mallcz00
    def test_carousel04(self):

        ## Case 04: na plaz: Check if there is 15 items in this carousel
        self.driver.get(TestData.MALLCZ_URL)
        time.sleep(4)
        carousel04_elem = self.driver.find_element(By.CLASS_NAME, "hooper-list")

        ## Scroll to 4th carousel
        self.driver.execute_script("arguments[3].scrollIntoView();",carousel04_elem)

        ## Check number of items in carousel
        carousel04_item = carousel04_elem.find_elements(By.CLASS_NAME, "product-box-simple__box")
        carousel04_item_num = len(carousel04_item)
        print("Carousel item number: ", carousel04_item_num)
        if carousel04_item_num == 15:
            print("Test PASSED")
            assert True
        else:
            print("Test FAILED")
            assert False

    @pytest.mark.mallcz00
    def test_carousel05(self):

        ## Case 05: doprava: Check if there is 15 items in this carousel
        self.driver.get(TestData.MALLCZ_URL)
        time.sleep(4)
        carousel05_elem = self.driver.find_element(By.CLASS_NAME, "hooper-list")

        ## Scroll to 5th carousel
        self.driver.execute_script("arguments[4].scrollIntoView();",carousel05_elem)

        ## Check number of items in carousel
        carousel05_item = carousel05_elem.find_elements(By.CLASS_NAME, "product-box-simple__box")
        carousel05_item_num = len(carousel05_item)
        print("Carousel item number: ", carousel05_item_num)
        if carousel05_item_num == 15:
            print("Test PASSED")
            assert True
        else:
            print("Test FAILED")
            assert False

    @pytest.mark.mallcz00
    def test_carousel06(self):

        ## Case 06: hyckejte: Check if there is 15 items in this carousel
        self.driver.get(TestData.MALLCZ_URL)
        time.sleep(4)
        carousel06_elem = self.driver.find_element(By.CLASS_NAME, "hooper-list")

        ## Scroll to 6th carousel
        self.driver.execute_script("arguments[5].scrollIntoView();",carousel06_elem)

        ## Check number of items in carousel
        carousel06_item = carousel06_elem.find_elements(By.CLASS_NAME, "product-box-simple__box")
        carousel06_item_num = len(carousel06_item)
        print("Carousel item number: ", carousel06_item_num)
        if carousel06_item_num == 15:
            print("Test PASSED")
            assert True
        else:
            print("Test FAILED")
            assert False

    @pytest.mark.mallcz00
    def test_carousel07(self):

        ## Case 07: to bude jizda: Check if there is 15 items in this carousel
        self.driver.get(TestData.MALLCZ_URL)
        time.sleep(4)
        carousel07_elem = self.driver.find_element(By.CLASS_NAME, "hooper-list")

        ## Scroll to 7th carousel
        self.driver.execute_script("arguments[6].scrollIntoView();",carousel07_elem)

        ## Check number of items in carousel
        carousel07_item = carousel07_elem.find_elements(By.CLASS_NAME, "product-box-simple__box")
        carousel07_item_num = len(carousel07_item)
        print("Carousel item number: ", carousel07_item_num)
        if carousel07_item_num == 15:
            print("Test PASSED")
            assert True
        else:
            print("Test FAILED")
            assert False

    @pytest.mark.mallcz00
    def test_carousel08(self):

        ## Case 08: dokonala: Check if there is 15 items in this carousel
        self.driver.get(TestData.MALLCZ_URL)
        time.sleep(4)
        carousel08_elem = self.driver.find_element(By.CLASS_NAME, "hooper-list")

        ## Scroll to 7th carousel
        self.driver.execute_script("arguments[7].scrollIntoView();",carousel08_elem)

        ## Check number of items in carousel
        carousel08_item = carousel08_elem.find_elements(By.CLASS_NAME, "product-box-simple__box")
        carousel08_item_num = len(carousel08_item)
        print("Carousel item number: ", carousel08_item_num)
        if carousel08_item_num == 15:
            print("Test PASSED")
            assert True
        else:
            print("Test FAILED")
            assert False

