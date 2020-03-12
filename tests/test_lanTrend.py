from opentrend import lanTrend


def test_readDataset():
    df = lanTrend.getDataset()
    print(df)
