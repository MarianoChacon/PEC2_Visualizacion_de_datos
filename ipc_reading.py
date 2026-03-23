import pandas as pd

file_path = r'sh_ipc_03_26.xls'
df_ipc = pd.read_excel(file_path, sheet_name='Variación mensual IPC Nacional', dtype=str)
anotations = df_ipc.iat[2,0]

col_names = df_ipc.iloc[:,2]
col_names_idx = col_names[~(col_names.isna())].index[0]

df_ipc = df_ipc.iloc[col_names_idx:,:]
df_ipc.reset_index(inplace=True, drop = True)
df_ipc.columns = df_ipc.iloc[0,:]
df_ipc = df_ipc.iloc[1:,:]
df_ipc.columns.name = None


df_gba_idx = df_ipc.loc[df_ipc['Total nacional'] == 'Región GBA',].index[0]
df_pampeana_idx = df_ipc.loc[df_ipc['Total nacional'] == 'Región Pampeana',].index[0]
df_no_idx = df_ipc.loc[df_ipc['Total nacional'] == 'Región Noroeste',].index[0]
df_ne_idx = df_ipc.loc[df_ipc['Total nacional'] == 'Región Noreste',].index[0]
df_cuyo_idx = df_ipc.loc[df_ipc['Total nacional'] == 'Región Cuyo',].index[0]
df_patagonia_idx = df_ipc.loc[df_ipc['Total nacional'] == 'Región Patagonia',].index[0]

df_gba = df_ipc.loc[df_gba_idx:df_pampeana_idx,:]
df_gba.reset_index(inplace=True, drop = True)
df_gba.columns = df_gba.iloc[0,:]
df_gba = df_gba.iloc[1:,:]
df_gba.reset_index(inplace=True, drop = True)
df_gba.columns.name = None
df_gba = df_gba.dropna(how='all')
df_gba.rename(columns={'Región GBA':'Concepto'}, inplace=True)
df_gba = df_gba.melt(
    id_vars=['Concepto'],
    var_name='Fecha',
    value_name='IPC'             
)
df_gba = df_gba[~df_gba['IPC'].str.contains('/')]
df_gba['zona'] = 'GBA'

df_pampeana = df_ipc.loc[df_pampeana_idx:df_no_idx,:]
df_pampeana.reset_index(inplace=True, drop = True)
df_pampeana.columns = df_pampeana.iloc[0,:]
df_pampeana = df_pampeana.iloc[1:,:]
df_pampeana.reset_index(inplace=True, drop = True)
df_pampeana.columns.name = None
df_pampeana = df_pampeana.dropna(how='all')
df_pampeana.rename(columns={'Región Pampeana':'Concepto'}, inplace=True)
df_pampeana = df_pampeana.melt(
    id_vars=['Concepto'],
    var_name='Fecha',
    value_name='IPC'             
)
df_pampeana = df_pampeana[~df_pampeana['IPC'].str.contains('/')]
df_pampeana['zona'] = 'Pampeana'


df_no = df_ipc.loc[df_no_idx:df_ne_idx,:]
df_no.reset_index(inplace=True, drop = True)
df_no.columns = df_no.iloc[0,:]
df_no = df_no.iloc[1:,:]
df_no.reset_index(inplace=True, drop = True)
df_no.columns.name = None
df_no = df_no.dropna(how='all')
df_no.rename(columns={'Región Noroeste':'Concepto'}, inplace=True)
df_no = df_no.melt(
    id_vars=['Concepto'],
    var_name='Fecha',
    value_name='IPC'             
)
df_no = df_no[~df_no['IPC'].str.contains('/')]
df_no['zona'] = 'NOA'


df_ne = df_ipc.loc[df_ne_idx:df_cuyo_idx,:]
df_ne.reset_index(inplace=True, drop = True)
df_ne.columns = df_ne.iloc[0,:]
df_ne = df_ne.iloc[1:,:]
df_ne.reset_index(inplace=True, drop = True)
df_ne.columns.name = None
df_ne = df_ne.dropna(how='all')
df_ne.rename(columns={'Región Noreste':'Concepto'}, inplace=True)
df_ne = df_ne.melt(
    id_vars=['Concepto'],
    var_name='Fecha',
    value_name='IPC'             
)
df_ne = df_ne[~df_ne['IPC'].str.contains('/')]
df_ne['zona'] = 'NEA'

df_cuyo = df_ipc.loc[df_cuyo_idx:df_patagonia_idx,:]
df_cuyo.reset_index(inplace=True, drop = True)
df_cuyo.columns = df_cuyo.iloc[0,:]
df_cuyo = df_cuyo.iloc[1:,:]
df_cuyo.reset_index(inplace=True, drop = True)
df_cuyo.columns.name = None
df_cuyo = df_cuyo.dropna(how='all')
df_cuyo.rename(columns={'Región Cuyo':'Concepto'}, inplace=True)
df_cuyo = df_cuyo.melt(
    id_vars=['Concepto'],
    var_name='Fecha',
    value_name='IPC'             
)
df_cuyo = df_cuyo[~df_cuyo['IPC'].str.contains('/')]
df_cuyo['zona'] = 'Cuyo'


df_patagonia = df_ipc.loc[df_patagonia_idx:,:]
df_patagonia.reset_index(inplace=True, drop = True)
df_patagonia.columns = df_patagonia.iloc[0,:]
df_patagonia = df_patagonia.iloc[1:,:]
df_patagonia.reset_index(inplace=True, drop = True)
df_patagonia.columns.name = None
df_patagonia = df_patagonia.dropna(how='all')
df_patagonia.rename(columns={'Región Patagonia':'Concepto'}, inplace=True)
df_patagonia = df_patagonia.melt(
    id_vars=['Concepto'],
    var_name='Fecha',
    value_name='IPC'             
)
df_patagonia = df_patagonia[~df_patagonia['IPC'].str.contains('/')]
df_patagonia['zona'] = 'Patagonia'

df_ipc.rename(columns={'Total nacional':'Concepto'}, inplace=True)
df_ipc = df_ipc.iloc[0:df_gba_idx,:]
df_ipc.reset_index(inplace=True, drop = True)
df_ipc = df_ipc.dropna(how='all')
df_ipc = df_ipc.melt(
    id_vars=['Concepto'],
    var_name='Fecha',
    value_name='IPC'             
)
df_ipc = df_ipc[~df_ipc['IPC'].str.contains('/')]
df_ipc['zona'] = 'Nacional'

df_total = pd.concat([df_ipc, df_gba, df_pampeana, df_no, df_ne, df_cuyo, df_patagonia], axis=0, ignore_index=True).drop_duplicates()
df_total = df_total[~df_total['Concepto'].str.contains('Región')]
df_total['Fecha'] = pd.to_datetime(df_total['Fecha'], dayfirst=True)
df_total['IPC'] = df_total['IPC'].astype(float)
