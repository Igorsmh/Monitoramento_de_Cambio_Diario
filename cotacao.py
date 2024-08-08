from src import init_driver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as condicao_esperada
from selenium.webdriver.support.wait import WebDriverWait

#Site usado
site_escolhido = 'https://br.financas.yahoo.com/quote/USDBRL%3DX/'

sleep(5)

driver, wait = init_driver()
driver.get(site_escolhido)



dados_historicos = wait.until(condicao_esperada.element_to_be_clickable(
    (By.XPATH,"//li[@data-test='HISTORICAL_DATA']"))).click()



# Rolar X quantidade em pixels(descer)
sleep(3)
driver.execute_script("window.scrollTo(0, 500);")
sleep(3)


#Extrair o Dolar atual
cotacao = driver.find_elements(By.XPATH, "//td[@class='Py(10px) Pstart(10px)']")
cotacao_text = cotacao[3].text
sleep(3)

#Extrair a data atual
data = driver.find_elements(By.XPATH, "//td[@class='Py(10px) Ta(start) Pend(10px)']")
data_text = data[0].text
sleep(3)


#print(hora_text)
