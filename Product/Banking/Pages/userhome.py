from typing import Dict


banking_userhome_page_elements = {
    "search_field" : "//input[@id='search']",
    "search_button" : "//*[@id='search-icon-legacy']",
    "deposit_button" : "//button[contains(text(),'Deposit')]",
    "transactions_button" : "//button[contains(text(),'Transactions')]",
    "withdrawl_button" : "//button[contains(text(),'Withdrawl')]",

    "account_number" : "//*[text()='Account Number : ']//following::strong[1]",
    "balance" : "//*[text()='Account Number : ']//following::strong[2]",
    "currency" : "//*[text()='Account Number : ']//following::strong[3]",

    "home_button" : "//button[text()='Home']",
    "logout_button" : "//button[text()='Logout']",
}



