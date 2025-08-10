import os
from pathlib import Path

import pytest
import datetime
import time

product = None
browser = None
page = None
test_path = None

def start_test(prod):
    print("\n")
    print("HiQATech")
    print(datetime.datetime.now())
    global product
    product = prod
    current_path = Path(os.getcwd())
    global test_path
    test_path = current_path
    print("test_path =" + str(current_path))
    print("report_path =" + str(current_path.parent))
    global driver_path
    driver_path = str(current_path.parent.parent.parent.parent) + "\Common\WebDrivers"
    print("driver_path =" + str(driver_path))


def set_browser(net):
    global browser
    browser = net


def get_browser():
    return "Chrome"


def get_product():
    return product

def get_test_path():
    return test_path

def set_page(page_name):
    global page
    page = page_name

def get_page():
    return page

def get_url():
    global product
    global browser
    if product == "Banking":
        if browser in "Chrome, MSEdge,Firefox":
            return str("https://www.globalsqa.com/angularJs-protractor/BankingProject")

def verify_that(message):
    assert True, message
    print(message)


def assert_that(message):
    # print(message)
    if "PASS" in message:
        assert True
    elif "FAIL" in message:
        time.sleep(2)
        assert False
