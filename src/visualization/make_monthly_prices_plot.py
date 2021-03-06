def make_monthly_prices_plot():
    """Crea un grafico de lines que representa los precios promedios diarios.

    Usando el archivo data_lake/business/precios-diarios.csv, crea un grafico de
    lines que representa los precios promedios diarios.

    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/daily_prices.png.

    """
    #raise NotImplementedError("Implementar esta función")


    """importe de librerías"""

    import matplotlib
    import matplotlib.pyplot as plt
    import pandas as pd

    """creación de gráficos"""

    df_monthly_prices = pd.read_csv('data_lake/business/precios-mensuales.csv')
    df_monthly_prices['fecha'] = pd.to_datetime(df_monthly_prices["fecha"])

    x = df_monthly_prices['fecha']
    y = df_monthly_prices['precio']

    plt.figure(figsize=(12, 8)) 
    plt.plot(x, y, label='Prom Mensual') 
    plt.title('Precio Prom Mensual') 
    plt.xlabel('Fecha') 
    plt.ylabel('Precio') 
    plt.savefig("data_lake/business/reports/figures/monthly_prices.png") 

    return


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    make_monthly_prices_plot()
