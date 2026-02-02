from playwright.sync_api import Page

#Aceptar cookies (desktop y mobile)
def accept_cookies_if_present(page: Page):
    try:
        accept_button = page.get_by_role("button", name="Accept")
        if accept_button.is_visible():
            accept_button.click()
    except:
        pass


#Abrir buscador solo si estamos en móvil
def open_search_if_mobile(page: Page):
    try:
        # En móvil existe el botón "Button to search"
        search_button = page.get_by_label("Button to search")
        if search_button.is_visible():
            search_button.click()
    except:
        pass
