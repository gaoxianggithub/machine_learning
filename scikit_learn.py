import os
import tarfile
from urllib.request import urlretrieve

import pandas as pd

DOWNLOAD_ROOT = "https://github.com/gaoxianggithub/handson-ml2/tree/master/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"


def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    # print(housing_url)
    # os.makedirs(housing_path, exist_ok=True)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    # urlretrieve(url=housing_url, filename=tgz_path)
    housing_tgz = tarfile.open('D:\demo\PycharmProjects\handson-ml2\datasets\housing\housing.tgz')
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()


fetch_housing_data(HOUSING_URL, HOUSING_PATH)


def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)


housing = load_housing_data()
housing.head()
print('运行结束')
