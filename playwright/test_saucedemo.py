#Imports

from playwright.sync_api import sync_playwright

#Test Data

URL = "https://www.saucedemo.com"

#Functions

def login(page, username, password):
    page.locator("#user-name").fill(username)
    page.locator("#password").fill(password)
    page.locator("#login-button").click()

def add_product_to_cart(page, product_id_name):
    page.locator(f"#add-to-cart-{product_id_name}").click()

def remove_product_from_cart(page, product_id_name):
    page.locator(f"#remove-{product_id_name}").click()

def open_cart(page):
    page.locator("a.shopping_cart_link").click()

def verify_product_in_cart(page, expected_product_name):
    cart_products = page.locator("div.inventory_item_name").all_text_contents()
    assert expected_product_name in cart_products

def verify_empty_cart(page):
    assert page.locator(".shopping_cart_badge").count() == 0

def verify_product_count(page, expected_count):
    products = page.locator(".inventory_item_name")
    assert products.count() == expected_count

def verify_product_visible(page, product_name):
    products = page.locator(".inventory_item_name").all_text_contents()
    assert product_name in products

def test_successful_login(page):
    page.goto(URL)
    login(page, "standard_user", "secret_sauce")
    assert page.url == "https://www.saucedemo.com/inventory.html"

def test_locked_out_user_login(page):
    page.goto(URL)
    login(page, "locked_out_user", "secret_sauce")
    assert page.locator("[data-test='error']").text_content() == "Epic sadface: Sorry, this user has been locked out."

def test_add_and_remove_product_from_cart(page):
    product_name = "Sauce Labs Bolt T-Shirt"
    product_id = "sauce-labs-bolt-t-shirt"
    page.goto(URL)
    login(page, "standard_user", "secret_sauce")
    page.wait_for_timeout(1000)
    verify_product_count(page, 6)
    verify_product_visible(page, product_name)
    add_product_to_cart(page, product_id)
    assert page.locator(".shopping_cart_badge").text_content() == "1"
    open_cart(page)
    verify_product_in_cart(page, product_name)
    remove_product_from_cart(page, product_id)
    verify_empty_cart(page)
