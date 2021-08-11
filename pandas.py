#1 - noy
import pandas as pd
read_file = pd.read_excel (r"C:\Users\Noy Vilkin\Documents\python\Automobile_data.xlsx", sheet_name='in')
read_file.to_csv (r"C:\Users\Noy Vilkin\Documents\python\Automobile_data.csv", index = None, header=True)
df = pd.read_csv(r"C:\Users\Noy Vilkin\Documents\python\Automobile_data.csv")
print(df.head(5))
print(df.tail(5))

#3 - noy
high_val = df.sort_values(by="price", ascending=False)
high_val = high_val[["company", "price"]]
print("Highest price:\n", high_val.head(1))

#6 - ofir
import pandas as pd
df = pd.read_csv('Automobile_data.csv')
df2 = df.groupby('company').max('price')
df2['company'] = df2.index
print(df2[['company', 'price']])

#8 - ofir
import pandas as pd
df = pd.read_csv('Automobile_data.csv')
print(df.sort_values(by='price', ascending=False))
