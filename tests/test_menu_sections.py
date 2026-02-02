from playwright.sync_api import Page, expect
import re

#Aceptamos las cookies
def accept_cookies_if_present(page: Page):
    accept_button = page.get_by_role("button", name="Accept")
    if accept_button.is_visible():
        accept_button.click()

#Abrimos el menu
def open_menu(page: Page):
    menu_button = page.locator("#navbtn_tutorials")

    if menu_button.is_visible():
        menu_button.click()
    else:
        page.get_by_role("button", name="Tutorials").hover()
        page.locator("#nav_tutorials").wait_for(state="visible")


def test_visit_menu_links(page: Page):

    page.goto("https://www.w3schools.com/")
    accept_cookies_if_present(page)
    page.wait_for_url("https://www.w3schools.com/")

    #HTML
    open_menu(page)
    page.locator("#nav_tutorials").get_by_role("link", name="HTML", exact=True).click()
    expect(page).to_have_url(re.compile("html"))
    expect(page).to_have_title("HTML Tutorial")
    expect(page.locator("h1")).to_be_visible()

    #CSS
    open_menu(page)
    page.locator("#nav_tutorials").get_by_role("link", name="CSS", exact=True).click()
    expect(page).to_have_url(re.compile("css"))
    expect(page).to_have_title("CSS Tutorial")
    expect(page.locator("h1")).to_be_visible()

    #JAVASCRIPT
    open_menu(page)
    page.locator("#nav_tutorials").get_by_role("link", name="JAVASCRIPT", exact=True).click()
    expect(page).to_have_url(re.compile("js"))
    expect(page).to_have_title("JavaScript Tutorial")
    expect(page.locator("h1")).to_be_visible()

    #SQL
    open_menu(page)
    page.locator("#nav_tutorials").get_by_role("link", name="SQL", exact=True).click()
    expect(page).to_have_url(re.compile("sql"))
    expect(page).to_have_title("SQL Tutorial")
    expect(page.locator("h1")).to_be_visible()

    #PYTHON
    open_menu(page)
    page.locator("#nav_tutorials").get_by_role("link", name="PYTHON", exact=True).click()
    expect(page).to_have_url(re.compile("python"))
    expect(page).to_have_title("Python Tutorial")
    expect(page.locator("h1")).to_be_visible()

    #JAVA
    open_menu(page)
    page.locator("#nav_tutorials").get_by_role("link", name="JAVA", exact=True).click()
    expect(page).to_have_url(re.compile("java"))
    expect(page).to_have_title("Java Tutorial")
    expect(page.locator("h1")).to_be_visible()
