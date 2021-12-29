import pandas as pd
import os
import json
data_folder = 'dados_json'


def get_onlyfiles(_):
    return os.path.isfile(_)


files = [os.path.join(data_folder, f) for f in os.listdir(data_folder)]
files = list(filter(get_onlyfiles, files))


key_wanted = ['nome', 'data_nasc', 'sexo', 'email', 'altura', 'peso']
main_data = []

for file in files[:1]:
    # with open(file) as f:
    #     fileread = json.load(f)

    df = pd.read_json(file)
    df_tam = len(df.index)

    # print(df.columns)

    # print(df.head(10)) #mostra 10 linhas
    # print(df.loc[0:5])
    for cont in range(df_tam):
        eachdata = [df.at[cont, d] for d in key_wanted]
        eachdict = {a: b for (a, b) in zip(key_wanted, eachdata)}

        main_data.append(eachdict.copy())

        print(eachdict["nome"])

    # for test in df.loc[0]:
    #     print(test)
print(len(main_data))
print(main_data)
