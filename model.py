import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet
from sklearn import ensemble

df = pd.read_csv('file.csv')
df = df.dropna(subset=['LOCATION', 'PRICE', 'CITY', 'BEDS', 'BATHS', 'LOT SIZE', 'DAYS ON MARKET', 'SQUARE FEET'])
df['SALE TYPE'] = df[df['SALE TYPE'] == 'MLS Listing']
df['HOA/MONTH'] = df['HOA/MONTH'].fillna(0)
df['YEAR BUILT'] = df['YEAR BUILT'].fillna(1980)
df['CITY'] = df['CITY'].astype('category')
df['LOCATION'] = df['LOCATION'].astype('category')
df['PROPERTY TYPE'] = df['PROPERTY TYPE'].astype('category')
df['AGE'] = 2019 - df['YEAR BUILT']
df = df.drop(columns=['SALE TYPE', 'ADDRESS', 'ZIP OR POSTAL CODE', 'STATE OR PROVINCE', 'STATUS', 'URL (SEE http://www.redfin.com/buy-a-home/comparative-market-analysis FOR INFO ON PRICING)', 'SOURCE', 'MLS#', 'NEXT OPEN HOUSE START TIME', "NEXT OPEN HOUSE END TIME", 'SOLD DATE', 'INTERESTED', 'FAVORITE', '$/SQUARE FEET'])
df = pd.get_dummies(df, columns=['CITY'])
df = pd.get_dummies(df, columns=['LOCATION'])
df = pd.get_dummies(df, columns=['PROPERTY TYPE'])
X = df
y = df['PRICE']
X = X.drop(columns=["PRICE"])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=7) 
X_train, X_valid, y_train, y_valid = train_test_split(X_train, y_train, test_size=.25, random_state=7)
print("Using Linear Regression:")
clf = LinearRegression(fit_intercept=True, normalize=False)
clf.fit(X_train, y_train)
yhat = clf.predict(X_train)
print("Training: ", end = "")
print(((yhat-y_train)**2).mean()**(1/2))
yhat_valid =clf.predict(X_valid)
print("Valid: ", end = "")
print(((yhat_valid-y_valid)**2).mean()**(1/2))
yhat = clf.predict(X_test)
print("Test: ", end = '')
print(((yhat-y_test)**2).mean()**(1/2))
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=7) 
X_train, X_valid, y_train, y_valid = train_test_split(X_train, y_train, test_size=.25, random_state=7)


print("\n\nUsing Ridge Regression:")
clf = Ridge()
clf.fit(X_train, y_train)
yhat = clf.predict(X_train)
print("Training: ", end = "")
print(((yhat-y_train)**2).mean()**(1/2))
yhat_valid =clf.predict(X_valid)
print("Valid: ", end = "")
print(((yhat_valid-y_valid)**2).mean()**(1/2))
yhat = clf.predict(X_test)
print("Test: ", end = '')
print(((yhat-y_test)**2).mean()**(1/2))
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=7) 
X_train, X_valid, y_train, y_valid = train_test_split(X_train, y_train, test_size=.25, random_state=7)


print("\n\nUsing Extra Trees Regressor:")
clf = ensemble.ExtraTreesRegressor(n_estimators = 500)
clf.fit(X_train, y_train)
yhat = clf.predict(X_train)
print("Training: ", end = "")
print(((yhat-y_train)**2).mean()**(1/2))
yhat_valid =clf.predict(X_valid)
print("Valid: ", end = "")
print(((yhat_valid-y_valid)**2).mean()**(1/2))
yhat = clf.predict(X_test)
print("Test: ", end = '')
print(((yhat-y_test)**2).mean()**(1/2))
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=7) 
X_train, X_valid, y_train, y_valid = train_test_split(X_train, y_train, test_size=.25, random_state=7)


print("\n\nUsing Elastic Net:")
clf = ElasticNet(alpha=.001, fit_intercept=True)
clf.fit(X_train, y_train)
yhat = clf.predict(X_train)
print("Training: ", end = "")
print(((yhat-y_train)**2).mean()**(1/2))
yhat_valid = clf.predict(X_valid)
print("Valid: ", end = "")
print(((yhat_valid-y_valid)**2).mean()**(1/2))
yhat = clf.predict(X_test)
print("Test: ", end = '')
print(((yhat-y_test)**2).mean()**(1/2))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3, random_state=7) 
X_train, X_valid, y_train, y_valid = train_test_split(X_train, y_train, test_size=.3, random_state=7)
clf = ensemble.GradientBoostingRegressor(n_estimators = 500, learning_rate=.05, max_depth = 3)
clf.fit(X_train, y_train)
clf.fit(X_train, y_train)
yhat = clf.predict(X_train)
print("\n\nUsing Gradient Boosting Regressor: ")
print("Training: ", end = "")
print(((yhat-y_train)**2).mean()**(1/2))
yhat_valid =clf.predict(X_valid)
print("Valid: ", end = "")
print(((yhat_valid-y_valid)**2).mean()**(1/2))
yhat = clf.predict(X_test)
print("Test: ", end = '')
print(((yhat-y_test)**2).mean()**(1/2))
