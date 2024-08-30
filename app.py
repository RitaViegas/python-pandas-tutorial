#print("Hello World")
import pandas as pd
data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
#print(data_frame)

# 04 - SERIES 
data = pd.Series([23,45,7,34,6,63,36,78,54,34])
#print(data)

# 04.1 - DATE RANGE
serie_de_datas = pd.date_range(start="2021-05-01", end="2021-05-12")
#print(serie_de_datas)

# 04.2 - SERIES APPLY

my_series = pd.Series([2, 4, 6, 8, 10])
resultado = my_series.apply(lambda x: x/2)
#print(resultado)

# 05 - DATA_FRAMES 

data_1 = [["Toyota", "Corolla", "Blue"], ["Ford", "K", "Yellow"], ["Porsche", "Cayenne", "White"]]
df = pd.DataFrame(data_1, columns=['Brand', 'Model', 'Color'])
#print(df)

# 05.1 - DATA_FRAME DICT

data_2 = [
    { 
        "brand": "Toyota", 
        "model": "Corolla",
        "color": "Blue"
    },
    {
        "brand": "Ford", 
        "model": "K",
        "color": "Yellow"
    },
    {
        "brand": "Porsche", 
        "model": "Cayenne",
        "color": "White"
    },
    {
        "brand": "Tesla",
        "model": "Model S",
        "color": "Red"
    }
]
df_2 = pd.DataFrame(data_2, columns=['brand', 'model', 'color'])
#print(df_2)

# 05.2  - DATA_FRAME iLoc

data_frame_1 = pd.read_csv('.learn/assets/pokemon_data.csv')
valor = data_frame_1.iloc[133,6]
#print(valor)

# 05.3 - DATA_FRAME HEAD

resultado_05_3 = data_frame_1.head(3)
#print(resultado_05_3)

# 05.4 - DATA_FRAME TAIL

resultado_05_4 = data_frame_1.tail(3)
#print(resultado_05_4)

# 05.5 - PRINT COLUMNS

#print(data_frame_1[['Name', 'Type 1']][0:10])

# 05.6 - LOC FUNCTION

resultado_05_6 = data_frame_1.loc[data_frame_1['Attack'] > 80]
#print(resultado_05_6)

# 05.7 - FILTER AND COUNT
legendary_pokemons = data_frame_1.loc[data_frame_1['Legendary'] == True]
total_pokemons = len(legendary_pokemons)
#print(total_pokemons)

# 06 - CLEAN DATASETS

data_frame_06 = pd.read_csv('.learn/assets/us_baby_names_right.csv')
resultado_06 = data_frame_06.head(5)
#print(resultado_06)

#06.1 - REMOVE COLUMN

data_frame_new = data_frame_06.iloc[: , 1:]
data_frame_new_5_rows = data_frame_new.head(5)
#print(data_frame_new_5_rows)

# 06.2 - VALUE COUNTS

gender_counts = data_frame_06['Gender'].value_counts()
#print(gender_counts)

# 06.3 - GROUP BY
grouped_names = data_frame_06.groupby('Name').sum()
#print(grouped_names)
number_of_unique_names = len(grouped_names)
#print(number_of_unique_names)