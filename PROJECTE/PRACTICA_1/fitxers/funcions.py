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

    
    if not nom_carpeta:
        FITXER=os.path.join(DIRECTORI, fitxer)
    else:
        FITXER=os.path.join(DIRECTORI, nom_carpeta, fitxer)
    if not os.path.isfile(FITXER):
        raise FileNotFoundError("Error en el fitxer")
    dataframe=pd.read_csv(FITXER, encoding="utf-8")
    # amb empty validem si té fila true si està buit
    if dataframe.empty:
        return None
    return dataframe

