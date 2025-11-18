# ? PRACTICA 1 - RGARCI

from funcions import obrir_fitxer

jocs=obrir_fitxer("../data", "vgsales.csv")

# ? Canvia el nom de la columna Global_Sales a Total_Sales i mostra les primeres 5 files.
print("\n--- Canvi nom columna Global_Sales a Total_Sales ---")
canvi_nom = jocs.rename(columns={"Global_Sales": "Total_Sales"})
print(canvi_nom.head(5))
# Aqui el que he fet ha sigut crear una variable per canviar el nom, he utilitzat el reaname per canviar el nom de la columna i per canviar el nom he agut de seleccionar-la amb {(aquest es el parametre que vull canviar) -> "Global_Sales": "Total_Sales" <- (aquest es el nom al que vull canviar)} i  al print he utilitzat el head(5) per mostrar les 5 primeres files.
# ? Compta quants jocs hi ha per cada plataforma.
print("\n--- Comptar jocs per plataforma ---")
jocs_plataforma = jocs['Platform'].value_counts()
print(jocs_plataforma)
# Aqui he fet la variable jocs_plataforma on he utilitzat el value_counts que serveix per comptar els valors de la columna que li diguis, en aquest cas he utilitzat la columna Platform per comptar quants jocs hi ha per cada plataforma.
# ? Compta quants jocs hi ha per gènere i ordena'ls de menor a major.
print("\n--- Comptar jocs per gènere ordenats de menor a major ---")
jocs_genere = jocs['Genre'].value_counts().sort_values()
print(jocs_genere)
# Aqui he fet la variable jocs_genere on he utilitzat el value_counts per comptar els valors de la columna Genre i despres he utilitzat el sort_values() per ordenar-los de menor a major.
# ? Quants jocs es van llançar cada any? 
print("\n--- Comptar jocs per any ---")
jocs_any = jocs['Year'].value_counts().sort_index()
print(jocs_any)
# Aqui he fet la variable jocs_any on he utilitzat el value_counts per comptar els valors de la columna Year i despres he utilitzat el sort_index() per ordenar-los per any. La diferencia entre sort_values() i sort_index() es que el primer ordena per els valors que son els jocs comptats i el segon ordena per l'index que en aquest cas son els anys.
# ? Mostra els 5 jocs més venuts a USA.
print("\n--- 5 jocs més venuts a USA ---")
jocs_usa = jocs.sort_values('NA_Sales', ascending=False).head(5)
print(jocs_usa)
# Aqui he fet la variable jocs_usa on he utilitzat el sort_values() i dins he possat la columna NA_Sales per ordenar els jocs per les vendes a USA de major a menor amb el ascending=False si volguessim ordenar de menor a major seria ascending=True. Despres he utilitzat el head(5) per mostrar els 5 primers jocs mes venuts a USA.
# ? Quina plataforma ha venut més en total?
print("\n--- Plataforma que ha venut més en total ---")
plataforma_mes_vendes = jocs.groupby('Platform')['Global_Sales'].sum().idxmax()
print(plataforma_mes_vendes)
# Aqui el que he fet ha sigut crear la variable plataforma_mes_vendes on he utilitzat el groupby per agrupar els jocs per plataforma i despres he seleccionat la columna Global_Sales per sumar les vendes totals per cada plataforma amb el sum(). Finalment he utilitzat l'idxmax() per mostrar la plataforma amb més vendes totals.
# ? Calcula la suma de vendes per cada regió (NA_Sales, EU_Sales, JP_Sales, Other_Sales).
print("\n--- Suma de vendes per cada regió ---")
suma_vendes_regions = jocs[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum()
print(suma_vendes_regions)
# Aqui el que he fet a sigut seleccionar les columnes NA_Sales, EU_Sales, JP_Sales i Other_Sales i despres he utilitzat el sum() per sumar les dades i aixi tindre la suma de vendes.
# ? Quin editor ha publicat més jocs i el nombre?
print("\n--- Editor que ha publicat més jocs i el nombre ---")
editor_mes_jocs = jocs['Publisher'].value_counts().idxmax()
nombre_jocs_editor = jocs['Publisher'].value_counts().max()
print(f"Editor: {editor_mes_jocs}, Nombre de jocs: {nombre_jocs_editor}")
# 
# ? Filtra els jocs del gènere 'Action' i mostra el joc que ha venut més en l'àmbit global.

# ? La mitjana de vendes globals en valor absolut