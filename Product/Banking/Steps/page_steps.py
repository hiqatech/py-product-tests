from Common.Steps.web_steps import *

def login_with_user(user_name):
    on_the_page("Login")
    select_the_element("customer_login")
    select_from_dropdown("user_select", "Ron Weasly")
    select_the_element("login_button")
    time.sleep(2)

def go_to_deposit():
    on_the_page("UserHome")
    select_the_element("deposit_button")

def land_deposit(amount):
    on_the_page("Deposit")
    type_into_the_element("amount_field", amount)
    select_the_element("deposit_submit")
    time.sleep(2)

def verify_deposit(amount):
    should_see_the_element("deposit_successful")
    should_element_text_equal("balance", "100")

def go_to_transactions():
    on_the_page("UserHome")
    select_the_element("transactions_button")

def verify_transaction(amount):
    on_the_page("Transactions")
    should_element_text_equal("transaction1_amount", "100")
    select_the_element("back_button")