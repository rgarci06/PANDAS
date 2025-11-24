# ? PRACTICA 1 - RGARCI

from funcions import obrir_fitxer

jocs=obrir_fitxer("../data", "vgsales.csv")

# ? Canvia el nom de la columna Total_Sales a Total_Sales i mostra les primeres 5 files.
print("\n--- Canvi nom columna Global_Sales a Total_Sales ---")
canvi_nom = jocs.rename(columns={"Global_Sales": "Total_Sales"}, inplace = True)
print(jocs.head(5))
# Aqui he utilitzat el metode rename() per canviar el nom de la columna Global_Sales a Total_Sales i aixi es canvia per a totes les consultes següents. Despres he utilitzat el metode head(5) per mostrar les primeres 5 files del DataFrame.

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
plataforma_mes_vendes = jocs.groupby('Platform')['Total_Sales'].sum().idxmax()
print(plataforma_mes_vendes)
# Aqui el que he fet ha sigut crear la variable plataforma_mes_vendes on he utilitzat el groupby per agrupar els jocs per plataforma i despres he seleccionat la columna Total_Sales per sumar les vendes totals per cada plataforma amb el sum(). Finalment he utilitzat l'idxmax() per mostrar la plataforma amb més vendes totals.

# ? Calcula la suma de vendes per cada regió (NA_Sales, EU_Sales, JP_Sales, Other_Sales).
print("\n--- Suma de vendes per cada regió ---")
suma_vendes_regions = jocs[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum()
print(suma_vendes_regions)
# Aqui el que he fet a sigut seleccionar les columnes NA_Sales, EU_Sales, JP_Sales i Other_Sales i despres he utilitzat el sum() per sumar les dades i aixi tindre la suma de vendes.

# ? Quin editor ha publicat més jocs i el nombre?
print("\n--- Editor que ha publicat més jocs i el nombre ---")
nom_editor = jocs['Publisher'].value_counts().idxmax()
nombre_jocs = jocs['Publisher'].value_counts().max()
print(f"{nom_editor} amb {nombre_jocs} jocs\n")
# Aqui he fet la variable nom_editor on he utilitzat el value_counts() per comptar els valors de la columna Publisher i despres he utilitzat l'idxmax() per mostrar l'editor que ha publicat més jocs. Despres he fet la variable nombre_jocs on he utilitzat el value_counts() per comptar els valors de la columna Publisher i per últim he utilitzat el max() per mostrar el nombre de jocs que ha publicat l'editor que ha publicat més jocs.

# ? Filtra els jocs del gènere 'Action' i mostra el joc que ha venut més en l'àmbit global.
print("\n--- Joc d'Acció més venut globalment ---")
joc_accio_mes_vendes = jocs[jocs['Genre'] == 'Action'].sort_values('Total_Sales', ascending=False).head(1)
print(joc_accio_mes_vendes)
# Aqui he fet la variable joc_accio_mes_vendes on he filtrat els jocs del gènere Action utilitzant jocs[jocs['Genre'] == 'Action'] i despres he utilitzat el sort_values() per ordenar els jocs per la columna Total_Sales de major a menor amb el ascending=False. Finalment he utilitzat el head(1) per mostrar el joc d'acció més venut globalment.

# ? La mitjana de vendes globals en valor absolut
print("\n--- Mitjana de vendes globals en valor absolut ---")
mitjana_vendes_globals = jocs['Total_Sales'].mean()
print(abs(mitjana_vendes_globals))
# Aqui he fet la variable mitjana_vendes_globals on he utilitzat el mean() per calcular la mitjana de les vendes globals de la columna Total_Sales i despres he utilitzat la funcio abs() per mostrar el valor absolut de la mitjana.