# 
# You must be install Chromium browser
#  (for use the webdriver)
# 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests

# Inicializar el navegador
driver = webdriver.Chrome()  # ChromeDriver debe estar en tu PATH (OS)
driver.get("https://web.whatsapp.com/")
time.sleep(20)  # Esperar tiempo suficiente para escanear el código QR

def descargar_foto_de_perfil(nombre_contacto):
    # 01. Buscar el campo de búsqueda y escribir el nombre del contacto
    search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    search_box.clear()
    search_box.send_keys(nombre_contacto)
    time.sleep(2)  # Esperar a que aparezcan los resultados de búsqueda

    # 02. Hacer clic en el contacto que se encontro con el nombre ingresado
    contact = driver.find_element(By.XPATH, '//*[@id="pane-side"]//span[@title="{}"]'.format(nombre_contacto))
    contact.click()
    print("se clicleo")
    time.sleep(2)  # Esperar a que se abra la conversación con el contacto

    # 03. Clickear en la foto (para ver la foto mas grande)
    contact = driver.find_element(By.XPATH, '//*[@id="main"]/header/div[1]')
    contact.click()
    print("se clicleo")

    # 04. Obtener la URL de la foto de perfil
    profile_picture = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[5]/span/div/span/div/div/section/div[1]/div[1]/div/img')
    picture_url = profile_picture.get_attribute("src")
    print(picture_url)

    # Descargar la foto de perfil
    response = requests.get(picture_url)
    with open(f"{nombre_contacto}_profile_picture.jpg", "wb") as file:
        file.write(response.content)

    print(f"Foto de perfil de {nombre_contacto} descargada exitosamente.")

#
#
# Started the app
#
#
# Llamar a la función para descargar la foto de perfil de un contacto específico
contacto_a_buscar = "Pepe"
descargar_foto_de_perfil(contacto_a_buscar)

# Cerrar el navegador
driver.quit()
