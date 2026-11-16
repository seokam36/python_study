import pandas as pd
url = 'https://raw.githubusercontent.com/rashida048/Datasets/master/USA_cars_datasets.csv'
df = pd.read_csv(url)

df = df[df['price'] > 0]
num_cols = ['year', 'mileage']
cat_cols = ['brand', 'model', 'title_status', 'color', 'state']
for col in cat_cols:
    df[col] = df[col].astype('category')

X = df[num_cols + cat_cols]
Y = df['price']
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)