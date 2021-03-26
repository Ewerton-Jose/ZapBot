from selenium import webdriver
import time
import os

caminho = os.getcwd()
print(caminho)
class zapzapbot:
    def __init__(self):
        self.mensagem = 'Pênis'
        self.grupos = "GTA"
        opitions = webdriver.ChromeOptions()
        opitions.add_argument('lang=pt-br')
        self.webdriver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def enviar(self):
        self.webdriver.get('https://web.whatsapp.com')
        time.sleep(30)
        grupo = self.webdriver.find_element_by_xpath("//span[@titlle='GTA']")
        grupo.click()
        time.sleep(3)
        cb = self.webdriver.find_element_by_class_name("_2A8P4")
        cb.click()
        time.sleep(2)
        cb.send_keys(self.mensagem)
        self.webdriver.find_element_by_xpath("//span[@data-icon='send']")
        be.click()
        sleep(3)

boti = zapzapbot()
boti.enviar()