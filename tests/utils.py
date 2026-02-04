from playwright.sync_api import Page

#Aceptar cookies (desktop y mobile)
def accept_cookies_if_present(page: Page):
    try:
        #cambiar localizador
        print("When user accept cookies")
        page.frame_locator("iframe[title=\"FastCMP\"]").get_by_role("button", name="Accept").click(timeout=2000)
    except:
        print("Cookies not present")


#Abrir buscador solo si estamos en móvil
def open_search_if_mobile(page: Page):
    try:
        # En móvil existe el botón "Button to search"
        search_button = page.get_by_label("Button to search")
        if search_button.is_visible():
            search_button.click()
    except:
        pass

def isMobile(page:Page):
    if (page.viewport_size['width'] > 1024):
        return False
    else:
        return True
