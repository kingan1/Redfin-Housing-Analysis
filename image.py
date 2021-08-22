import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.ticker as ticker

df = pd.read_csv("data/file.csv")
df.drop(["STATUS"], axis=1, inplace=True)
df = df.dropna(
    subset=[
        "LOCATION",
        "PRICE",
        "CITY",
        "LOT SIZE",
        "BEDS",
        "BATHS",
        "DAYS ON MARKET",
        "SQUARE FEET",
    ]
)
df["HOA/MONTH"] = df["HOA/MONTH"].fillna(0)
mapper = cm.ScalarMappable()
mapper.set_array(df["PRICE"])


def distrColor():
    plt.scatter(
        df.LATITUDE,
        df.LONGITUDE,
        alpha=0.5,
        c=df["PRICE"],
        cmap=plt.get_cmap("jet"),
        s=6,
    )
    plt.colorbar()
    plt.clim(50000, 500000)
    plt.title("Distribution of homes, with gradient of price")
    plt.xlabel("Latitude")
    plt.ylabel("Longitude")


def allPrices():
    df["PRICE"].hist(bins=20)
    plt.xlim(df.PRICE.min(), df.PRICE.max())
    locs, labels = plt.xticks()
    plt.xticks(locs, ["${:,.0f}".format(l) for l in locs])

    plt.title("All prices")
    plt.xlabel("Price")
    plt.ylabel("Total number of homes")


def averagePrice():
    cities = df.CITY.unique()
    plt.bar(x=df.CITY, height=df.PRICE)
    plt.ylim(50000)
    plt.tight_layout()
    locs, labels = plt.yticks()
    plt.yticks(locs, ["${:,.0f}".format(l) for l in locs])
    plt.title("Average price per city")
    plt.xlabel("City")
    plt.ylabel("Price")
    plt.xticks(rotation=90)


def beds():
    plt.bar(x=df.BEDS, height=df.PRICE)
    locs, labels = plt.yticks()
    plt.yticks(locs, ["${:,.0f}".format(l) for l in locs])

    plt.title("Average price based on beds")
    plt.xlabel("# of beds")
    plt.ylabel("Average price")


def bedsVsBaths():
    df["Corr"] = (df["BEDS"] / df["BATHS"]).round().astype("int") + 1
    plt.bar(x=df.Corr, height=df["PRICE"])
    plt.xlim(0)
    locs, labels = plt.yticks()
    plt.yticks(locs, ["${:,.0f}".format(l) for l in locs])

    plt.title("Percentage of beds/baths correlated to price")
    plt.xlabel("# of beds / # of baths")
    plt.ylabel("Price")


def age():
    plt.bar(x=df.AGE, height=df.PRICE)
    plt.xlim(0, 200)
    locs, labels = plt.yticks()
    plt.yticks(locs, ["${:,.0f}".format(l) for l in locs])
    plt.title("Price vs Year Built")
    plt.xlabel("Age")
    plt.ylabel("Price")


df["YEAR BUILT"] = df["YEAR BUILT"].fillna(1980)
df["AGE"] = 2021 - df["YEAR BUILT"]
plt.figure(0)
age()
plt.figure(1)
bedsVsBaths()
plt.figure(2)
beds()
plt.figure(3)
allPrices()
plt.figure(4)
averagePrice()
plt.figure(5)
distrColor()
plt.show()
