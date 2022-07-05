def create_data_lake():
    """Cree el data lake con sus capas.

    Esta función debe crear la carpeta `data_lake` en la raiz del proyecto. El data lake contiene
    las siguientes subcarpetas:

    ```
    .
    |
    \___ data_lake/
         |___ landing/
         |___ raw/
         |___ cleansed/
         \___ business/
              |___ reports/
              |    |___ figures/
              |___ features/
              |___ forecasts/

    ```


    """

    """"creación del data lake del proyecto, que almancenará los datos de los modelos"""

    import os
    import sys
    
    os.mkdir('data_lake')

    raiz_ppal = 'data_lake/'

    nivel_1 = ['landing', 'raw', 'cleansed', 'business']

    for items in nivel_1:
        path = os.path.join(raiz_ppal, items)
        os.mkdir(path)

    raiz_business = 'data_lake/business'

    nivel_2 = ['reports', 'features', 'forecasts']

    for items in nivel_2:
        path = os.path.join(raiz_business, items)
        os.mkdir(path)
    
    nivel_3 = 'figures'
    raiz_business_reports = 'data_lake/business/reports/'
    path = os.path.join(raiz_business_reports, nivel_3)
    os.mkdir(path)

    return


   #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    create_data_lake()

    doctest.testmod()
    
