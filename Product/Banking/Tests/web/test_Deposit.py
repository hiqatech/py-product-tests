import pytest

from Common.Steps.hooks import start_test
from Common.Steps.web_steps import start_web_driver, navigate_to_the_main_url, stop_web_driver
from Product.Banking.Steps.page_steps import login_with_user, go_to_deposit, land_deposit, verify_deposit, \
    go_to_transactions, verify_transaction


@pytest.fixture
def start_run():
    start_test("Banking")
    start_web_driver("Chrome")
    navigate_to_the_main_url()
    yield
    stop_web_driver()

@pytest.mark.bankingweb
@pytest.mark.parametrize("amount", ['100'])
def test_make_deposits(start_run, amount):
    login_with_user("Ron Weasly")
    go_to_deposit()
    land_deposit(amount)
    verify_deposit(amount)
    go_to_transactions()
    verify_transaction(amount)



