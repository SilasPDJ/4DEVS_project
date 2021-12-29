# 4DEVS_project

4devs website scrapping project

### anotações

-   \# btf = BeautifulSoup(res.text, "html.parser")
-   \# tb = btf.findAll('table')[7]
-   \# tb_selct = btf.select(
-   \# "table:nth-child(11)")

## multiple sheets on workbook

1. \# df and yearcont are in loop

    1. [ ] \# df[0].to_excel("football.xlsx", str(\_\_yearcont), index=False)

        - ~~somente assim não é possível escrever várias sheets diferentes~~

    1. [x] \# xwriter = pd.ExcelWriter('myworkbook.xlsx', engine='xlsxwriter')
    1. [x] df.to_excel(xwriter, sheet_name=yearcont)

### **pandas** at vs lot

#### https://stackoverflow.com/questions/28757389/pandas-loc-vs-iloc-vs-at-vs-iat
