"""
Módulo de ingestión de datos.
-------------------------------------------------------------------------------
Descarga de los datos a la carpeta landing, se importan los datos desde la URL desde 1995 a 2022


"""


from gettext import install


def ingest_data():
    """Ingeste los datos externos a la capa landing del data lake.

    Del repositorio jdvelasq/datalabs/precio_bolsa_nacional/xls/ descarge los
    archivos de precios de bolsa nacional en formato xls a la capa landing. La
    descarga debe realizarse usando únicamente funciones de Python.

    """
    import os
    import pandas as pd
    
    
    import xlwt

    inicio = 1995

    fin = 2022

    ruta_repositorio = 'https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls'

    ruta_destino = 'data_lake/landing'

    for years in range(inicio, fin):

        try:

            files = pd.read_excel(ruta_repositorio + '/' + str(years) + 'xlsx?raw=true')
            files.to_excel(ruta_destino  + str(years) + '.xlsx', index=None, header=True)
        except:

            files = pd.read_excel(ruta_repositorio + '/' + str(years) + '.xls?raw=true')
            files.to_excel(ruta_destino + str(years) + '.xls', index=None, header=True)

    return







    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    
    ingest_data()
    import doctest
    
    doctest.testmod()
