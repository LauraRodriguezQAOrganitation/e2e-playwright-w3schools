from playwright.sync_api import Page, expect
from utils import accept_cookies_if_present, open_search_if_mobile

def test_search_no_results_for_qa_manual(page: Page):

    #Dado que el usuario se encuentra en la web
    page.goto("https://www.w3schools.com")

    #(CLAVE en prueba de escritorio y movil)
    accept_cookies_if_present(page)
    open_search_if_mobile(page)

    #Cuando busca una variable que no existe (Como QA Manual)
    search_input = page.get_by_placeholder("Search...")
    expect(search_input).to_be_visible()

    search_input.fill("QA Manual")
    search_input.press("Enter")

    #Entonces no se muestra contenido relacionado
    expect(page.get_by_text("QA Manual Tutorial")).not_to_be_visible()

    #Y la página sigue funcionando correctamente
    expect(page.locator("body")).to_be_visible()
