import pandas as pd


pd.set_option("display.max_rows", None, "display.max_columns", None)
df_fr_cor = pd.read_csv('../text_scrapped/religious/coran/fr/fr_cor.csv')
df_wol_cor = pd.read_csv('../text_scrapped/religious/coran/wol/wol_cor.csv')

print(df_fr_cor.head(5))
print(df_wol_cor.head(5))
