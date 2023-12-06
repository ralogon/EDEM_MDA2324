""" Ejercicio 1
Lee el archivo CSV con Pandas de 'pokemon_data.csv' alojado en la carpeta de datos de este repositorio y realizar las siguientes operaciones
"""
import pandas as pd
import numpy as np

pokemon = pd.read_csv("C:\\Users\\josan\\Documents\\GitHub\\EDEM_MDA2324\\Alumnos\\ES\\Josan_Rodrigo_Cortes\\CursodePython\\Sesion5\\ejercicio1\\pokemon_data.csv",sep=',')
pokemondf=pd.DataFrame(pokemon)

#print(pokemondf.info()) información sobre el dataframe
#print(pokemondf.describe())
# # print(pokemondf.Attack.describe()) describe solamente la columna Attack
# print(pokemondf.describe(include=np.number)) describe las columnas de tipo numerico
# # print(pokemondf.describe(include=object)) describe las de tipo no numérico
# print(pokemondf.head()) 5 primeros registros
# print(pokemondf.tail()) 5 ultimos registros
# print(pokemondf.shape) Nos devuelve el total de filas y columnas
# pokemondf.Name=pokemondf['Speed'] No lo ejecuto pero cambiaría los valores de una columna por los de otra, conserva la original
#pokemondf.drop(['NombredelaColumnaaelimninar'],axis=1,inplace=True) eliminariá una columna del data frame
# # media print(pokemondf.mean)
# Renombrar una columna:
# pokemondf.rename(columns={'nombreactual':'nuevonombre'},inplace=True)
# Con la funcion map, podemos transformar los valores de una columna en otra columna
# print(pokemondf['Name'])
# Obtener la media metodo .mean()
# print(pokemondf.mean()) No me funciona
# print(pokemondf['Speed'].mean()) así si
# values_counts
# print(pokemondf["Type 2"].value_counts())


# IMPRIMIR TODOS LOS VALORES
# print(pokemondf)
# IMPRIMIR LOS PRIMEROS 5
# print(pokemondf.head())
# IMPRIMIR LOS ÚLTIMOS 5
# print(pokemondf.tail())
# OBTENER NOMBRES DE LAS COLUMNAS nos devuelve el nombre de las columnas
# print(pokemondf.columns) 
# OBTENER TODOS LOS NOMBRES, obtenemos todos los valores de la columna 'Name'
# print(pokemondf['Name'])
# print(pokemondf.Name)
#print(list(pokemondf.Name))
# OBTENER TODOS LOS NOMBRES Y VELOCIDADES, tres formas, la ultima en formato lista
# print(pokemondf.columns)
# print(pokemondf[['Name','Speed']])

# LOS PRIMEROS 5 NOMBRES USANDO [::]
# listaPokemons=list(pokemondf.Name)
# print(listaPokemons[0:5])

# OBTENER TODAS LAS FILAS
# print(pokemondf[:])
# OBTENER UN RANGO DE FILAS
# print(pokemondf[20:290])
# OBTENER EL NOMBRE DE LA FILA 10
# print(pokemondf.loc[10,'Name'])
# ITERAR POR TODOS Y MOSTRAR EL ÍNDICE Y NOMBRE DE CADA FILA
# No se como hacerlo
# POKEMONS DE TIPO 1 == WATER
#No funciona,nuevopokemondf=pokemondf[pokemondf['Type'].str.contains('Water', case=False, na=False)]
# print(nuevopokemondf)
# ESTADÍSTICAS (usando Describe del DafaFrame)
# print(pokemondf.describe())
# ORDENACIÓN POR NOMBRE ASCENDENTE
# pokemondfOrdenado= pokemondf.sort_values(by='Name',)
# print(pokemondfOrdenado)
# CREAR UNA COLUMNA EXTRA CALCULADA
# La columna debe ser la suma de HP + ATAQUE + DEFENSA + VELOCIDAD
# La columna debe llamarse TOTAL
# pokemondf['Total']=pokemondf['HP']+pokemondf['Attack']+ pokemondf['Defense']+pokemondf['Sp. Atk']+pokemondf['Sp. Def']+pokemondf['Speed']
# print(pokemondf)
# # ELIMINAR LA COLUMNA TOTAL
# pokemondf=pokemondf.drop(columns='Total')
# print(pokemondf)

# FILTRAR POKEMONS DE TIPOS "GRASS" Y "POISON"

# FILTRAR POKEMONS DE TIPO "FIRE" Ó "POISON
# print(pokemondf.head)
# pokemondfFiltrado = pokemondf[(pokemondf['Type 1'] == "Fire") | (pokemondf['Type 1'] == "Poison")]
# print(pokemondfFiltrado)
# FILTRAR POKEMONS DE TIPO "GRASS" Y "POISON" Y UN HP >= 70
# print(pokemondf.head)
# pokemondfFiltrado = pokemondf[(pokemondf['Type 1'] == "Fire") | (pokemondf['Type 1'] == "Poison") | (pokemondf['HP'] >= 70)]
# print(pokemondfFiltrado)

pokemondfFiltrado = pokemondf[(pokemondf['Type 1'] == "Poison")]
print(pokemondfFiltrado)
# FILTRAR POKEMONS CON NOMBRE "MEGA"
# FILTRAR POKEMONS SIN NOMBRE "MEGA"
# FILTRAR POKEMONS CUYOS NOMBRES COMIENCEN CON "PI"
# RENOMBRADO DE COLUMNA "FIRE" a "FLAME"
# RENOMBRAR DE NUEVO A "FIRE" LA COLUMNA "FLAME" RECIÉN CAMBIADA
# CAMBIAR A TODOS LOS POKEMON LEGENDARIOS A TIPO "FIRE"
# (Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR DEFENSA
# (Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR ATAQUE
# (Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR HP
# (Agrupación - groupBy) ESTADÍSTICAS DE SUMA POR TIPO DE POKEMON
# (Agrupación - groupBy) ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1DE POKEMON
# (Agrupación - groupBy) ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1 y 2 DE POKEMON
# Nota: SI TENEMOS ARCHIVOS ENORMES (1TB) PODEMOS LEERLOS POR PARTES Cada fila podría estar acumulando cerca de 20 bytes, por lo que podríamos estar trabajando con cantidades enormes

# LEE EL ARCHIVO CVS SEPARÁNDOLO POR CHUNKS Y CON UN TAMAÑO DE (chunksize=5)
# ITERA POR LOS CHUNKS Y MUÉSTRALOS POR CONSOLA 


