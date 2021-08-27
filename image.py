import matplotlib.cm as cm
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/file.csv")

# Data cleaning
valid_sale_type = ["MLS Listing", "New Construction Home", "New Construction Plan"]
df = df[df["SALE TYPE"].isin(valid_sale_type)]

# Drop everything without a price
df = df.dropna(subset=["PRICE"])

df["HOA/MONTH"] = df["HOA/MONTH"].fillna(0)


def distrColor():
    plt.figure()
    plt.scatter(
        df.LATITUDE,
        df.LONGITUDE,
        alpha=0.5,
        c=df["PRICE"],
        cmap=plt.get_cmap("jet"),
        s=6,
    )
    cbar = plt.colorbar()
    plt.clim(df.PRICE.quantile(0.25), df.PRICE.quantile(0.75))
    labels = cbar.ax.get_yticks()
    cbar.ax.set_yticklabels(["${:,.0f}".format(l) for l in labels])
    plt.title("Distribution of homes, with gradient of price")
    plt.xlabel("Latitude")
    plt.ylabel("Longitude")
    plt.show()


def allPrices():
    plt.figure()
    df["PRICE"].hist(bins=20)
    plt.xlim(df.PRICE.min(), df.PRICE.max())
    locs, labels = plt.xticks()
    plt.xticks(locs, ["${:,.0f}".format(l) for l in locs])

    plt.title("How is the Price variable distributed?")
    plt.xlabel("Price")
    plt.ylabel("Total number of homes")
    plt.show()


def pricePerCity():
    plt.figure()
    cities = df.groupby("CITY").mean()["PRICE"].sort_values()
    top_5 = cities[-5:]
    bot_5 = cities[:5]
    fig, ax = plt.subplots(1, 2)
    pal_red = sns.color_palette("Reds_d", len(top_5))
    pal_green = sns.color_palette("Greens_d", len(top_5))[::-1]

    sns.barplot(top_5.keys(), top_5.values, ax=ax[0], palette=np.array(pal_red))
    sns.barplot(bot_5.keys(), bot_5.values, ax=ax[1], palette=np.array(pal_green))
    ax[0].set_yticklabels(["${:,.0f}".format(l) for l in ax[0].get_yticks()])
    ax[1].set_yticklabels(["${:,.0f}".format(l) for l in ax[1].get_yticks()])
    ax[0].set_title("Most Expensive cities")
    ax[1].set_title("Least Expensive cities")
    plt.show()


def beds():
    plt.bar(x=df.BEDS, height=df.PRICE)
    locs, labels = plt.yticks()
    plt.yticks(locs, ["${:,.0f}".format(l) for l in locs])

    plt.title("Average price based on beds")
    plt.xlabel("# of beds")
    plt.ylabel("Average price")


def hoa():
    # making a new binary variable
    df["HOA"] = df["HOA/MONTH"].apply(lambda x: "REQUIRED" if x != 0 else "NOTREQUIRED")
    sns.boxplot(x="HOA", y="PRICE", data=df)
    plt.ylim(0, df.PRICE.max())
    locs, labels = plt.yticks()
    plt.yticks(locs, ["${:,.0f}".format(l) for l in locs])
    plt.title("Do homes with a HOA have a higher price?")

    plt.show()


def age():
    plt.figure()
    plt.bar(x=df["YEAR BUILT"], height=df.PRICE)
    # plt.xlim(0, 200)
    locs, labels = plt.yticks()
    plt.yticks(locs, ["${:,.0f}".format(l) for l in locs])
    plt.title("Price vs Year Built")
    plt.xlabel("Age")
    plt.ylabel("Price")
    plt.show()


age()
