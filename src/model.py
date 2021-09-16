"""

Creates models based on our data

"""
import pandas as pd
from sklearn import ensemble
from sklearn.linear_model import ElasticNet
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split


def run():
    df = pd.read_csv("data/file.csv")
    df = df.dropna(
        subset=[
            "LOCATION",
            "PRICE",
            "CITY",
            "BEDS",
            "BATHS",
            "LOT SIZE",
            "DAYS ON MARKET",
            "SQUARE FEET",
        ]
    )
    print(df["SALE TYPE"].unique())
    # not sure purpose of this line
    # df["SALE TYPE"] = df[df["SALE TYPE"] == "MLS Listing"]
    df["HOA/MONTH"] = df["HOA/MONTH"].fillna(0)
    df["YEAR BUILT"] = df["YEAR BUILT"].fillna(1980)
    df["CITY"] = df["CITY"].astype("category")
    df["LOCATION"] = df["LOCATION"].astype("category")
    df["PROPERTY TYPE"] = df["PROPERTY TYPE"].astype("category")
    df["AGE"] = 2021 - df["YEAR BUILT"]
    df = df.drop(
        columns=[
            "SALE TYPE",
            "ADDRESS",
            "ZIP OR POSTAL CODE",
            "STATE OR PROVINCE",
            "SOURCE",
            "MLS#",
            "$/SQUARE FEET",
        ]
    )
    df = pd.get_dummies(df, columns=["CITY"])
    df = pd.get_dummies(df, columns=["LOCATION"])
    df = pd.get_dummies(df, columns=["PROPERTY TYPE"])
    X = df
    y = df["PRICE"]
    X = X.drop(columns=["PRICE"])
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=7
    )
    X_train, X_valid, y_train, y_valid = train_test_split(
        X_train, y_train, test_size=0.25, random_state=7
    )

    print("Using Linear Regression:")
    clf = LinearRegression(fit_intercept=True, normalize=False)
    clf.fit(X_train, y_train)
    yhat = clf.predict(X_train)
    print("Training: ", end="")
    print(((yhat - y_train) ** 2).mean() ** (1 / 2))
    yhat_valid = clf.predict(X_valid)
    print("Valid: ", end="")
    print(((yhat_valid - y_valid) ** 2).mean() ** (1 / 2))
    yhat = clf.predict(X_test)
    print("Test: ", end="")
    print(((yhat - y_test) ** 2).mean() ** (1 / 2))

    print("\n\nUsing Ridge Regression:")
    clf = Ridge()
    clf.fit(X_train, y_train)
    yhat = clf.predict(X_train)
    print("Training: ", end="")
    print(((yhat - y_train) ** 2).mean() ** (1 / 2))
    yhat_valid = clf.predict(X_valid)
    print("Valid: ", end="")
    print(((yhat_valid - y_valid) ** 2).mean() ** (1 / 2))
    yhat = clf.predict(X_test)
    print("Test: ", end="")
    print(((yhat - y_test) ** 2).mean() ** (1 / 2))

    print("\n\nUsing Extra Trees Regressor:")
    clf = ensemble.ExtraTreesRegressor(n_estimators=500)
    clf.fit(X_train, y_train)
    yhat = clf.predict(X_train)
    print("Training: ", end="")
    print(((yhat - y_train) ** 2).mean() ** (1 / 2))
    yhat_valid = clf.predict(X_valid)
    print("Valid: ", end="")
    print(((yhat_valid - y_valid) ** 2).mean() ** (1 / 2))
    yhat = clf.predict(X_test)
    print("Test: ", end="")
    print(((yhat - y_test) ** 2).mean() ** (1 / 2))

    print("\n\nUsing Elastic Net:")
    clf = ElasticNet(alpha=0.001, fit_intercept=True)
    clf.fit(X_train, y_train)
    yhat = clf.predict(X_train)
    print("Training: ", end="")
    print(((yhat - y_train) ** 2).mean() ** (1 / 2))
    yhat_valid = clf.predict(X_valid)
    print("Valid: ", end="")
    print(((yhat_valid - y_valid) ** 2).mean() ** (1 / 2))
    yhat = clf.predict(X_test)
    print("Test: ", end="")
    print(((yhat - y_test) ** 2).mean() ** (1 / 2))

    clf = ensemble.GradientBoostingRegressor(
        n_estimators=500, learning_rate=0.05, max_depth=3
    )
    clf.fit(X_train, y_train)
    clf.fit(X_train, y_train)
    yhat = clf.predict(X_train)
    print("\n\nUsing Gradient Boosting Regressor: ")
    print("Training: ", end="")
    print(((yhat - y_train) ** 2).mean() ** (1 / 2))
    yhat_valid = clf.predict(X_valid)
    print("Valid: ", end="")
    print(((yhat_valid - y_valid) ** 2).mean() ** (1 / 2))
    yhat = clf.predict(X_test)
    print("Test: ", end="")
    print(((yhat - y_test) ** 2).mean() ** (1 / 2))


if __name__ == "__main__":
    run()
