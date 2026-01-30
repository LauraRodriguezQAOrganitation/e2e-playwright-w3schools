from playwright.sync_api import Page, expect
import re

def test_visit_menu_links(page: Page):

    print("Given the user visits W3Schools homepage")
    page.goto("https://www.w3schools.com/")

    print("When the page is loaded")
    page.wait_for_url("https://www.w3schools.com/")

    #HTML
    print("And click on HTML menu")
    page.get_by_role("link", name="HTML", exact=True).click()

    print("Then user should be on HTML Tutorial page")
    expect(page).to_have_url("https://www.w3schools.com/html/default.asp")
    expect(page).to_have_url(re.compile("html"))
    expect(page).to_have_title("HTML Tutorial")

    #CSS
    print("And click on CSS menu")
    page.get_by_role("link", name="CSS", exact=True).click()

    print("Then user should be on CSS Tutorial page")
    expect(page).to_have_url(re.compile("css"))
    expect(page).to_have_title("CSS Tutorial")

    #JAVASCRIPT
    print("And click on JAVASCRIPT menu")
    page.get_by_role("link", name="JAVASCRIPT", exact=True).click()

    print("Then user should be on JavaScript Tutorial page")
    expect(page).to_have_url(re.compile("js"))
    expect(page).to_have_title("JavaScript Tutorial")

    #SQL
    print("And click on SQL menu")
    page.get_by_role("link", name="SQL", exact=True).click()

    print("Then user should be on SQL Tutorial page")
    expect(page).to_have_url(re.compile("sql"))
    expect(page).to_have_title("SQL Tutorial")

    #PYTHON
    print("And click on PYTHON menu")
    page.get_by_role("link", name="PYTHON", exact=True).click()

    print("Then user should be on Python Tutorial page")
    expect(page).to_have_url(re.compile("python"))
    expect(page).to_have_title("Python Tutorial")