#1 - noy
import pandas as pd
read_file = pd.read_excel ("Automobile_data.xlsx", sheet_name='in')
read_file.to_csv ("Automobile_data.csv", index = None, header=True)
df = pd.read_csv("Automobile_data.csv")
print(df.head(5))
print(df.tail(5))


#3 - noy
high_val = df.sort_values(by="price", ascending=False)
high_val = high_val[["company", "price"]]
print("Highest price:\n", high_val.head(1))

#5 - maya
read_file = pd.read_excel('C:/Users/User/Automobile_data.xlsx', sheet_name='in')
read_file.to_csv(r'C:/Users/User/Automobile_data.csv', index = None, header=True)
df = pd.read_csv(r'C:/Users/User/Automobile_data.csv')
count = df['company'].value_counts()
print(count)

#6 - ofir
import pandas as pd
df = pd.read_csv('Automobile_data.csv')
df2 = df.groupby('company').max('price')
df2['company'] = df2.index
print(df2[['company', 'price']])

#7 - amit
df = pd.read_csv('Automobile_data.csv')
print(df.groupby(['company'])['average-mileage'].agg(lambda x: x.unique().sum()/x.nunique()))

#8 - ofir
import pandas as pd
df = pd.read_csv('Automobile_data.csv')
print(df.sort_values(by='price', ascending=False))

#10 - ofir
import pandas as pd
Car_Price = {'Company': ['Toyota', 'Honda', 'BMW', 'Audi'],
             'Price': [23845, 17995, 135925, 71400]}
Car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMW', 'Audi'],
                  'Horsepower': [141, 80, 182, 160]}
df1 = pd.DataFrame(Car_Price)
df2 = pd.DataFrame(Car_Horsepower)
df3 = pd.merge(df1, df2, on='Company')
print(df3)
