import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

ROOT_FOLDER = Path(__file__).parent #bloco base para excução do selenium
EDGEDRIVER_EXEC = ROOT_FOLDER / 'drivers' / 'msedgedriver.exe' #exec do webdriver
edge_options = webdriver.EdgeOptions() #instancia o option do navegador
edge_service = Service(executable_path = str(EDGEDRIVER_EXEC)) 
edge_browser = webdriver.Edge(
    service=edge_service,
    options=edge_options,
)

edge_browser.get("https://www.google.com/webhp?hl=pt-BR&sa=X&ved=0ahUKEwiiquvdj9X_AhWlpJUCHaiJA9IQPAgI") #Localiza o site
search = edge_browser.find_element(By.CLASS_NAME, "gLFyf") #Localiza o elemento de busca
search.send_keys("Corinthians", Keys.ENTER) #Executa uma ação
classification = edge_browser.find_element(By.XPATH, '//*[@id="sports-app"]/div/div[2]/div/div/div/ol/li[3]').click() #Clica na classificação
time.sleep(10) #Função de tempo para fechar para encerrar o programa

