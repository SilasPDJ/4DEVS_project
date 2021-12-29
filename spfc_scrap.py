import requests
from bs4 import BeautifulSoup, SoupStrainer
import pandas as pd

query_selector = "#page > div.fake_container > div.page > table:nth-child(11)"
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
