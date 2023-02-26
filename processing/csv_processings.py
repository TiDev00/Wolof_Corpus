import pandas as pd


pd.set_option("display.max_rows", None, "display.max_columns", None)
df_wol_coran = pd.read_csv('../text_scrapped/religious/coran/fr/fr_cor.csv')
print(df_wol_coran)
