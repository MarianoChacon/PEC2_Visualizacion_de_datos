import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import PercentFormatter
import matplotlib.font_manager as fm
import matplotlib.patches as patches

ruta_fuente = r'./fonts/Libre_Franklin/static/LibreFranklin-Regular.ttf'
mi_fuente = fm.FontProperties(fname=ruta_fuente)
fuente_bold = fm.FontProperties(fname=r'./fonts/Libre_Franklin/static/LibreFranklin-Bold.ttf')
fuente_cursiva = fm.FontProperties(fname=r'./fonts/Libre_Franklin/static/LibreFranklin-Italic.ttf')
fuente_light = fm.FontProperties(fname=r'./fonts/Libre_Franklin/static/LibreFranklin-Light.ttf')

df_gdp = pd.read_csv('Data_GDP.csv', sep=';', decimal=',')
df_gdp = df_gdp[~(df_gdp.GDP_comonent =='Final consumption expenditure, gross capital formation and exports of goods and services')]
df_gdp = df_gdp.sort_values(by='GEO (Labels)', ascending=False)
fig, ax = plt.subplots(figsize=(12, 8))

consumption = df_gdp.loc[df_gdp['GDP_comonent'] == 'Final consumption expenditure',['Perc']].values.flatten()
capital = df_gdp.loc[df_gdp['GDP_comonent'] == 'Gross capital formation',['Perc']].values.flatten()
exports = df_gdp.loc[df_gdp['GDP_comonent'] == 'Exports of goods and services',['Perc']].values.flatten()
comp_label = [str(round(i*100,1)) + '%' for i in consumption]
cap_label = [str(round(i*100,1)) + '%' for i in capital]
expo_label = [str(round(i*100,1)) + '%' for i in exports]
cons = ax.bar(df_gdp['GEO (Labels)'].unique(), consumption,width = 0.7, bottom = np.zeros(5), color='#E63946', label = 'Consumo',linewidth=0.5, edgecolor = 'white')
cons_bar = ax.bar_label(cons, labels=comp_label, label_type='center',fontproperties=mi_fuente)
expo =ax.bar(df_gdp['GEO (Labels)'].unique(),exports,width = 0.7, bottom = consumption, color='#457B9D', label = 'Exportaciones',linewidth=0.5, edgecolor = 'white')
expo_bar = ax.bar_label(expo, labels=expo_label, label_type='center',fontproperties=mi_fuente)
cap = ax.bar(df_gdp['GEO (Labels)'].unique(),capital,width =0.7, bottom = consumption + exports, color='#2A9D8F', label = 'Capital',linewidth=0.5, edgecolor = 'white')
cap_bar = ax.bar_label(cap, labels=cap_label, label_type='center',fontproperties=mi_fuente)
ax.yaxis.set_major_formatter(PercentFormatter(xmax=1))
for bloque in [cons_bar, expo_bar, cap_bar]:
    for i in range(1,5):
        expo = bloque[i]
        expo.set_fontproperties(fuente_light)

    expo_spain = bloque[0]
    expo_spain.set_fontproperties(fuente_bold)
    
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(mi_fuente)

for label in ax.get_xticklabels():
    if label.get_text() == 'Spain':
        label.set_fontproperties(fuente_bold)
        label.set_fontsize(14)
    else:
        label.set_fontproperties(fuente_light)
        label.set_fontsize(12)
    

ax.tick_params(axis='both', which='both', length=0) 
ax.yaxis.grid(True, linestyle='--', alpha=0.3, color='gray')

for spine in ['top', 'right', 'left']:
    ax.spines[spine].set_visible(False)
leg = ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15),ncol=3,prop=mi_fuente, frameon=False)


plt.suptitle('Destino del PIB de las principales economías europeas',fontproperties=fuente_bold, fontsize=18, fontweight='bold',horizontalalignment='left',x=0.125,y=0.95)
ax.set_title('Porcentajes calculado en base al PIB en euros corrientes - Año 2025', fontproperties=mi_fuente, fontsize=14, color='gray',loc='left',pad=8)
ax.annotate('Fuente: Eurostat.', 
            xy=(1, -0.25), 
            xycoords='axes fraction', 
            ha='right', 
            va='top', 
            fontsize=9, 
            color='gray', 
            fontproperties=fuente_cursiva)
plt.subplots_adjust(bottom=0.25)
#fig.set_facecolor('#F5F5DC') 
ax.set_facecolor('#F0F2F5')

plt.savefig('Stacked_bar.png',dpi=300 )
#plt.show()
