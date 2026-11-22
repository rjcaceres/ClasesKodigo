import pandas as pd


def calcular_metricas_ventas(dataframe: pd.DataFrame) -> dict:
    """
    Calcula métricas principales de ventas.

    Args:
        dataframe (pd.DataFrame): Tabla con la columna
            numérica 'ventas' sin valores nulos.

    Returns:
        dict: Total, promedio y cantidad de ventas.

    Raises:
        ValueError: Si falta la columna 'ventas'.
    """
    if "ventas" not in dataframe.columns:
        raise ValueError("Falta la columna ventas")

    if dataframe.empty:
        return {
            "total": 0,
            "promedio": 0,
            "cantidad": 0,
        }

    total = dataframe["ventas"].sum()
    cantidad = len(dataframe)
    promedio = total / cantidad

    return {
        "total": total,
        "promedio": promedio,
        "cantidad": cantidad,
    }