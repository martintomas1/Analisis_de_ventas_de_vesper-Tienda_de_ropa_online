import pandas as pd
import re
import sys
from collections import Counter

df1=pd.read_excel('Listado de ventas Vesper (5).xlsx')
df2=pd.read_excel('Listado de ventas Vesper (6).xlsx')
df3=pd.read_excel('Listado de ventas Vesper (7).xlsx')
df4=pd.read_excel('Listado de ventas Vesper (8).xlsx')
df5=pd.read_excel('Listado de ventas Vesper (9).xlsx')
df6=pd.read_excel('Listado de ventas Vesper (10).xlsx')
df7=pd.read_excel('Listado de ventas Vesper (11).xlsx')

lista_dfs=[df1,df2,df3,df4,df5,df6,df7]

resultado = pd.concat(lista_dfs, ignore_index=True)

resultado.drop(columns=['DNI / CUIT / CUIL','Nombre para el envío', 'Teléfono del comprador', 'Email del comprador', 'Teléfono para el envío', 'Calle', 'Metódo de pago', 'Nombre del comprador','Notas personalizadas','Notas del pedido','Altura','Departamento','Descripción del sitio','Peso en KG','Alto en CM','Ancho en CM','Profundidad en CM'], inplace=True)

resultado.to_csv('Data2.csv', index=False)

archivo_entrada = 'Data2.csv'
archivo_salida = 'ventas_limpio_completo.csv'

columnas_del_pedido = [
    'Fecha', 'Hora', 'Estado de la venta', 'Subtotal de productos',
    'Descuento', 'Costo de envío', 'Total', 'Metódo de envío',
    'Código postal', 'Provincia o estado', 'Ciudad', 'Cupón de decuento',
]


categorias_por_keyword = {
    'bucanera': 'Bucaneras', 'baby tee': 'Baby Tee', 'remera': 'Remera',
    'guante': 'Guantes', 'tote': 'Tote Bag', 'buzo': 'Buzo/Hoodie',
    'hoodie': 'Buzo/Hoodie', 'campera': 'Campera', 'short': 'Short',
    'vestido': 'Vestido', 'falda': 'Pollera', 'pollera': 'Pollera',
    'panty': 'Medias/Pantys', 'medias': 'Medias/Pantys', 'gorro': 'Gorro',
    'pantalon': 'Pantalón', 'pantalón': 'Pantalón',
}


def completar_datos_del_pedido(df):
    df = df.sort_values('# de venta').reset_index(drop=True)
    columnas_presentes = [c for c in columnas_del_pedido if c in df.columns]
    for columna in columnas_presentes:
        df[columna] = df.groupby('# de venta')[columna].transform(lambda s: s.ffill().bfill())
    return df


def agregar_fecha_y_mes(df):
    df['Fecha'] = pd.to_datetime(df['Fecha'], format='%d/%m/%Y', errors='coerce')
    df['Mes'] = df['Fecha'].dt.to_period('M').astype(str)
    return df


def categorizar(nombre_producto):
    nombre = str(nombre_producto).lower()
    for palabra_clave, categoria in categorias_por_keyword.items():
        if palabra_clave in nombre:
            return categoria
    return 'Otro'


def extraer_talle(nombre_producto):
    match = re.search(r'\((XS|S|M|L|XL|XXL)\)', str(nombre_producto), re.IGNORECASE)
    return match.group(1).upper() if match else None


def limpiar_nombre(nombre_producto):
    nombre = str(nombre_producto)
    nombre = re.sub(r'\([^)]*\)', '', nombre)
    nombre = re.sub(r'preventa', '', nombre, flags=re.IGNORECASE)
    nombre = re.sub(r'[^\w\sÁÉÍÓÚÜÑáéíóúüñ]', ' ', nombre)
    nombre = re.sub(r'\s+', ' ', nombre).strip()
    return nombre


def identificar_diseno(df):

    nombres_limpios = df['Nombre del producto'].apply(limpiar_nombre)

    etiqueta_mas_comun_por_sku = (
        df.assign(nombre_limpio=nombres_limpios)
          .dropna(subset=['SKU'])
          .groupby('SKU')['nombre_limpio']
          .agg(lambda nombres: Counter(nombres).most_common(1)[0][0])
    )

    return df['SKU'].map(etiqueta_mas_comun_por_sku).fillna(nombres_limpios)


def limpiar(path_csv):
    df = pd.read_csv(path_csv)
    df = completar_datos_del_pedido(df)
    df = agregar_fecha_y_mes(df)

    df['Categoria'] = df['Nombre del producto'].apply(categorizar)
    df['Talle'] = df['Nombre del producto'].apply(extraer_talle)
    df['Total_linea'] = df['Precio del producto'] * df['Cantidad del producto']
    df['Diseño'] = identificar_diseno(df)
    df['Total_linea'] = (
    df['Total_linea'] * (df['Subtotal de productos'] + df['Descuento']) / df['Subtotal de productos']
)

    return df


if __name__ == '__main__':
    df_limpio = limpiar(archivo_entrada)
    df_limpio.to_csv(archivo_salida, index=False)
    df_confirmadas = df_limpio[df_limpio['Estado de la venta'] == 'Pago Confirmado']
    df_confirmadas.to_csv('ventas_limpio_confirmadas.csv', index=False)
