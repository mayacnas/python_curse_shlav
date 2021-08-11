#1 
import pandas as pd
read_file = pd.read_excel (r"C:\Users\Noy Vilkin\Documents\python\Automobile_data.xlsx", sheet_name='in')
read_file.to_csv (r"C:\Users\Noy Vilkin\Documents\python\Automobile_data.csv", index = None, header=True)
df = pd.read_csv(r"C:\Users\Noy Vilkin\Documents\python\Automobile_data.csv")
print(df.head(5))
print(df.tail(5))
