import re
from playwright.sync_api import expect

def test_search_no_results_for_qa_manual(page):

    #Dado que el usuario se encuentra en la web
    page.goto("https://www.w3schools.com")

    #Cuando busca un término que no existe (como QA Manual)
    search_input = page.get_by_placeholder("Search...")
    search_input.fill("QA Manual")
    search_input.press("Enter")

    #Entonces se valida que no se muestre contenido relacionado
    expect(page.get_by_text("QA Manual Tutorial")).not_to_be_visible()

    #Y la página sigue funcionando correctamente
    expect(page.locator("body")).to_be_visible()