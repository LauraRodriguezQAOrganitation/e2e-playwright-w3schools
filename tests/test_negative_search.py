from playwright.sync_api import Page, expect

#Aceptamos las cookies
def accept_cookies_if_present(page: Page):
    try:
        accept_button = page.get_by_role("button", name="Accept")
        if accept_button.is_visible():
            accept_button.click()
    except:
        pass

#Abrir buscador si es móvil
def open_search_if_mobile(page: Page):
    search_button = page.locator("#tnb-google-search-btn")
    if search_button.count() > 0 and search_button.is_visible():
        search_button.click()

#Buscamos una variable inexistente (QA Manual)
def test_search_no_results_for_qa_manual(page: Page):

    #Dado que el usuario se encuentra en la web
    page.goto("https://www.w3schools.com")

    #(CLAVE en test móvil)
    accept_cookies_if_present(page)
    open_search_if_mobile(page)

    #Cuando busca una variable que no existe
    search_input = page.get_by_placeholder("Search...")
    search_input.wait_for(state="visible")
    search_input.fill("QA Manual")
    search_input.press("Enter")

    #Entonces no se muestra contenido relacionado
    expect(page.get_by_text("QA Manual Tutorial")).not_to_be_visible()

    #Y la página sigue funcionando correctamente
    expect(page.locator("body")).to_be_visible()
