from playwright.sync_api import Page, expect

def test_search_empty(page:Page):
  print("Given the user is on the w3school homepage")
  page.goto("https://www.w3schools.com/")

  print ("When the user accept the cookeis")
  page.locator("iframe[title=\"FastCMP\"]").content_frame.get_by_role("button", name="Aceptar").click()

  print("And the user search with empty value")
  page.get_by_placeholder("Search our tutorials").click()
#Presiona la tecla enter
  page.get_by_placeholder("Search our tutorials").press("Enter")

  print("Then the user should keep seeing search bar")
  expect(page.get_by_role("textbox", name="Search our tutorials")).to_be_visible()
