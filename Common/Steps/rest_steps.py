import requests
import json
from Common.Steps.hooks import assert_that, verify_that

request = None
response = None
status = None
rest_url = None


def create_the_request(data):
    global request
    request = data


def send_get_request_to(url):
    message = " : send request to " + url
    global response
    global status
    global rest_url
    rest_url = url

    try:
        resp = requests.get(url, data=request)
        response = json.loads(resp.text)
        status = resp.status_code
        verify_that("Response is : " + str(response))
        assert_that("PASS " + message)
    except Exception as ex:
        assert_that("FAIL " + message + " " + str(ex))

def send_post_request_to(url):
    message = " : send request to " + url
    global response
    global status
    global rest_url
    rest_url = url

    try:
        resp = requests.post(url, data=request)
        response = json.loads(resp.text)
        status = resp.status_code
        verify_that("Response is : " + str(response))
        assert_that("PASS " + message)
    except Exception as ex:
        assert_that("FAIL " + message + " " + str(ex))

def response_status_should_be(status_code):
    message = " : The response status code should be " + status_code
    global status
    if str(status) == status_code:
        assert_that("PASS" + message)
    else:
        assert_that("FAIL" + message)


def response_status_should_not_be(status_code):
    message = " : The response status code should not be " + status_code
    global status
    if str(status) != status_code:
        assert_that("FAIL" + message)
    else:
        assert_that("PASS" + message)


def response_text_should_contain(text):
    message = " : The text should be " + text
    global response
    if text in str(response):
        assert_that("PASS" + message)
    else:
        assert_that("FAIL" + message)


def response_text_should_not_contain(text):
    message = " : The text should not be " + text
    global response
    if text not in str(response):
        assert_that("FAIL" + message)
    else:
        assert_that("PASS" + message)


def response_detail1_should_be(detail1, expected):
    message = " : The response " + str(detail1) + " should be " + str(expected)
    global response
    if str(response[detail1]) == str(expected):
        assert_that("PASS" + message)
    else:
        assert_that("FAIL" + message)


def response_detail1_should_not_be(detail1,expected):
    message = " : The response " + str(detail1) + " should be " + str(expected)
    global response
    if str(response[detail1]) != str(expected):
        assert_that("FAIL" + message)
    else:
        assert_that("PASS" + message)


def response_detail2_should_be(detail1, detail2, expected):
    message = " : The response " + str(detail2) + " should be " + str(expected)
    global response
    if str(response[detail1][detail2]) == str(expected):
        assert_that("PASS" + message)
    else:
        assert_that("FAIL" + message)


def response_detail2_should_not_be(detail1,detail2,expected):
    message = " : The response " + str(detail2) + " should be " + expected
    global response
    if str(response[detail1][detail2]) != str(expected):
        assert_that("FAIL" + message)
    else:
        assert_that("PASS" + message)