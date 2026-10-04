import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def driver():
    # Setup Chrome WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    # Teardown
    driver.quit()

#Automatización de Login exitoso en SauceDemo
def test_01_login(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    assert "https://www.saucedemo.com/inventory.html" in driver.current_url, f"ERROR: Login fallido, usuario no fue redirigido a la página de inventario."

#Verificar título de la página y título de catálogo después del login exitoso
def test_02_verify_title(driver):
    page_title = driver.title
    section_title = driver.find_element(By.CLASS_NAME, "title").text

    assert page_title == "Swag Labs", f"ERROR: Título de ventana incorrecto. Se esperaba 'Swag Labs', pero se obtuvo '{page_title}'."

    assert section_title == "Products", f"ERROR: Título de catálogo incorrecto. Se esperaba 'Products', pero se obtuvo '{section_title}'."

#Verificar que existan productos visibles en la página de inventario después del login exitoso
def test_03_verify_visible_products(driver):
    visible_products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(visible_products) > 0, f"ERROR: No se encontraron productos visibles en la página de inventario."

#Verificar que exista un producto específico en la página de inventario después del login exitoso
def test_04_verify_specific_product(driver):
    specific_product = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    assert len(specific_product) > 0, f"ERROR: El producto 'Sauce Labs Backpack' no se encontró en la página de inventario."

#Verificar interfaz de usuario después del login exitoso
def test_05_verify_ui_elements(driver):
    # Verificar que el botón de menú esté presente
    menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
    assert menu_button.is_displayed(), f"ERROR: El botón de menú no está visible en la página de inventario."

    # Verificar que el filtro esté presente
    filter_button = driver.find_element(By.CLASS_NAME, "product_sort_container")
    assert filter_button.is_displayed(), f"ERROR: El filtro no está visible en la página de inventario."

#Añadir un producto al carrito
def test_06_add_product_to_cart(driver):
    # Añadir el producto "Sauce Labs Backpack" al carrito
    first_product = driver.find_elements(By.CLASS_NAME, "inventory_item")[0]
    add_to_cart_button = first_product.find_element(By.TAG_NAME, "button")
    add_to_cart_button.click()

    #Espera explícita para que el botón cambie a "REMOVE"
    WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element((By.TAG_NAME, "button"), "Remove"))    
    assert add_to_cart_button.text.capitalize() == "REMOVE", f"ERROR: El botón no cambió a 'REMOVE' después de añadir el producto al carrito."

#Verificar contador de carrito después de añadir un producto
def test_07_verify_cart_counter(driver):
    cart_counter = driver.find_element(By.CLASS_NAME,'shopping_cart_badge').text

    assert cart_counter == "1", f"ERROR: El contador de carrito no muestra 1 después de añadir un producto. Valor actual: {cart_counter}"

#Navegar al carrito de compras
def test_08_navigate_to_cart(driver):
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    assert "/cart.html" in driver.current_url, f"ERROR: No se redirigió a la página del carrito."


#Comprobar que el producto añadido esté presente en el carrito
def test_09_verify_product_in_cart(driver):
    product_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert product_name == "Sauce Labs Backpack", f"ERROR: El producto en el carrito no es 'Sauce Labs Backpack'. Producto encontrado: {product_name}"