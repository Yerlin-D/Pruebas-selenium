from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Iniciar el navegador
driver = webdriver.Chrome()  # Puedes cambiar a webdriver.Firefox() si prefieres Firefox

name = "Napewo"
email = "napewo5584@fashlend.com"
username = "Napewo5584"
password = "Prueba123"

# Función para realizar pruebas de registro
def test_registration():
    driver.get("https://www.instagram.com/accounts/emailsignup/")
    
    # Esperar a que la página se cargue completamente
    time.sleep(5)

    # Introducir información en los campos del formulario de registro
    name_input = driver.find_element(By.NAME, "name")
    email_input = driver.find_element(By.NAME, "emailOrPhone")
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")
    signup_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    name_input.send_keys("Napewo D")
    email_input.send_keys("napewo5584@fashlend.com")
    username_input.send_keys("Napewo5584")
    password_input.send_keys("Prueba123")
    signup_button.click()

    # Esperar a que se procese el registro
    time.sleep(5)

    # Verificar si se ha completado el registro correctamente
    assert "Instagram" in driver.title
    assert "Inicio" in driver.page_source

# Ejecutar la prueba de registro
test_registration()

# Cerrar el navegador al finalizar las pruebas
driver.quit()
