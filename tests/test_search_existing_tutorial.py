from playwright.sync_api import expect

def test_search_html_tutorial(page):
    #Dado que el usuario se encuentra en la web de W3Schools
    page.goto("https://www.w3schools.com")

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