import pgdas_driver as pgd
from selenium.webdriver.support.ui import Select

from os.path import realpath

path = '\\'.join(realpath(__file__).split('\\')[:-1])

driver = pgd.pgdas_driver('Chromedriver/chromedriver.exe', path+'\\dados_json')
# pgdas_driver.get('https://www.4devs.com.br')
driver.get('https://www.4devs.com.br/gerador_de_pessoas')


# sexo aleatório && dados_json
driver.find_element_by_id('sexo_indiferente').click()
driver.find_element_by_id('pontuacao_nao').click()
qtd_pessoas = driver.find_element_by_id('txt_qtde')
qtd_pessoas.clear()
qtd_pessoas.send_keys(20)


def gera_n_vezes(n: int):
    for e in range(n):
        driver.find_element_by_id('bt_gerar_pessoa').click()
        bt = 'Download'
        driver.implicitly_wait(10)
        download = driver.find_element_by_css_selector(f"[title^='{bt}']")
        from time import sleep
        sleep(3)
        download.click()

gera_n_vezes(4)
# pgdas_driver.find_element_by_id('idade').send_keys()






