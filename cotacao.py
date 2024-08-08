from src import init_driver
from time import sleep
from selenium.webdriver.common.by import By

#Site usado
site_escolhido = 'https://br.financas.yahoo.com/quote/USDBRL%3DX/'



driver = init_driver()
driver.get(site_escolhido)
sleep(5)

#Extrair o Dolar atual
cotacao = driver.find_element(By.XPATH, "//fin-streamer[@data-test='qsp-price']")
cotacao_text = cotacao.text

#Extrair a data atual
hora = driver.find_element(By.CLASS_NAME,'quote-market-notice')
hora_text = hora.text



