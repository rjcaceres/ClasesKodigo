# Control de Ventas

Proyecto académico en python para caluclar métricas básicas de ventas, con documentación y pruebas.

## Herramientas

Python
Pandas
Pytest
Git

## Estructura

- `src/`: función de procesamiento.
- `tests/`: pruebas unitarias.
- `data/`: CSV local de muestra, ignorado por Git.

## Instalación

Crear un entorno virtual:

```powershell
python -m venv .venv
```

Activarlo (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

Instalar paquetes:

```powershell
python -m pip install -r requirements.txt
```

## Ejecutar pruebas

Desde la raíz del proyecto:

```powershell
python -m pytest -v
```

## Contrato de la función

`calcular_metricas_ventas(dataframe)` recibe una tabla
con columna numérica `ventas` y devuelve un diccionario
con `total`, `promedio` y `cantidad`.

Para un DataFrame vacío con esa columna, devuelve ceros.
Si falta la columna `ventas`, genera `ValueError`.

## Resultados esperados

Para 100, 250, 150, 300 y 200: total 1000,
promedio 200 y cantidad 5.

El archivo CSV local no se incluye en Git. Las pruebas
crean los datos directamente en memoria.