from matplotlib import pyplot as plt
import pandas as pd
from .dbmanage import DBManger

# PATH ="data/data.csv"

sql = """
SELECT `language` as lan,created_day,period,sum(period_stars_count) as stars
FROM lake.opentrend
where `hour`= 18
-- and created_day >= "2020-01-02"
and period = "monthly"
group by 1,2,3
"""


def getDataset():
    dbm = DBManger()
    data, fields = dbm.query(sql)
    df = pd.DataFrame(data, columns=fields)
    return df


class Koa:
    def __init__(self):
        pass

    def getTable(self):
        df = getDataset()
        mdf = df[df["period"] == "monthly"]
        mdf["stars"] = mdf["stars"].astype("float64")
        table = pd.pivot_table(mdf, "stars", "created_day", "lan")
        table.fillna(0, inplace=True)
        smoothTable = table.rolling(window=30).mean()
        lanRank = smoothTable.sum(0).sort_values(ascending=False)
        topLan = lanRank[:20].index.tolist()
        smoothTable = smoothTable.loc[:, topLan]
        return smoothTable


def main():
    koa = Koa()
    smoothTable = koa.getTable()
    perTable = (smoothTable.T / smoothTable.sum(1)).T
    perTable.plot()
    plt.show()

