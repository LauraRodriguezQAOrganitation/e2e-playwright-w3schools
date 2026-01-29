from playwright.sync_api import Page, expect


# TEST 1: EMAIL VACÍO
def test_signup_with_empty_email(page: Page):
    print("Given the user opens W3Schools signup page")
    page.goto("https://profile.w3schools.com/signup")

    print("When user leaves email empty")
    page.get_by_placeholder("email").clear()

    print("And the user fills password")
    page.get_by_placeholder("password").fill("Test-1234")

    print("And the user fills first name and last name")
    page.get_by_placeholder("first name").fill("Laura")
    page.get_by_placeholder("last name").fill("Rodriguez")

    print("And the user clicks sign up button")
    page.get_by_role("button", name="Create account").click()

    print("Then the user should see an error message")
    expect(page.get_by_text("Please fill in all fields")).to_be_visible()


# TEST 2: CONTRASEÑA VACÍA
def test_signup_with_empty_password(page: Page):
    print("Given the user opens W3Schools signup page")
    page.goto("https://profile.w3schools.com/signup")

    print("And the user fills email with valid email")
    page.get_by_placeholder("email").fill("laura@gmail.com")

    print("And the user fills first name and last name")
    page.get_by_placeholder("first name").fill("Laura")
    page.get_by_placeholder("last name").fill("Rodriguez")

    print("When user leaves password empty")
    page.get_by_placeholder("password").clear()

    print("And the user clicks sign up button")
    page.get_by_role("button", name="Create account").click()

    print("Then the user should see an error message")
    expect(page.get_by_text("Please fill in all fields")).to_be_visible()