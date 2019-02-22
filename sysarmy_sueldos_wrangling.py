#!/usr/bin/env python
# coding: utf-8

# # Encuestas de sueldos de sysarmy
# ## Limpieza y transformación de los resultados de las encuestas
# 
# Se utilizaron resultados de **encuestas de sueldos realizadas por la comunidad [sysarmy](http://sysarmy.com/)**. Esta comunidad se autodefine de la siguiente manera: *“Es la Comunidad Argentina de Sistemas, con el objetivo de nuclear a profesionales del sector para favorecer el contacto y el intercambio de conocimiento”*.
# Las encuestas contienen información relativa a los **salarios de trabajadores en IT en Argentina y otros países de América**. Hay disponible resultados de siete encuestas realizadas cada seis meses, desde el segundo semestre de 2015 hasta el segundo semestre de 2018
# 
# ### Objetivo
# La intención del proyecto es limpiar y transformar los datasets de todas las encuestas, y agrupar los resultados en un único archivo. Se realizaron diversas transformaciones de los datos, entre las que se destacan:
# *  Unificación y renombre de las columnas
# *  Conversión de los sueldos a su valor neto para simplificar las comparaciones. Se asumió la siguiente equivalencia: neto = bruto * 0.83
# *  Conversión de los sueldos a dólares estadounidenses, utilizando esta moneda como medida de referencia para poder hacer comparaciones entre los países y evitar las distorsiones inflacionarias de las monedas. Se descargaron de [Bloomberg](https://www.bloomberg.com/markets) archivos *.json* con las cotizaciones semanales de las diferentes monedas con respecto al dólar estadounidense.
# *  Eliminación de filas con outliers en el sueldo. Algunos registros tenían valores distorsionados. Se utilizó la métrica IQR para determinar los outliers.
# *  Mapeo de carreras a una variable categórica con los siguientes posibles valores: *Ingenieria, Licenciatura, Tecnicatura, Analista u Otros*.
# 
# ### Datos de entrada
# *  Resultados de encuestas
# 
# | Período | Formato |   Países  |            Ruta           |          Link         |
# |:-------:|:-------:|:---------:|:-------------------------:|:---------------------:|
# |  2015-2 |   .csv  | Argentina |  */data/input/2015_2.csv* | https://goo.gl/xx11f7 |
# |  2016-1 |   .csv  | Argentina |  */data/input/2016_1.csv* | https://goo.gl/Jd2NzQ |
# |  2016-2 |  .xlsx  |   Varios  | */data/input/2016_2.xlsx* | https://goo.gl/RqzrJd |
# |  2017-1 |  .xlsx  |   Varios  | */data/input/2017_1.xlsx* | https://goo.gl/SyDpKo |
# |  2017-2 |  .xlsx  |   Varios  | */data/input/2017_2.xlsx* | https://goo.gl/g3C1bj |
# |  2018-1 |  .xlsx  |   Varios  | */data/input/2018_1.xlsx* | https://goo.gl/bFDCnA |
# |  2018-2 |  .xlsx  |   Varios  | */data/input/2018_2.xslx* | https://goo.gl/Lf2d8Z |
# |  2019-1 |  .xlsx  |   Varios  | */data/input/2019_1.xslx* | https://goo.gl/CX8tTd |
# 
# *  Cotización de monedas
#   *  Descripción: archivos *.json* con las cotizaciones semanales con respecto al dólar estadounidense (USD) de las diferentes monedas utilizadas en las encuestas.
#   
# | Moneda |    País   |              Ruta             |                                            Link                                            |
# |:------:|:---------:|:-----------------------------:|:------------------------------------------------------------------------------------------:|
# |   ARS  | Argentina | */data/input/USDARS_CUR.json* | https://www.bloomberg.com/markets/api/bulk-time-series/price/USDARS%3ACUR?timeFrame=5_YEAR |
# |   BOB  |  Bolivia  | */data/input/USDBOB_CUR.json* | https://www.bloomberg.com/markets/api/bulk-time-series/price/USDBOB%3ACUR?timeFrame=5_YEAR |
# |   CLP  |   Chile   | */data/input/USDCLP_CUR.json* | https://www.bloomberg.com/markets/api/bulk-time-series/price/USDCLP%3ACUR?timeFrame=5_YEAR |
# |   COP  | Colombia  | */data/input/USDCOP_CUR.json* | https://www.bloomberg.com/markets/api/bulk-time-series/price/USDCOP%3ACUR?timeFrame=5_YEAR |
# |   CRC  | Costa Rica| */data/input/USDCRC_CUR.json* | https://www.bloomberg.com/markets/api/bulk-time-series/price/USDCRC%3ACUR?timeFrame=5_YEAR |
# |   CUP  |   Cuba    | */data/input/USDCUP_CUR.json* | https://www.bloomberg.com/markets/api/bulk-time-series/price/USDCUP%3ACUR?timeFrame=5_YEAR |
# |   DOP  |Dominicana | */data/input/USDDOP_CUR.json* | https://www.bloomberg.com/markets/api/bulk-time-series/price/USDDOP%3ACUR?timeFrame=5_YEAR |
# |   GTQ  |Guatemala  | */data/input/USDGTQ_CUR.json* | https://www.bloomberg.com/markets/api/bulk-time-series/price/USDGTQ%3ACUR?timeFrame=5_YEAR |
# |   HNL  |  Honduras | */data/input/USDHNL_CUR.json* | https://www.bloomberg.com/markets/api/bulk-time-series/price/USDHNL%3ACUR?timeFrame=5_YEAR |
# |   MXN  |  México   | */data/input/USDMXN_CUR.json* | https://www.bloomberg.com/markets/api/bulk-time-series/price/USDMXN%3ACUR?timeFrame=5_YEAR |
# |   NIO  | Nicaragua | */data/input/USDNIO_CUR.json* | https://www.bloomberg.com/markets/api/bulk-time-series/price/USDNIO%3ACUR?timeFrame=5_YEAR |
# |   PAB  |  Panamá   | */data/input/USDPAB_CUR.json* | https://www.bloomberg.com/markets/api/bulk-time-series/price/USDPAB%3ACUR?timeFrame=5_YEAR |
# |   PEN  |   Perú    | */data/input/USDPEN_CUR.json* | https://www.bloomberg.com/markets/api/bulk-time-series/price/USDPEN%3ACUR?timeFrame=5_YEAR |
# |   PYG  | Paraguay  | */data/input/USDPYG_CUR.json* | https://www.bloomberg.com/markets/api/bulk-time-series/price/USDPYG%3ACUR?timeFrame=5_YEAR |
# |   UYU  | Uruguay   | */data/input/USDUYU_CUR.json* | https://www.bloomberg.com/markets/api/bulk-time-series/price/USDUYU%3ACUR?timeFrame=5_YEAR |
# |   VEF  |  Venezuela| */data/input/USDVEF_CUR.json* | https://www.bloomberg.com/markets/api/bulk-time-series/price/USDVEF%3ACUR?timeFrame=5_YEAR |
#   
# 
# ### Datos de salida
# *  */data/output/encuestas.csv*: archivo *.csv* de salida, con los resultados normalizados de todas las encuestas.
# 

# ## Data Wrangling

# In[1]:


# Imports
import os
import pandas as pd
import yaml
from unidecode import unidecode
from numpy import percentile
import json
import datetime
import re


# ### Archivo de configuración
# En *config* guarda los datos del archivo *sysarmy_sueldos_wrangling.yml* que tiene información de configuración del proyecto (parámetros para leer y escribir los archivos, configuración general).

# In[2]:


config = yaml.safe_load(open("sysarmy_sueldos_wrangling.yml", encoding="utf-8"))


# ### Transformaciones
# A continuación están los métodos que se aplican a los datos para transformalos.

# In[12]:


def junta_tecnologias(df):
    """ Junta columnas con tecnologías """
    tech_columns = [c for c in df.columns.tolist() if "tecnologias" in c]
    df["tecnologias"] = df[tech_columns].fillna(value="").astype(str).apply(lambda x: ','.join(x.tolist()), axis=1)
    df["tecnologias"] = df["tecnologias"].apply(lambda x: re.sub(",+", ",", x))
    df["tecnologias"] = df["tecnologias"].apply(lambda x: re.sub("^,|,$", "", x))
    df.drop(columns=tech_columns, inplace=True)

    
def valores_inconsistentes(row):
    """ Soluciona inconsistencia en los datos """
    if row["experiencia"] == "10+" or row["antiguedad_puesto"] == "10+":
        return row["experiencia"]

    if int(row["experiencia"]) >= int(row["antiguedad_puesto"]):
        return row["experiencia"]
    else:
        return row["antiguedad_puesto"]


def transforma_edad(x):
    """ Convierte 'Menos de 18 años' a '0 - 17'"""
    if x == "Menos de 18 años":
        return "0 - 17"
    elif int(x) > 100:
        return 50
    else:
        return int(x)


def transforma_experiencia(x):
    """ Convierte 'x' a un int """
    if x == "Menos de un año":
        return 0
    elif x == "1 - 2":
        return 1
    elif x == "3 - 5":
        return 4
    elif x == "5 - 7":
        return 6
    elif x == "8 - 10":
        return 9
    elif int(x) > 50:
        return 10
    else:
        return int(x)


def transforma_antiguedad(x):
    """ Convierte 'x' a un int """
    if x == "Menos de un año":
        return 0
    elif x == "1 - 2":
        return 1
    elif x == "2 - 3":
        return 2
    elif x == "3 - 4":
        return 3
    elif x == "4 - 5":
        return 4
    elif x == "5 - 6":
        return 5
    elif x == "6 - 7":
        return 6
    elif x == "7 - 8":
        return 7
    elif x == "8 - 9":
        return 8
    elif x == "9 - 10":
        return 9
    elif int(x) > 50:
        return 10
    else:
        return int(x)


def transforma_gente_a_cargo(x):
    """ Convierte 'x' a un int """
    if x == "No":
        return 0
    elif x == "Sí":
        return 1
    elif x == "1 - 2":
        return 1
    elif x == "2 - 3":
        return 2
    elif x == "3 - 4":
        return 3
    elif x == "4 - 5":
        return 4
    elif x == "5 - 6":
        return 5
    elif x == "6 - 7":
        return 6
    elif x == "7 - 8":
        return 7
    elif x == "8 - 9":
        return 8
    elif x == "9 - 10":
        return 9
    else:
        return x


def transforma_cantidad_empleados(x):
    """ Convierte a None si 'x' no está en 'validos' """
    validos = ["1-10", "11-50", "51-100", "101-200", "201-500", "501-1000", "1001-2000", "2001-5000",
              "5001-10000", "10001+"]
    if x in validos:
        return x
    else:
        return None


def transforma_sueldo(row):
    """ Convierte sueldo bruto a sueldo neto. Asume: neto = bruto * 0.83"""
    if "tipo_sueldo_mensual" not in row:    # Por defecto es 'bruto'
        return round(row["sueldo_mensual"] * 0.83, 2)

    if row["tipo_sueldo_mensual"] == "Bruto":
        return round(float(row["sueldo_mensual"]) * 0.83, 2)
    else:
        return round(float(row["sueldo_mensual"]), 2)


def transforma_sueldo_a_usd(row, currencies, input_path):
    """ Convierte a USD """
    try:
        curr_sym = currencies[row["pais"]]

        if curr_sym == "USD":
            return round(row["sueldo_mensual_neto"], 2)
        file = "USD{0}_CUR.json".format(curr_sym)
        with open(input_path + file) as data_file:
            data = json.load(data_file)
            currency_df = pd.DataFrame(data[0]['price'])
            currency_df.date = pd.to_datetime(currency_df.date)
            
            print(currency_df.head())
            print("periodo antes de regex: {}".format(row["periodo"]))
            year = int(re.search("([0-9]+)", row["periodo"]).group(1))
            month = 1 if re.search("_([0-9]+)", row["periodo"]).group(1) == "1" else 6
            print("mes: {0}".format(month))
            period_as_datetime = pd.Timestamp(year=year, month=month, day=1)
            
            print("as datetime: {}".format(period_as_datetime))

            rate = currency_df.loc[currency_df["date"] > period_as_datetime].sort_values(by="date").iloc[0]["value"]
        
            print(rate)
        return round(row["sueldo_mensual_neto"] / rate, 2)
    except (KeyError, IndexError):
        return 0


def transforma_cursos_especializacion(x):
    """ Convierte a binario (0,1) """
    if re.search("No", x) is not None:
        return 0
    else:
        return 1


def transforma_carrera(row):
    """ Mapea 'carrera' con valores predefinidos """
    if "carrera" not in row:
        return None

    carrera = unidecode(str(row["carrera"]))
    if carrera is None or carrera == "" or carrera == " ":
        return None
    elif re.search(r"(\s|^)ing(\s|\W|enieria|eniero).+(sis|info|comp|tic|prog)", carrera, re.IGNORECASE | re.UNICODE)     is not None:
        return "Ingenieria"
    elif re.search(r"(\s|^)lic(\s|\W|enciatura|enciado).+(sis|info|comp|tic|prog)", carrera, re.IGNORECASE | re.UNICODE)     is not None:
        return "Licenciatura"
    elif re.search(r"(\s|^)tec(\s|\W|nico|nicatura).+(sis|info|comp|tic|prog)", carrera, re.IGNORECASE | re.UNICODE)     is not None:
        return "Tecnicatura"
    elif re.search(r"(\s|^)(analista|analisis).+(sis|info|comp|tic|prog)", carrera, re.IGNORECASE | re.UNICODE) is not None:
        return "Analista"
    else:
        return "Otro"


def transforma_ajuste_inflacion(x):
    """ Convierte a int """
    if x == "No":
        return 0
    elif x == "Uno":
        return 1
    elif x == "Dos":
        return 2
    elif x == "Más de dos":
        return 3
    else:
        return 0


def transforma_cambio_empresa_6_meses(x):
    """ Convierte a binario (0,1) """
    if x == "No":
        return 0
    else:
        return 1


def transforma_motivo_cambio_empresa(row):
    """ Mapea valores """
    if row["cambio_empresa_6_meses"] == 0:
        return "No cambio"
    else:
        return row["motivo_cambio_empresa"]

    
def transforma_periodo_a_fecha(x):
    """ Convierte 'x' a formato de fecha (str) """
    if x == "2015_2":
        return "01/07/2015"
    elif x == "2016_1":
        return "01/01/2016"
    elif x == "2016_2":
        return "01/07/2016"
    elif x == "2017_1":
        return "01/01/2017"
    elif x == "2017_2":
        return "01/07/2017"
    elif x == "2018_1":
        return "01/01/2018"
    elif x == "2018_2":
        return "01/07/2018"
    elif x == "2019_1":
        return "01/01/2019"
    else:
        return None


# In[13]:


def transformaciones(df, country, period, rename_values, currencies, sorted_columns, input_folder):
    """ Aplica las transformaciones sobre el DataFrame 'df' """
    df.loc[:, "pais"] = country  # Agrega una nueva columna con el nombre del pais

    df.rename(rename_values, axis=1, inplace=True) # Renombra las columnas

    print("periodo: {}".format(period))
    # Transformaciones
    junta_tecnologias(df)
    df["periodo"] = period
    df["periodo_fecha"] = df["periodo"].apply(transforma_periodo_a_fecha)
    df["pais"] = df["pais"].replace({"Mexico": "México", "Peru": "Perú", "Republica Dominicana": "República Dominicana"})
    df["edad"] = df["edad"].apply(transforma_edad)
    df["carrera"] = df.apply(transforma_carrera, axis=1)
    df["experiencia"] = df["experiencia"].apply(transforma_experiencia)
    df["antiguedad_puesto"] = df["antiguedad_puesto"].apply(transforma_antiguedad)

    if "cantidad_empleados" in df.columns.tolist():
        df["cantidad_empleados"] = df["cantidad_empleados"].apply(transforma_cantidad_empleados)
    else:
        df["cantidad_empleados"] = None

    df["experiencia"] = df.apply(valores_inconsistentes, axis=1)


    if "gente_a_cargo" in df.columns.tolist():
        df["gente_a_cargo"] = df["gente_a_cargo"].apply(transforma_gente_a_cargo)
    else:
        df["gente_a_cargo"] = None

    df["sueldo_mensual_neto"] = df.apply(transforma_sueldo, axis=1)
    df["sueldo_mensual_neto_usd"] = df.apply(lambda r: transforma_sueldo_a_usd(r, currencies, input_folder), axis=1)

    if "cursos_especializacion" in df.columns.tolist():
        df["cursos_especializacion"] = df["cursos_especializacion"].apply(transforma_cursos_especializacion)
    else:
        df["cursos_especializacion"] = None

    df["ajuste_inflacion"] = df["ajuste_inflacion"].apply(transforma_ajuste_inflacion)
    
    if "cambio_empresa_6_meses" in df.columns.tolist():
        df["cambio_empresa_6_meses"] = df["cambio_empresa_6_meses"].apply(transforma_cambio_empresa_6_meses)
    else:
        df["cambio_empresa_6_meses"] = None
        
    if "movivo_cambio_empresa" in df.columns.tolist():
        df["motivo_cambio_empresa"] = df.apply(transforma_motivo_cambio_empresa, axis=1)
    else:
        df["motivo_cambio_empresa"] = None

    return df.reindex(columns=sorted_columns)


# ### Aplica transformaciones
# Lee los archivos *.csv* y *.xlsx* en DataFrames y les aplica las transformaciones correspondientes. Junta todos los datos en un nuevo DataFrame (*full_df*)

# In[14]:


def get_df_csv(input_path):
    """ Devuelve un DataFrame con los datos procesados del .csv en 'path' """
    df = pd.read_csv(input_path, **config["input"]["csv"])
    df.rename({"Trabajo en": "provincia"}, axis=1, inplace=True)
    return transformaciones(df, "Argentina", period, config["rename"], config["currencies"], config["sorted_columns"], 
                            config["input"]["folder"])


def get_df_xlsx(input_path):
    """ Devuelve un DataFrame con los datos procesados del .xlsx en 'path' """
    dfs = pd.read_excel(input_path, **config["input"]["excel"])  # OrderedDict, each key is a DataFrame

    new_df = pd.DataFrame()
    # Itera sobre todos los DataFrames en 'dfs' y los concatena en 'new_df'
    for key, df in dfs.items():
        if key != "Todas las respuestas":
            df.rename({key: "provincia"}, axis=1, inplace=True)
            new_df_transformed = transformaciones(df, key, period, config["rename"], config["currencies"], 
                                                   config["sorted_columns"], config["input"]["folder"])
            new_df = new_df.append(new_df_transformed, ignore_index=True)

    return new_df


full_df = pd.DataFrame() # DataFrame que junta todas las encuestas

for file in os.listdir(config["input"]["folder"]):
    input_path = config["input"]["folder"] + file
    period = re.search(".+ ?(?=\.)", file).group(0)

    if ".xlsx" in file:
        new_df = get_df_xlsx(input_path)
    elif ".csv" in file:
        new_df = get_df_csv(input_path)
    else:
        continue

    full_df = full_df.append(new_df, ignore_index=True)
    
print(full_df.shape)


# ### Valores fuera de rango

# In[6]:


def borra_outliers(df):
    """ Borra filas con valores fuera de rango en 'sueldo_mensual_neto_usd' """

    # Outliers por IQR
    q25 = percentile(df.loc[:, "sueldo_mensual_neto_usd"].tolist(), 25)
    q75 = percentile(df.loc[:, "sueldo_mensual_neto_usd"].tolist(), 75)
    iqr = q75 - q25
    cut_off = iqr * 1.5
    lower, upper = q25 - cut_off, q75 + cut_off
    df = df.query("sueldo_mensual_neto_usd > @lower & sueldo_mensual_neto_usd < @upper")

    # Outliers por valores predefinidos
    df = df.query("sueldo_mensual_neto_usd > 1")
    df = df.query("sueldo_mensual_neto_usd > 5 | pais == 'Venezuela'")

    return df

full_df = borra_outliers(full_df)


# ### Archivo de salida
# Guarda el archivos de salida en formato CSV de acuerdo a los parámetros fijados en el archivo de configuración

# In[7]:


full_df.to_csv(**config["output"])


# In[ ]:




