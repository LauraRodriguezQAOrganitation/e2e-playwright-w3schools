from playwright.sync_api import Page, expect

def test_search_empty(page:Page):
  print("Given the user is on the w3school homepage")
  page.goto("https://www.w3schools.com/")
  
  def accept_cookies_if_present(page):
    try:
        iframe = page.locator('iframe[title="FastCMP"]')
        iframe.wait_for(timeout=5000)
        iframe.content_frame.get_by_role("button", name="Aceptar").click()
    except:
        pass

#Presiona la tecla enter
  page.get_by_placeholder("Search our tutorials").press("Enter")

  print("Then the user should keep seeing search bar")
  expect(page.get_by_role("textbox", name="Search our tutorials")).to_be_visible()

#BUSCAR UNA VARIABLE VALIDA
def test_search_valid_value(page:Page):
    print ("Given the user open w3school homepage")
    page.goto("https://www.w3schools.com/")

    print("When user accept cookies")
    page.locator("iframe[title=\"FastCMP\"]").content_frame.get_by_role("button", name="Aceptar").click()

    print("And the user search for HTML content")
    page.get_by_role("textbox", name="Search our tutorials").click()
    page.get_by_role("textbox", name="Search our tutorials").fill("HTML")
    page.get_by_role("textbox", name="Search our tutorials").press("Enter")

    print("Then the user should see HTML Tutorial page")
    expect(page.locator("h1")).to_be_visible()