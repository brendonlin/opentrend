from opentrend import dbmanage


def test_dbmanage():
    dbm = dbmanage.DBManger()
    data,fields = dbm.query("select * from lake.opentrend limit 1")
    assert len(data) >= 1
    