from playwright.sync_api import Page, expect
from utils import accept_cookies_if_present

def test_search_empty(page:Page):
  print("Given the user is on the w3school homepage")
  page.goto("https://www.w3schools.com/")
  
  accept_cookies_if_present(page)

#Presiona la tecla enter
  page.get_by_placeholder("Search our tutorials").press("Enter")

  print("Then the user should keep seeing search bar")
  expect(page.get_by_role("textbox", name="Search our tutorials")).to_be_visible()

#BUSCAR UNA VARIABLE VALIDA
def test_search_valid_value(page:Page):
    print ("Given the user open w3school homepage")
    page.goto("https://www.w3schools.com/")

 
    accept_cookies_if_present(page)

    print("And the user search for HTML content")
    page.get_by_role("textbox", name="Search our tutorials").click()
    page.get_by_role("textbox", name="Search our tutorials").fill("HTML")
    page.get_by_role("textbox", name="Search our tutorials").press("Enter")

    print("Then the user should see HTML Tutorial page")
    expect(page.locator("h1")).to_be_visible()

def test_search_no_results_for_qa_manual(page: Page):

#Dado que el usuario se encuentra en la web
    page.goto("https://www.w3schools.com")


    accept_cookies_if_present(page)
    
#Cuando busca una variable que no existe (Como QA Manual)
    search_input = page.get_by_placeholder("Search our tutorials, e.g.")
    expect(search_input).to_be_visible()

    search_input.fill("QA Manual")
    search_input.press("Enter")

#Entonces no se muestra contenido relacionado
    expect(page.get_by_text("QA Manual Tutorial")).not_to_be_visible()

#Y la página sigue funcionando correctamente
    expect(page.locator("body")).to_be_visible()

def test_search_html_tutorial(page):
    #Dado que el usuario se encuentra en la web de W3Schools
    page.goto("https://www.w3schools.com")

    accept_cookies_if_present(page)
    

    #Entonces se valida que el menú principal se visualiza correctamente (localizador por ID)
    menu = page.locator("#subtopnav")
    expect(menu).to_be_visible()

    #Cuando el usuario utiliza el buscador para buscar un tutorial existente
    search_input = page.locator("input[aria-label='Search our tutorials']")
    search_input.click()
    search_input.fill("HTML")
    search_input.press("Enter")

    #Entonces se valida que el usuario es redirigido al tutorial de HTML
    expect(page).to_have_url("https://www.w3schools.com/html/default.asp")

    #Y se muestra el título principal del tutorial
    expect(page.locator("h1")).to_be_visible()
