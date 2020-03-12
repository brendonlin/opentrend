import os
import pickle
import hashlib
import mysql.connector
from .config import DB_HOST, DB_PORT, DB_PWD, DB_USER

CACHE_DIR = "cache"

if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)


def hashcode(x):
    return hashlib.md5(bytes(x, "utf-8")).hexdigest()


def cache(func):
    def wapper(*args, **kwargs):
        self_ = args[0]
        remainArgs = args[1:]
        useCache = False
        tag = hashcode("-".join(remainArgs))
        filename = f"{func.__name__}-{tag}.pkl"
        filepath = os.path.join(CACHE_DIR, filename)
        if self_.isCache and os.path.exists(filepath):
            try:
                with open(filepath, "rb") as f:
                    result = pickle.load(f)
                    useCache = True
                    print(f"Use cache: {filepath}")
            except IOError:
                pass
        if not useCache:
            result = func(*args, **kwargs)
            # if self_.isCache:
            with open(filepath, "wb") as f:
                pickle.dump(result, f)
                # print(f"Save cache: {filepath}")
        return result

    return wapper


class DBManger:
    def __init__(self, isCache=False):
        self.isCache = isCache

    def connect(self):
        cnx = mysql.connector.connect(
            host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PWD
        )
        return cnx

    @cache
    def query(self, sql):
        cnx = self.connect()
        cur = cnx.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        fields = [x[0] for x in cur._description]
        cnx.close()
        return rows, fields
