from typing import Dict


banking_deposit_page_elements = {
    "amount_field" : "//input[@placeholder='amount']",
    "deposit_submit" : "//button[text()='Deposit']",
    "deposit_successful" : "//*[text()='Deposit Successful']",
    "account_number" : "//*[text()='Account Number : ']//following::strong[1]",
    "balance" : "//*[text()='Account Number : ']//following::strong[2]",
    "currency" : "//*[text()='Account Number : ']//following::strong[3]",

    "deposit_button" : "//button[contains(text(),'Deposit')]",
    "transactions_button" : "//button[contains(text(),'Transactions')]",
    "withdrawl_button" : "//button[contains(text(),'Withdrawl')]",

    "home_button" : "//button[text()='Home']",
    "logout_button" : "//button[text()='Logout']",

}






