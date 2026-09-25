#Imports

from playwright.sync_api import sync_playwright

#Test Data

URL = "https://www.saucedemo.com"

#Functions

def login(page, username, password):
    page.locator('#user-name').fill(username)
    page.locator('#password').fill(password)
    page.locator("#login-button").click()

def add_backpack_to_cart(page):
    page.locator("#add-to-cart-sauce-labs-backpack").click()

def remove_backpack_from_cart(page):
    page.locator("#remove-sauce-labs-backpack").click()

def open_cart(page):
    page.locator("a.shopping_cart_link").click()

def verify_backpack_in_cart(page):
    inventory_item = page.locator("div.inventory_item_name").first
    assert inventory_item.text_content() == "Sauce Labs Backpack"

def verify_empty_cart(page):
    assert page.locator(".shopping_cart_badge").count() == 0

def verify_product_count(page, expected_count):
    products = page.locator(".inventory_item_name")
    assert products.count() == 6

def verify_product_visible(page, product_name):
    products = page.locator(".inventory_item_name").all_text_contents()
    assert product_name in products

#Test 1 - Verify successful login


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()
    page.goto(URL)

    login(page, "standard_user", "secret_sauce")

    page.wait_for_timeout(1000)

    print(page.title())
    print(page.url)

    assert page.url == "https://www.saucedemo.com/inventory.html"

    browser.close()


#Test 2 - Verify products are displayed

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()
    page.goto(URL)

    login(page, "standard_user", "secret_sauce")

    page.wait_for_timeout(1000)
    verify_product_count(page, 6)

    verify_product_visible(page, "Sauce Labs Backpack")

    add_backpack_to_cart(page)
    cart_badge = page.locator(".shopping_cart_badge")

    assert cart_badge.text_content() == "1"

    open_cart(page)
    verify_backpack_in_cart(page)

    remove_backpack_from_cart(page)

    verify_empty_cart(page)


    browser.close()

