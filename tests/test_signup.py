from playwright.sync_api import Page, expect

def test_signup_with_empty_email(page:Page):
    print ("Given the user open w3school signup page")
    page.goto("https://profile.w3schools.com/signup")

    print("When user leaves empty email")
    #Dejamos vacio el campo email con clear
    page.get_by_placeholder("email").clear()

    print("And the user fill password")
    page.get_by_role("textbox", name="password").clear()
    page.get_by_role("textbox", name="password").fill("1234")

    print("And the user fill password")
    page.get_by_role("textbox", name="first name").clear()
    page.get_by_role("textbox", name="first name").fill("Laura")

    print("And the user fill last name")
    page.get_by_role("textbox", name="last name").clear()
    page.get_by_role("textbox", name="last name").fill("Rodriguez")

    print("And the user click sign up button")
    page.get_by_role("button", name="Create account").click()

    print("Then the user should see error message")
    expect(page.get_by_text("Please fill in all fields")).to_be_visible()

