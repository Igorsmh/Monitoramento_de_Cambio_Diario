# Monitoramento Dólar para Real com geração de relatório

Este projeto é um script Python que acessa um site de cotação de dólar (USD) para real brasileiro (BRL), captura a cotação atual, a data, o site de referência, e tira um print da página. Em seguida, gera um relatório em PDF com essas informações. O projeto também inclui um instalador para facilitar a instalação e execução do programa.

## Funcionalidades

- Acessa um site de cotação de câmbio USD/BRL
- Captura a cotação atual
- Armazena a data da captura
- Salva o site de referência
- Tira um print da página de cotação
- Gera um relatório em PDF contendo a cotação, data, site e print da página
- Inclui um instalador para facilitar a instalação e execução do script


## Uso

1. Clone este repositório:
    ```bash
    git clone https://github.com/Igorsmh/Monitoramento_de_Cambio_Diario.git
    cd Monitoramento_de_Cambio_Diario
    ```
2. Execute o instalador:
  ```bash
   
  ```

3. O script irá acessar o site de cotação, capturar as informações necessárias, gerar um relatório em PDF e salvá-lo no diretório especificado.


## Instalação do repositório:

1. Clone este repositório:
    ```bash
    git clone https://github.com/Igorsmh/Monitoramento_de_Cambio_Diario.git
    cd Monitoramento_de_Cambio_Diario
    ```

2. Instale os requisitos:
    ```bash
    pip install -r requirements.txt
    ```

3. Certifique-se de ter o WebDriver do Selenium (por exemplo, ChromeDriver) instalado e configurado no PATH do sistema.

4. Execute o script principal:
    ```bash
    python cotacao.py
    ```
    
## Exemplo de Saída

Um relatório em PDF será gerado contendo:

- Cotação atual do dólar em relação ao real
- Data da captura da cotação
- URL do site de referência
- Print da página de cotação


