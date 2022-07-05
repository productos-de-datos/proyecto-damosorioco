import imp
"""se extrae del dataframe los datos y se les realiza una transformación logarítmica, adicionalmente se crea una que será el precio atrás 12 meses del punto evaluado en la serie logarítmica"""

def make_features():
    """Prepara datos para pronóstico.

    Cree el archivo data_lake/business/features/precios-diarios.csv. Este
    archivo contiene la información para pronosticar los precios diarios de la
    electricidad con base en los precios de los días pasados. Las columnas
    correspoden a las variables explicativas del modelo, y debe incluir,
    adicionalmente, la fecha del precio que se desea pronosticar y el precio
    que se desea pronosticar (variable dependiente).

    En la carpeta notebooks/ cree los notebooks de jupyter necesarios para
    analizar y determinar las variables explicativas del modelo.

    """
    import pandas as pd
    import numpy as np

    df_daily_prices = pd.read_csv('data_lake/business/precios-diarios.csv')
    df_daily_prices['log_precio'] = np.log(df_daily_prices['precio'])
    df_daily_prices['precio_12'] = df_daily_prices.precio.shift(12)
    df_daily_prices['log_precio_12'] = np.log(df_daily_prices['precio_12'])
    df_daily_prices.to_csv('data_lake/business/features/precios-diarios.csv', index= False)

    return

import pytest
def test_make_features():

    """prueba de las características del modelo"""

    import pandas as pd

    make_features()

    df_test_features = pd.read_csv('data_lake/business/features/precios-diarios.csv')

    assert df_test_features.empty is False


    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    make_features()
    doctest.testmod()
