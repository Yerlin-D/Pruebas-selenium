from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Iniciar el navegador
driver = webdriver.Chrome() # Puedes cambiar a webdriver.Firefox() si prefieres Firefox

# Función para realizar pruebas de navegación
def test_navigation():
    driver.get("https://www.instagram.com/")
    
    # Esperar a que la página se cargue completamente
    time.sleep(5)

    # Navegar a la página de Explorar
    explore_link = driver.find_element(By.XPATH, "//a[contains(@href,'/explore/')]")
    explore_link.click()

    # Esperar a que la página de Explorar se cargue completamente
    time.sleep(5)

    # Verificar si se ha cargado correctamente la página de Explorar
    assert "Explorar" in driver.title
    assert "Explorar" in driver.page_source

    # Navegar a la página de Perfil
    profile_link = driver.find_element(By.XPATH, "//a[contains(@href,'/accounts/profile/')]")
    profile_link.click()

    # Esperar a que la página de Perfil se cargue completamente
    time.sleep(5)

    # Verificar si se ha cargado correctamente la página de Perfil
    assert "Perfil" in driver.title
    assert "Publicaciones" in driver.page_source

# Ejecutar la prueba de navegación
test_navigation()

# Cerrar el navegador al finalizar las pruebas
driver.quit()
