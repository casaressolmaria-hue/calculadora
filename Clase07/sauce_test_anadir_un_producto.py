from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument('--start-maximized') # Opcional: ventana grande
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5) # Espera implícita profesional

try:
    # 1) Entrar a la página
    driver.get('https://www.saucedemo.com')
    
    # 2) Verificar título de la página
    assert driver.title == 'Swag Labs' 

    # 3) Login
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()

    # 4) Verificar que estamos en el inventario
    assert '/inventory.html' in driver.current_url
    print('Test OK')

    # 5) Verificar título de sección
    titulo = driver.find_element(By.CSS_SELECTOR,
    'div.header_secondary_container .title').text
    assert titulo == 'Products'

    # 6) Confirma que aparece al menos un div.inventory_item
    productos = driver.find_elements(By.CSS_SELECTOR, "div.inventory_item")
    assert len(productos) > 0

    # 7) Muestra en consola el nombre y precio del primer producto
    primer_producto = productos[0]
    nombre_del_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio_del_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text

    print(f"Nombre: {nombre_del_producto}, Precio: {precio_del_producto}")

    # 8) Haz clic en "Add to cart" del primer producto
    boton_agregar = primer_producto.find_element(By.XPATH, ".//button[text()='Add to cart']")
    boton_agregar.click()

    # 9) Verifica que el contador del carrito muestre 1
    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    badge = carrito.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    assert len(badge) > 0

    valor = badge[0].text
    assert valor == "1"
    
    print(f"El contador del carrito: {valor}")

finally:
    driver.quit()