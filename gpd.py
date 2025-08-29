import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.odr as odr

# --- Carga de datos ---
gdp_data = pd.read_excel('gpd_cte.xls')
poverty_data = pd.read_excel('informe.xlsx') # Pobreza semestral entre 2016 y 2024

# --- Preprocesamiento de datos de pobreza ---
# Extrae la serie de pobreza y la convierte a tipo numérico
poverty_series = pd.to_numeric(poverty_data.iloc[5, 1:], errors='coerce')

# Cálculo del promedio de pobreza anual a partir de datos semestrales
annual_poverty = [poverty_series[0]]
for i in range(1, len(poverty_series) - 1, 2):
    annual_poverty.append((poverty_series[i] + poverty_series[i+1]) / 2)

# --- Preparación de datos para el ploteo ---
years = list(range(2016, 2025))
gdp_per_capita = gdp_data.iloc[13, 66-6:]

# --- Ploteo ---
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)
fig.suptitle('Pobreza y PIB per Cápita en Argentina (2016-2024)')

ax1.set_ylabel('Pobreza [%]')
ax2.set_ylabel('PIB per Cápita [MM USD]')
ax2.set_xlabel('Años')

ax1.plot(years, annual_poverty, 'o', color='red')
ax2.plot(years, gdp_per_capita, 'o')

fig.tight_layout()
plt.show()
