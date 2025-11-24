import pandas as pd
import os

def obrir_fitxer(nom_carpeta: str, fitxer: str): # Amb aixo el que faig es fer que posi el nom de la carpeta i el fitxer per trobar-lo
    
    ruta = os.path.join(os.path.dirname(__file__), nom_carpeta, fitxer) # Aixo es per obtenir la ruta completa del fitxer

    if not os.path.exists(ruta):
        print("Error: Fitxer no trobat")
        return 0

    return pd.read_csv(ruta)
