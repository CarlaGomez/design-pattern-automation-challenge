# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


import os
from dotenv import load_dotenv
from actors.actor import Actor
from tasks.search_for_products import SearchForProducts
from tasks.sort_items import SortItems
from tasks.go_to_item_details import GoToItemDetails
from tasks.validate_item_name import ValidateItemName
from tasks.validate_item_price import ValidateItemPrice
from tasks.add_item_to_cart import AddItemToCart
from tasks.validate_items_on_shopping_cart import ValidateItemsOnShoppingCart
from tasks.validate_shipping_info import ValidateShippingInfo
from tasks.checkout import Checkout
from tasks.validate_checkout_info import ValidateCheckoutInfo
from tasks.confirm_purchase import ConfirmPurchase
from tasks.validate_purchase import ValidatePurchase
from tasks.login import Login
from tasks.navigate_to import NavigateTo

load_dotenv()

login_name = os.getenv("LOGIN_NAME")
login_password = os.getenv("LOGIN_PASSWORD")


def test_purchase(page):
    actor = Actor("Test User", page)
    actor.attempts_to(
        NavigateTo(),
        Login(login_name, login_password),
        SearchForProducts("Fragrance", "Women"),
        SortItems("p.price-ASC"),
        GoToItemDetails(),
        ValidateItemName("ck One Gift Set"),
        ValidateItemPrice("$36.00"),
        AddItemToCart("1"),
        ValidateItemsOnShoppingCart("Shopping Cart", "ck One Gift Set", "1"),
        ValidateShippingInfo("$36.00", "$41.06"),
        Checkout(),
        ValidateCheckoutInfo(
            "Checkout Confirmation", "ck One Gift Set", "$36.00", "$41.06"
        ),
        ConfirmPurchase(),
        ValidatePurchase("Your Order Has Been Processed!"),
    )
