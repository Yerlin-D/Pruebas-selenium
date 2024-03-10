from selenium import webdriver
from selenium.webdriver.common.by import By
import time

usuario = "napewo5584"
contraseña = "Prueba123"

driver = webdriver.Chrome()
driver.get('https://www.instagram.com/')
time.sleep(5)  # Esperamos un tiempo razonable para que la página cargue completamente

# Localizamos los campos de usuario y contraseña y los completamos
usuario_input = driver.find_element(By.NAME, 'username')
usuario_input.send_keys(usuario)

contrasenia_input = driver.find_element(By.NAME, 'password')
contrasenia_input.send_keys(contraseña)

# Hacemos clic en el botón de inicio de sesión
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

time.sleep(10)  # Esperamos un tiempo para ver si el inicio de sesión tiene éxito antes de cerrar el navegador


driver.quit()
