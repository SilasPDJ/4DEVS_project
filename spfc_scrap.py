import requests
from bs4 import BeautifulSoup, SoupStrainer
import pandas as pd
from datetime import datetime

from requests.models import to_native_string

# query_selector = "table:nth-child(11)"


def dataframe_spfc(inicio: int, nowyear: int = None, id_comp=51):
    """
    :param inicio: O ano mais antigo p/ iniciar a extrair da competação
    :param nowyear: Até que ano deseja ver os dados?
    :param id_comp: cod competição

    Cria dataframe com os anos selecionados...

    """
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}

    if nowyear is None:
        nowyear = datetime.now().year

    comp_oldest = nowyear - inicio
    if comp_oldest > 50:
        raise ValueError(f"{nowyear} - {inicio} = {comp_oldest}")

    # __yearcont = nowyear
    for page in range(1, comp_oldest+1):
        res = requests.get(
            f'https://www.ogol.com.br/equipa_competicao.php?id_comp=51&id_epoca=0&op=&id_equipa=2256&id_jogo=0&page={page}')
        only_table_tags = SoupStrainer("table")
        btf = BeautifulSoup(res.text, "html.parser",
                            parse_only=only_table_tags)
        # apesar do parse_only, é necessário isso para eu desvincular as tb...
        btf_tb_read = btf.find_all('table')[7]
        df = pd.read_html(str(btf_tb_read))
        yield df[0]
        # __yearcont -= 1


pd.concat(list(dataframe_spfc(2019))).to_excel("football.xlsx", index=False)

# pd.concat(listdfs, ).to_excel("football.xls", ycont, index=False)
