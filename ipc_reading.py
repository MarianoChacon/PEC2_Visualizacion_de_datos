import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from datetime import datetime as dtm
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

ruta_fuente = r'./fonts/Libre_Franklin/static/LibreFranklin-Regular.ttf'
mi_fuente = fm.FontProperties(fname=ruta_fuente)
fuente_bold = fm.FontProperties(fname=r'./fonts/Libre_Franklin/static/LibreFranklin-Bold.ttf')
fuente_cursiva = fm.FontProperties(fname=r'./fonts/Libre_Franklin/static/LibreFranklin-Italic.ttf')
fuente_light = fm.FontProperties(fname=r'./fonts/Libre_Franklin/static/LibreFranklin-Light.ttf')

file_path = r'sh_ipc_03_26.xls'
df_ipc = pd.read_excel(file_path, sheet_name='Variación mensual IPC Nacional', dtype=str)
anotations = df_ipc.iat[2,0]

col_names = df_ipc.iloc[:,2]
col_names_idx = col_names[~col_names.isna()].index[0]

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
df_gba = df_gba[~(df_gba['IPC'].str.contains('/') | df_gba['IPC'].str.contains('/'))]
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
df_total = df_total.loc[(df_total['Concepto'] != 'Nivel general y divisiones COICOP') & (df_total['Concepto'] != 'Categorías '),:]
df_total = df_total.dropna(how='any')

df_total_graph = df_total.loc[(df_total['zona'] != 'Nacional') ,:] # & (df_total['zona'] == 'Nacional')
# conceptos = ['Alimentos y bebidas no alcohólicas',
#             'Bebidas alcohólicas y tabaco',
#             'Prendas de vestir y calzado',
#             'Vivienda, agua, electricidad, gas y otros combustibles',
#             'Equipamiento y mantenimiento del hogar',
#             'Salud',
#             'Transporte',
#             'Comunicación',
#             'Recreación y cultura',
#             'Educación',
#             'Restaurantes y hoteles',
#             'Bienes y servicios varios',
#             'Núcleo']
#conceptos = ['Núcleo','Regulados','Bienes','Servicios']
conceptos = ['Bienes','Servicios']
#df_total_graph['colores'] = df_total_graph['Concepto'].apply(lambda x: x if x=='Núcleo' else 'No núcleo')
df_total_graph['Año'] = df_total_graph['Fecha'].dt.year
df_total_graph = df_total_graph.loc[df_total_graph['Concepto'].isin(conceptos),:]
formato = "%d/%m/%Y"
df_total_graph['Presidencia'] = df_total_graph['Fecha'].apply(lambda x: 'Macri' if x <= dtm.strptime('09/12/2019',formato) else ('Fernández' if (x > dtm.strptime('09/12/2019',formato)) and (x <= dtm.strptime('10/12/2023',formato)) else 'Milei'))

colores= {'Bienes': "#727475", 'Servicios': "#e74c3c"}
fig, ax = plt.subplots(figsize=(12, 8))
sns.swarmplot(data = df_total_graph, x = 'Año', y = 'IPC', size = 4, hue='Concepto',legend=True,palette=colores)#, hue = df_total['zona'])
ax.set_ybound(0,31)
ax.set_xlim(right=9.5)
ax.spines['left'].set_position(('data', -0.5))

plt.axvspan(-0.5, 3.5, color='#ffed00', alpha=0.3)
plt.axvspan(3.5, 7.5, color='#00AEEF', alpha=0.3)
plt.axvspan(7.5, 9.5, color='#7d3291', alpha=0.3)
ax.annotate('Mauricio Macri',xy=[1,28],fontproperties=mi_fuente,fontsize=12,color="#978d04")
ax.annotate('Alberto Fernández',xy=[4,28],fontproperties=mi_fuente, fontsize=12,color="#03445C")
ax.annotate('Javier Milei',xy=[8,28],fontproperties=mi_fuente, fontsize=12,color="#440954")
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15),ncol=3,prop=mi_fuente, frameon=True)

for tick in ax.get_xticklabels():
    if tick.get_text() in ['2020', '2025']:
        #tick.set_fontweight('bold')
        tick.set_fontproperties(fuente_bold)
        tick.set_fontsize(14)

ax.annotate('', 
            xy=(8, 6),
            xytext=(3, 6),
            arrowprops=dict(
                arrowstyle='->',
                connectionstyle='arc3,rad=-0.4',
                color='black',
                lw=1.5,
                linestyle='--'
            ))
icono_path = "icono_exch.png"
imagen = plt.imread(icono_path)
imagebox = OffsetImage(imagen, zoom=0.04)
ab = AnnotationBbox(imagebox, (5, 15.3), frameon=False)
ax.add_artist(ab)

plt.suptitle('Cambio en la composición de la inflación Argentina (2017 - 2026)',fontproperties=fuente_bold, fontsize=18, fontweight='bold',horizontalalignment='left',x=0.095,y=0.94)
ax.set_title('Datos correspondientes al agregado nacional', fontproperties=mi_fuente, fontsize=14, color='gray',loc='left',pad=8)
ax.annotate('Fuente: INDEC - Argentina.', 
            xy=(1, -0.25), 
            xycoords='axes fraction', 
            ha='right', 
            va='top', 
            fontsize=9, 
            color='gray', 
            fontproperties=fuente_cursiva)


fig.tight_layout()
plt.savefig('Beeswarm_plot.png')
