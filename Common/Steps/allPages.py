from Common.Steps.hooks import get_product, get_page
from Product.Banking.Pages.login import banking_login_page_elements
from Product.Banking.Pages.userhome import banking_userhome_page_elements
from Product.Banking.Pages.deposit import banking_deposit_page_elements
from Product.Banking.Pages.transactions import banking_transactions_page_elements


def get_selector(element_name):
    if get_product() == "Banking":
        if get_page() == "Login":
            return banking_login_page_elements.get(element_name)
        if get_page() == "UserHome":
            return banking_userhome_page_elements.get(element_name)
        if get_page() == "Deposit":
            return banking_deposit_page_elements.get(element_name)
        if get_page() == "Transactions":
            return banking_transactions_page_elements.get(element_name)