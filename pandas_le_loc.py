import pandas as pd
import os
import json
data_folder = 'dados_json'


def get_onlyfiles(_): return os.path.isfile(_)


def getloc(kwd, cont): return eval(f"df.loc[{cont}].{kwd}")


key_wanted = ['nome', 'data_nasc', 'sexo', 'email', 'altura', 'peso']

# main_data = list()

dataframes_list = []


files = [os.path.join(data_folder, f) for f in os.listdir(data_folder)]
files = list(filter(get_onlyfiles, files))

for file in files[:1]:
    df = pd.read_json(file)
    df_tam = len(df.index)

    # [print(df.loc[0][0])]
    newdf = pd.DataFrame(columns=key_wanted)
    for cnt in range(1, 10):
        eachdata = [getloc(k, cnt) for k in key_wanted]
        # print(main_data)
        eachdict = {k: v for k, v in zip(key_wanted, eachdata)}
        # index significa a quantidade
        dataframes_list.append(pd.DataFrame(eachdict, index=[0]))

dale = pd.concat(dataframes_list)

dale.to_excel(
    "teste.xlsx", "nome", index=False)
