import pandas as pd

# Lectura 
df = pd.read_excel('Calamar.xlsx')

# Verificación 
print("\nPrimeras 5 filas:")
print(df.head())

try:
    # DataTime
    df['Fecha'] = pd.to_datetime(df['Fecha'], dayfirst=True)
    
    # Filtrar solo Calamar
    municipio_deseado = "Calamar"
    df_filtrado = df[df['Municipio'] == municipio_deseado].copy()
    
    if df_filtrado.empty:
        raise ValueError(f"No se encontraron datos para el municipio: {municipio_deseado}")
    
    # Valores numéricos
    print("\nLimpieza de valores:")
    
    # Convertir a string 
    df_filtrado['Valor'] = df_filtrado['Valor'].astype(str)
    
    # Reemplazar puntos por comas en los decimales
    df_filtrado['Valor'] = df_filtrado['Valor'].str.replace('.', ',', regex=False)
    
    # Convertir a float 
    df_filtrado['Valor'] = pd.to_numeric(df_filtrado['Valor'].str.replace(',', '.'), errors='coerce')
    
    # >15000
    total_antes = len(df_filtrado)
    df_filtrado = df_filtrado[df_filtrado['Valor'] <= 15000]
    total_despues = len(df_filtrado)
    
    print(f"Valores eliminados por ser >15,000: {total_antes - total_despues}")
    print(f"Valores con formato incorrecto eliminados: {df_filtrado['Valor'].isna().sum()}")
    
    # Eliminar filas con valores NaN 
    df_filtrado = df_filtrado.dropna(subset=['Valor'])
    
    # Listas
    fechas_lista = df_filtrado['Fecha'].dt.strftime('%d/%m/%Y').tolist()
    valores_lista = df_filtrado['Valor'].tolist()
    
    # Resultados finales
    print("\nResultados después de la limpieza:")
    print(f"\nMunicipio: {municipio_deseado}")
    print(f"Total registros válidos: {len(valores_lista)}")
    print("\nMuestra de datos limpios:")
    print("\nPrimeras 5 fechas y valores:")
    for i in range(min(5, len(valores_lista))):
        print(f"{fechas_lista[i]}: {valores_lista[i]:.2f}")
    print("\nÚltimas 5 fechas y valores:")
    for i in range(max(0, len(valores_lista)-5), len(valores_lista)):
        print(f"{fechas_lista[i]}: {valores_lista[i]:.2f}")
    
    # Diccionario con los datos limpios (por si las moscas)
    datos_limpios = {
        'municipio': municipio_deseado,
        'fechas': fechas_lista,
        'valores': valores_lista,
        'valores_promedio': sum(valores_lista)/len(valores_lista) if valores_lista else 0
    }
    
    print("\nResumen estadístico:")
    print(f"- Cantidad datos: {len(valores_lista)}")
    print(f"- Valor máximo: {max(valores_lista):.2f}" if valores_lista else "N/A")
    print(f"- Valor mínimo: {min(valores_lista):.2f}" if valores_lista else "N/A")
    print(f"- Promedio: {datos_limpios['valores_promedio']:.2f}")

except KeyError as e:
    print(f"\nError: No se encontró la columna {str(e)}")
    print("Columnas disponibles:", df.columns.tolist())
except Exception as e:
    print(f"\nOcurrió un error inesperado: {str(e)}")