from seleniumbase import Driver
from selenium.webdriver.common.by import By
import pyperclip
import pyautogui
import time

driver = Driver(uc=True)
url = "https://www.imovelweb.com.br/apartamentos-vendas-joao-pessoa.html"
driver.uc_open_with_reconnect(url, 4)
driver.uc_gui_click_captcha()

imovel = []
titulos = []
subtitulos = []
vendas = []
condominioIptus = []
enderecos = []
iconFeatures = []
descricoes = []
caracteristicas = []
fotos = []
dados = []

anuncios = driver.find_elements(By.CLASS_NAME, "olx-ad-card")

anuncios[0].click()
    
titulos.append(driver.find_element(By.CLASS_NAME, "olx-text").text)
subtitulos.append(driver.find_element(By.CLASS_NAME, "olx-d-flex").text)
vendas.append(driver.find_element(By.CLASS_NAME, "price-value").text)
condominioIptus.append(driver.find_element(By.CLASS_NAME, "price-expenses").text)
enderecos.append(driver.find_element(By.CLASS_NAME, "section-location-property").text)
descricoes.append(driver.find_element(By.CLASS_NAME, "description-module__wrapper-description___2rEoY").text)

buttons = int(driver.find_element(By.ID, "new-gallery-portal").text)
pyautogui.moveTo(394, 619)  
pyautogui.click()

for i in range(buttons):
    pyautogui.moveTo(818, 664)  
    pyautogui.rightClick()
    pyautogui.moveTo(917, 798)
    pyautogui.click()

    image_src = pyperclip.paste()
    fotos.append(image_src)
    
    pyautogui.moveTo(1585, 636)
    pyautogui.click()
    time.sleep(3)

driver.close()

# proximos passos:
# 1. pegar os dados do scraping e gerar uma api com fastapi
# 2. Pegar a api gerada e colocar