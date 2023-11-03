from os import PathLike
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from joblib import dump
import pandas as pd
import pathlib

# Cargar el conjunto de datos
train_df = pd.read_csv(pathlib.Path('data/train.csv'))

train_df = train_df.drop(columns=['Id'])

# Extrae la columna 'Bikes_Rented' y guárdala en y_train
y_train = train_df.pop('Bikes_Rented')

# Elimina la columna 'Bikes_Rented' del DataFrame train_df y guárdala en X_train
X_train = train_df

print('Training model..')
clf = RandomForestClassifier(n_estimators=10, max_depth=2, random_state=0)
clf.fit(X_train, y_train)

print('Saving model..')
dump(clf, pathlib.Path('model/train.joblib'))
