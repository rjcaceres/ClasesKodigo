import pandas as pd

from src.procesamiento import calcular_metricas_ventas


def test_calculo_ventas():
    # Arrange
    datos = pd.DataFrame({
        "ventas": [100, 250, 150, 300, 200]
    })

    # Act
    resultado = calcular_metricas_ventas(datos)

    # Assert
    assert resultado["total"] == 1000
    assert resultado["promedio"] == 200
    assert resultado["cantidad"] == 5


def test_dataframe_vacio():
    # Arrange: existe la columna, sin registros
    datos = pd.DataFrame({
        "ventas": pd.Series(dtype="float64")
    })

    # Act
    resultado = calcular_metricas_ventas(datos)

    # Assert
    assert resultado["total"] == 0
    assert resultado["promedio"] == 0
    assert resultado["cantidad"] == 0