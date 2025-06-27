#Visualizador de evolución de campañas.

import pandas as pd
import matplotlib.pyplot as plt

# Leer archivo Excel
#No olvidar: el excel original está en la carpeta de apps, pero la que crea esta
#app está en entorno1, igual que los gráficos guardados y el nuevo excel.
df = pd.read_excel("/Users/marcelatroncosocortes/Desktop/Python/aplicaciones marcela - facil/GITHUB CV/campanas.xlsx")

# Calcular métricas
df["ROAS"] = df["Ingresos"] / df["Inversion"]
df["CPA"] = df["Inversion"] / df["Conversiones"]

# Mostrar tabla por consola (opcional)
print("==== Datos de campañas ====")
print(df)

# Graficar Clicks y Conversiones
plt.figure(figsize=(10, 6))
plt.plot(df["Semana"], df["Clicks"], marker="o", label="Clicks")
plt.plot(df["Semana"], df["Conversiones"], marker="s", label="Conversiones")

plt.title("Evolución de Clicks y Conversiones", fontsize=16, fontweight="bold")
plt.xlabel("Semana", fontsize=14)
plt.ylabel("Cantidad", fontsize=14)
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("grafico_clicks_conversiones.png")
plt.show()

# Graficar ROAS y CPA (en otra figura)
plt.figure(figsize=(10, 6))
plt.plot(df["Semana"], df["ROAS"], marker="o", color="green", label="ROAS")
plt.plot(df["Semana"], df["CPA"], marker="s", color="red", label="CPA")

plt.title("Métricas Financieras: ROAS vs CPA", fontsize=16, fontweight="bold")
plt.xlabel("Semana",fontsize=14)
plt.ylabel("Valor", fontsize=14)
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("grafico_roas_cpa.png")
plt.show()

df.to_excel("campanas_con_metricas.xlsx", index=False)