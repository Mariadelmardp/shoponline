import pandas as pd
import numpy as np 
import os


def abrir_archivo(ruta):
    """
    Abre un archivo de texto, CSV, Excel o PDF de manera automática.

    Parámetros:
        ruta (str): Ruta del archivo a abrir.

    Retorna:
        Dependerá del tipo de archivo:
        - Texto: contenido del archivo
        - CSV/Excel: DataFrame de pandas
        - PDF/otros: abre el archivo con el programa predeterminado
    """
    if not os.path.exists(ruta):
        raise FileNotFoundError(f"El archivo '{ruta}' no existe.")

    extension = os.path.splitext(ruta)[1].lower()

    if extension in ['.txt', '.md']:
        with open(ruta, 'r', encoding='utf-8') as f:
            return f.read()

    elif extension == '.csv':
        return pd.read_csv(ruta)

    elif extension in ['.xls', '.xlsx']:
        return pd.read_excel(ruta)

    elif extension == '.pdf' or extension in ['.jpg', '.png', '.docx', '.pptx']:
        os.startfile(ruta)  # Solo funciona en Windows

    else:
        raise ValueError(f"Formato '{extension}' no soportado.")
'''
 🔍 Revisar los archivos cargados
for nombre, contenido in dataframes.items():
    print(f"\n📊 {nombre} - Tipo: {type(contenido)}")
    if isinstance(contenido, pd.DataFrame):
        print(contenido.head())  # Mostrar primeras filas si es un DataFrame
    else:
        print(contenido[:200])  # Mostrar primeros 200 caracteres si es texto'''


def abrir_archivos(lista_rutas):
    """
    Abre varios archivos y los almacena en un diccionario.
    
    Parámetros:
        lista_rutas (list): Lista con las rutas de los archivos.

    Retorna:
        dict: Diccionario con los nombres de los archivos como claves y sus contenidos como valores.
    """
    datos = {}

    for ruta in lista_rutas:
        if not os.path.exists(ruta):
            print(f"⚠️ Advertencia: El archivo '{ruta}' no existe. Se omitirá.")
            continue

        nombre_archivo = os.path.basename(ruta)
        extension = os.path.splitext(ruta)[1].lower()

        if extension in ['.csv']:
            datos[nombre_archivo] = pd.read_csv(ruta)
        elif extension in ['.xls', '.xlsx']:
            datos[nombre_archivo] = pd.read_excel(ruta)
        elif extension in ['.txt', '.md']:
            with open(ruta, 'r', encoding='utf-8') as f:
                datos[nombre_archivo] = f.read()
        else:
            print(f"⚠️ Formato '{extension}' no soportado para '{nombre_archivo}'. Se omitirá.")

    return datos
'''
# 📂 Ejemplo de uso
archivos = [
    "ventas.csv", 
    "clientes.xlsx", 
    "productos.csv", 
    "transacciones.txt"
]

dataframes = abrir_archivos(archivos)

# 🔍 Revisar los archivos cargados
for nombre, contenido in dataframes.items():
    print(f"\n📊 {nombre} - Tipo: {type(contenido)}")
    if isinstance(contenido, pd.DataFrame):
        print(contenido.head())  # Mostrar primeras filas si es un DataFrame
    else:
        print(contenido[:200])  # Mostrar primeros 200 caracteres si es texto
'''


def abrir_archivos_en_carpeta(ruta_carpeta):
    """
    Abre automáticamente todos los archivos de una carpeta y los almacena en un diccionario.

    Parámetros:
        ruta_carpeta (str): Ruta de la carpeta donde están los archivos.

    Retorna:
        dict: Diccionario con los nombres de los archivos como claves y sus contenidos como valores.
    """
    if not os.path.isdir(ruta_carpeta):
        raise NotADirectoryError(f"⚠️ La ruta '{ruta_carpeta}' no es una carpeta válida.")

    datos = {}
    archivos = os.listdir(ruta_carpeta)  # Listar archivos en la carpeta

    for archivo in archivos:
        ruta_archivo = os.path.join(ruta_carpeta, archivo)
        extension = os.path.splitext(archivo)[1].lower()

        # Solo leer archivos, ignorando carpetas
        if os.path.isfile(ruta_archivo):
            try:
                if extension in ['.csv']:
                    datos[archivo] = pd.read_csv(ruta_archivo)
                elif extension in ['.xls', '.xlsx']:
                    datos[archivo] = pd.read_excel(ruta_archivo)
                elif extension in ['.txt', '.md']:
                    with open(ruta_archivo, 'r', encoding='utf-8') as f:
                        datos[archivo] = f.read()
                else:
                    print(f"⚠️ Formato '{extension}' no soportado para '{archivo}'. Se omitirá.")
            except Exception as e:
                print(f"❌ Error al abrir '{archivo}': {e}")

    return datos
'''
# 📂 Ejemplo de uso
ruta_carpeta = "datos_clientes"  # Cambia esto por tu carpeta real
dataframes = abrir_archivos_en_carpeta(ruta_carpeta)

# 🔍 Revisar los archivos cargados
for nombre, contenido in dataframes.items():
    print(f"\n📊 {nombre} - Tipo: {type(contenido)}")
    if isinstance(contenido, pd.DataFrame):
        print(contenido.head())  # Mostrar primeras filas si es un DataFrame
    else:
        print(contenido[:200])  # Mostrar primeros 200 caracteres si es texto
'''

def convertir_columnas (df, formato_fecha='%y-%m-%d'):
  for col in df.columns:
    for dtype in [float, int]:
      try:
       df[col]=df[col].astype(dtype)
      except:
       pass
    try:
       df[col]=pd.to_datetime(df[col], format=formato_fecha)
    except: 
      pass 
  



def abrir_y_guardar_archivos(ruta_carpeta):
    """
    Abre todos los archivos CSV y Excel de una carpeta y los guarda como variables individuales.
    
    Parámetros:
        ruta_carpeta (str): Ruta de la carpeta donde están los archivos.
    """
    if not os.path.isdir(ruta_carpeta):
        raise NotADirectoryError(f"⚠️ La ruta '{ruta_carpeta}' no es una carpeta válida.")

    archivos = os.listdir(ruta_carpeta)

    for archivo in archivos:
        ruta_archivo = os.path.join(ruta_carpeta, archivo)
        nombre_variable = os.path.splitext(archivo)[0]  # Elimina la extensión del nombre del archivo
        extension = os.path.splitext(archivo)[1].lower()

        if os.path.isfile(ruta_archivo):
            if extension in ['.csv']:
                globals()[nombre_variable] = pd.read_csv(ruta_archivo)
            elif extension in ['.xls', '.xlsx']:
                globals()[nombre_variable] = pd.read_excel(ruta_archivo)

            print(f"✅ Archivo '{archivo}' cargado en la variable: {nombre_variable}")
    return nombre_variable

def modificar_dataframes():
    """
    Aplica modificaciones automáticas en todos los DataFrames creados.
    - Convierte columnas de fecha a formato datetime.
    - Convierte texto a minúsculas en columnas de tipo 'object'.
    """
    for nombre_variable in list(globals().keys()):  
        if isinstance(globals()[nombre_variable], pd.DataFrame):
            df = globals()[nombre_variable]

            # Convertir columnas de fecha automáticamente
            for col in df.select_dtypes(include=['object']):  
                try:
                    df[col] = pd.to_datetime(df[col])
                    print(f"📅 Columna '{col}' convertida a datetime en '{nombre_variable}'.")
                except:
                    pass  # Si no se puede convertir, sigue

            # Convertir texto a minúsculas en columnas de tipo 'object'
            for col in df.select_dtypes(include=['object']):
                df[col] = df[col].str.lower()
                print(f"🔤 Texto en '{col}' convertido a minúsculas en '{nombre_variable}'.")

            globals()[nombre_variable] = df  # Guardar cambios en la variable