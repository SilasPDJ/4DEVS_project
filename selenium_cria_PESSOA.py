
from os import path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
mypath = '\\'.join(path.realpath(__file__).split('\\')[:-1])
downldpath = path.join(mypath, 'dados_json')
options = Options()
options.add_experimental_option("prefs", {
    "download.default_directory": downldpath,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing_for_trusted_sources_enabled": False,
    "safebrowsing.enabled": True,
    'profile.default_content_setting_values.automatic_downloads': 1

})

gerador_link = 'https://www.4devs.com.br/gerador_de_pessoas'
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# pgdas_driver.get('https://www.4devs.com.br')


def gera_n_vezes(n: int):
    for e in range(n):
        driver.get(gerador_link)
        # sexo aleatório && dados_json
        driver.find_element_by_id('sexo_indiferente').click()
        driver.find_element_by_id('pontuacao_nao').click()
        qtd_pessoas = driver.find_element_by_id('txt_qtde')
        qtd_pessoas.clear()
        qtd_pessoas.send_keys(30)

        driver.find_element_by_id('bt_gerar_pessoa').click()
        bt = 'Download'
        driver.implicitly_wait(10)
        download = driver.find_element_by_css_selector(f"[title^='{bt}']")
        from time import sleep
        sleep(3)
        download.click()
        sleep(3)


gera_n_vezes(2)
# pgdas_driver.find_element_by_id('idade').send_keys()
