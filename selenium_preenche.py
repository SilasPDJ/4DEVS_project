from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support import expected_conditions


from selenium.webdriver.support.ui import Select

from clipboard import paste


driver = webdriver.Chrome(executable_path='Chromedriver/chromedriver.exe')
driver.get('https://www.4devs.com.br')


class Gerador:

    def gera_nomes(self, link, gender_value: int, race_value='human'):

        driver.find_element_by_link_text(link).click()
        driver.implicitly_wait(10)

        # race
        race = Select(driver.find_element_by_name('race'))
        race.select_by_value(race_value)

        # gender
        gender = Select(driver.find_element_by_name('gender'))
        gender.select_by_index(gender_value)
        input('tudo certo?')
        copy = driver.find_elements_by_class_name('clipboard-copy')

        for el in copy:
            el.click()
            final = paste()
            yield final

    def gera_numeros(self, qtd, between: tuple, ordem_index=0, unico=False, txtcolunas=str(1), link='Gerador de Números Aleatórios'):

        def clear_b4(el):
            el.clear()
            return el

        driver.find_element_by_link_text(link).click()
        driver.implicitly_wait(10)

        clear_b4(driver.find_element_by_id('txt_entre_de')).send_keys(between[0])
        clear_b4(driver.find_element_by_id('txt_entre_para')).send_keys(between[1])
        clear_b4(driver.find_element_by_id('txt_colunas')).send_keys(txtcolunas)

        clear_b4(driver.find_element_by_id('txt_quantidade')).send_keys(str(qtd))

        if unico:
            driver.find_element_by_id('chk_unico').click()

        ordem_lista = Select(driver.find_element_by_id('sel_ordem'))
        ordem_lista.select_by_index(ordem_index)

        driver.find_element_by_id('bt_gerar').click()

        nmr_table = driver.find_element_by_id('resposta').find_element_by_tag_name('table')
        trs_table = nmr_table.find_elements_by_tag_name('tr')
        for el in trs_table:
            print(el.find_element_by_tag_name('td').text)
            yield el.find_element_by_tag_name('td').text

GR = Gerador()

numeros_len = '1'*10, '9'*10
# numeros = GR.gera_numeros(len(list(masculino)), between=numeros_len)

masc = GR.gera_nomes('Gerador de Nomes', 1)

numeros = GR.gera_numeros(10, between=numeros_len)


[print(n) for n in numeros]





