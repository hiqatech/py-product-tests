from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

from Common.Steps.hooks import assert_that, set_browser, get_url, set_page, get_test_path
from Common.Steps.allPages import get_selector

driver = None
element = None
wait_time_max = 20
waitTime = 0.5


def check_web_step(message):
    if "FAIL" in message:
        stop_web_driver()
    if message != "PASS":
        print(message)
    assert_that(message)


def wait_for_sec(sec):
    time.sleep(sec)
    check_web_step("PASS : I wait for " + str(sec) + " sec")


def start_web_driver(browser):
    try:
        print("\n")
        set_browser(browser)
        message = ": I start the " + browser + " browser"
        global driver
        if browser == "Chrome":
            driver = webdriver.Chrome()
        if browser == "MSEdge":
            driver = webdriver.Edge()
        if browser == "FireFox":
            print("Browser not implemented")
        driver.set_page_load_timeout(20)
        driver.set_script_timeout(100)
        driver.maximize_window()
        check_web_step("PASS " + message)
    except Exception as ex:
        check_web_step("FAIL " + message + "\n" + str(ex))


def stop_web_driver():
    global driver
    try:
        message = ": I stop the " + str(driver.name) + " browser"
        driver.close()
        driver.quit()
        time.sleep(5)
        assert_that("PASS " + message)
    except Exception as ex:
        print("FAIL " + message + "\n " + str(ex))


def navigate_to_the_main_url():
    global driver
    main_url = get_url()
    message = ": I navigate to the " + main_url
    try:
        driver.get(main_url)
        check_web_step("PASS " + message)
    except Exception as ex:
        check_web_step("FAIL " + message + "\n" + str(ex))


def on_the_page(page):
    set_page(page)
    check_web_step("PASS : I am on the " + page + " page")


def navigate_to_the_url(url):
    global driver
    message = ": I navigate to the " + url
    try:
        driver.get(url)
        check_web_step("PASS " + message)
    except Exception as ex:
        check_web_step("FAIL " + message + "\n" + str(ex))


def isDisplayed(selector):
    global driver
    global element
    try:
        element = driver.find_element(By.XPATH, selector)
        if element.is_displayed:
            if element.is_enabled:
                return "PASS"
            return "PASS"
        else:
            return "FAIL"
    except Exception as ex:
        return "FAIL"


def wait_to_appear(selector):
    global wait_time_max
    global waitTime
    start_time = 0
    while start_time < wait_time_max:
        if isDisplayed(selector) == "PASS":
            return "PASS"
        else:
            time.sleep(waitTime)
            start_time = start_time + waitTime
    return ("FAIL : Element with selector" + selector + " did not appear in " + wait_time_max + "s")


def wait_to_disappear(selector):
    start_time = 0
    global wait_time_max
    global waitTime
    while start_time < wait_time_max:
        if isDisplayed(selector) == "FAIL":
            return "PASS"
        else:
            time.sleep(waitTime)
            start_time = start_time + waitTime
    return ("FAIL : Element with selector" + selector + " did not disappear " + wait_time_max + "s")


def wait_to_click(selector):
    global element
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, selector)))


def get_attribute(selector, attribute):
    global element
    try:
        if attribute == "text":
            return element.text
        if attribute == "value":
            return element.get_attribute(attribute)
    except Exception as ex:
        return ex


def type_into_the_element(element_name, text):
    global element
    message = ": I type" + text + " into the " + element_name
    check_web_step(wait_to_appear(get_selector(element_name)))
    try:
        element.send_keys(text)
        check_web_step("PASS " + message)
    except Exception as ex:
        check_web_step("FAIL " + message + "\n" + str(ex))


def select_the_element(element_name):
    global element
    message = ": I select the " + element_name
    check_web_step(wait_to_appear(get_selector(element_name)))
    try:
        wait_to_click(get_selector(element_name))
        element.click()
        check_web_step("PASS " + message)
    except Exception as ex:
        check_web_step("FAIL " + message + " " + str(ex))


def select_the_element_by_text(text):
    global element
    message = ": I select the " + text
    check_web_step(wait_to_appear("//*[contains(text(),'" + text + "')]"))
    try:
        element.click()
        check_web_step("PASS " + message)
    except Exception as ex:
        check_web_step("FAIL " + message + " " + str(ex))

def select_from_dropdown(element_name, text):
    global element
    global driver
    message = ": I select the " + text + " from the " + element_name
    check_web_step(wait_to_appear(get_selector(element_name)))
    try:
        element.click()
        select_the_element_by_text(text)
        check_web_step("PASS " + message)
    except Exception as ex:
        check_web_step("FAIL " + message + " " + str(ex))


def send_enter_to_the_element(element_name):
    global element
    global driver
    message = " : I sent ENTER to the " + element_name
    check_web_step(wait_to_appear(get_selector(element_name)))
    try:
        ActionChains(driver).move_to_element(element).click(element).perform()
        check_web_step("PASS " + message)
    except Exception as ex:
        check_web_step("FAIL " + message + "\n" + str(ex))


def should_see_the_element(element_name):
    message = " : I should see the " + element_name
    check_web_step(wait_to_appear(get_selector(element_name)) + message)


def should_not_see_the_element(element_name):
    message = " : I should see the " + element_name
    check_web_step(wait_to_disappear(get_selector(element_name)) + message)


def should_element_text_equal(element_name, expected):
    message = ": The " + element_name + " text should equal " + expected
    check_web_step(wait_to_appear(get_selector(element_name)))
    attribute = get_attribute(get_selector(element_name),"text")
    if attribute == expected:
        check_web_step("PASS " + message)
    else:
        check_web_step("FAIL " + message)

def should_element_value_equal(element_name, expected):
    message = ": The " + element_name + " value should equal " + expected
    check_web_step(wait_to_appear(get_selector(element_name)))
    attribute = get_attribute(get_selector(element_name),"value")
    if attribute == expected:
        check_web_step("PASS " + message)
    else:
        check_web_step("FAIL " + message)


def should_element_attribute_equal(element_name, attribute, expected):
    message = ": The " + element_name + " " + attribute + " should equal " + expected
    check_web_step(wait_to_appear(get_selector(element_name)))
    attribute = get_attribute(get_selector(element_name), attribute)
    if attribute == expected:
        check_web_step("PASS " + message)
    else:
        check_web_step("FAIL " + message)


def should_not_element_attribute_equal(element_name, attribute, expected):
    message = ": The " + element_name + " " + attribute + "should not equal " + expected
    check_web_step(wait_to_appear(get_selector(element_name)))
    attribute = get_attribute(get_selector(element_name), attribute)
    if expected != attribute:
        check_web_step("PASS " + message)
    else:
        check_web_step("FAIL " + message)


def should_element_attribute_contain(element_name, attribute, expected):
    message = ": The " + element_name + " " + attribute + " should contain " + expected
    check_web_step(wait_to_appear(get_selector(element_name)))
    attribute = get_attribute(get_selector(element_name), attribute)
    if expected in attribute:
        check_web_step("PASS " + message)
    else:
        check_web_step("FAIL " + message)


def should_not_element_attribute_contain(element_name, attribute, expected):
    message = ": The " + element_name + " " + attribute + " should not contain " + expected
    check_web_step(wait_to_appear(get_selector(element_name)))
    attribute = get_attribute(get_selector(element_name), attribute)
    if expected not in attribute:
        check_web_step("PASS " + message)
    else:
        check_web_step("FAIL " + message)


def take_screenshot(name):
    global driver
    message = ": Screenshot taken and save as " + name
    try:
        driver.get_screenshot_as_file(str(get_test_path()) + "/" + name + ".png")
        check_web_step("PASS " + message)
    except Exception as ex:
        check_web_step("FAIL " + message + "\n" + str(ex))

#####################################################################################################################


