import pandas as pd
import os

# funció per fer dataFrame ----------------------------------------------------------------------

def obrir_fitxer(nom_carpeta:str, fitxer:str):
    """Funció per buscar fitxer i transformar-lo en DataFrame

    Args:
        nom_carpeta (str): carpeta
        fitxer (str): fitxer csv que volem transformar

    Returns:
        DataFrame o 0 en cas d'error
    """
    DIRECTORI=os.path.dirname(__file__)

    RUTA=os.path.join(DIRECTORI, nom_carpeta, fitxer)
    try:
        df=pd.read_csv(RUTA)
        return df
    except FileNotFoundError:
        print("Error: Fitxer no trobat")
        return 0

