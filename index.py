from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests

# Inicializar el navegador
driver = webdriver.Chrome()  # ChromeDriver debe estar en tu PATH
driver.get("https://web.whatsapp.com/")
time.sleep(15)  # Esperar tiempo suficiente para escanear el código QR

def descargar_foto_de_perfil(nombre_contacto):
    # Buscar el campo de búsqueda y escribir el nombre del contacto
    search_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="3"]')
    search_box.clear()
    search_box.send_keys(nombre_contacto)
    time.sleep(2)  # Esperar a que aparezcan los resultados de búsqueda

    # Hacer clic en el contacto
    contact = driver.find_element_by_xpath(f'//span[@title="{nombre_contacto}"]')
    contact.click()
    time.sleep(2)  # Esperar a que se abra la conversación con el contacto

    # Obtener la URL de la foto de perfil
    profile_picture = driver.find_element_by_xpath('//img[@class="_2goTk"]')
    picture_url = profile_picture.get_attribute("src")

    # Descargar la foto de perfil
    response = requests.get(picture_url)
    with open(f"{nombre_contacto}_profile_picture.jpg", "wb") as file:
        file.write(response.content)

    print(f"Foto de perfil de {nombre_contacto} descargada exitosamente.")

# Llamar a la función para descargar la foto de perfil de un contacto específico
contacto_a_buscar = "Juana"
descargar_foto_de_perfil(contacto_a_buscar)

# Cerrar el navegador
driver.quit()



# simple instalar chromiun simple STEP with selenium
# CHROMIUM BY DEFAULT INSTALL WEBDRIVER INTO THE BINARY FILES
