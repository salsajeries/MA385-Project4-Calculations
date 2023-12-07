import pandas as pd
import math

print()
def euclidean_distance(calories, protein, fat, sodium, fiber, carbs, sugars, potassium, vitamins):

    distance = math.sqrt((calories - 100)**2 + (protein - 3)**2 + (fat - 0)**2 + (sodium - 0)**2 + (fiber - 3)**2 + (carbs - 14)**2 + (sugars - 7)**2 + (potassium - 100)**2 + (vitamins - 10.28116895)**2)
    return distance

df = pd.read_csv('CerealData.csv')                          # Read in cereal data as dataframe

for ind in df.index:
    value = euclidean_distance(df['calories'][ind], df['protein'][ind], df['fat'][ind], df['sodium'][ind], df['fiber'][ind], df['carbs'][ind], df['sugars'][ind], df['potassium'][ind], df['vitamins'][ind])
    print(df['name'][ind], ': ', value)

print()



correlation_matrix = df.iloc[:, 1:11].corr()                # Create correlation matrix
popularity_correlation = correlation_matrix['rating']       # Determine popularity correlation based on rating

print()
print(popularity_correlation)                               # Print results
print()