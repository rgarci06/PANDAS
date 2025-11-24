import pandas as pd
import os

def obrir_fitxer(nom_carpeta: str, fitxer: str):
    """Obre un fitxer CSV i el retorna com a DataFrame."""
    
    ruta = os.path.join(os.path.dirname(__file__), nom_carpeta, fitxer)

    if not os.path.exists(ruta):
        print("Error: Fitxer no trobat")
        return 0

    return pd.read_csv(ruta)
