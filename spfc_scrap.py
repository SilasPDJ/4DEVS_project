import requests
from bs4 import BeautifulSoup, SoupStrainer
import pandas as pd
from datetime import datetime

# query_selector = "table:nth-child(11)"


def dataframe_spfc(inicio: int, nowyear: int = None, id_comp=51):
    """
    :param inicio: O ano mais antigo p/ iniciar a extrair da competação
    :param nowyear: Até que ano deseja ver os dados?
    :param id_comp: cod competição

    Cria dataframe com os anos selecionados...

    """
    if nowyear is None:
        nowyear = datetime.now().year

    comp_oldest = nowyear - inicio
    if comp_oldest > 50:
        raise ValueError(f"{nowyear} - {inicio} = {comp_oldest}")

    for i in range(1, comp_oldest):
        pass


input(dataframe_spfc(1980))

res = requests.get(
    'https://www.ogol.com.br/equipa_competicao.php?id_comp=51&id_epoca=0&op=&id_equipa=2256&id_jogo=0')
# page=1
# id_comp=51
# id_equipa=2256


only_table_tags = SoupStrainer("table")

btf = BeautifulSoup(res.text, "html.parser", parse_only=only_table_tags)

# apesar do parse_only, é necessário isso para eu desvincular as tb...
btf_tb_read = btf.find_all('table')[7]


df = pd.read_html(str(btf_tb_read))

print(df)


# print(tb_selct)
