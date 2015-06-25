#!/usr/bin/env python
from __future__ import print_function, division

from operator import itemgetter

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# URL = 'https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv'
URL = 'loansData.csv'


def load_data():
    return pd.read_csv(URL, dtype={'Interest.Rate': np.str, 'Loan.Length': np.str})


def clean_data(df):
    df['Interest.Rate'] = df['Interest.Rate'].str.replace('%', '').astype('float')
    df['Loan.Length'] = df['Loan.Length'].str.replace(' months', '').astype('int')
    df['FICO.Score'] = df['FICO.Range'].str.split('-').apply(itemgetter(0)).astype('int')


def plot_data(loansData):
    plt.figure()
    p = loansData['FICO.Score'].hist(bins=20)
    plt.show()

    a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')
    plt.show()


def main():
    loansData = load_data()
    clean_data(loansData)
    plot_data(loansData)


if __name__ == '__main__':
    main()
