# usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by koretsunobuyasu on 2020/07/29
import os
import pandas as pd
from datetime import datetime
from datetime import date
import glob
os.chdir('../')
import defs as d
os.chdir('./datasource')

def read_prefecture_data(path=''):
    if date == '':
        dataset = pd.read_pickle(d.ORIGINAL_DIR_INTERIM + '/prefecture_data.pkl')
    else:
        dataset = pd.read_pickle(f'{path}/prefecture_data.pkl')
    return dataset

def prefecturedata_to_pickle():

    # read prefecture csv
    prefecture_df = pd.read_csv(d.PREFECTURE)

    prefecture_df = prefecture_df.sort_values(['prefectureNameE', 'year', 'month', 'date'])
    prefecture_df = prefecture_df.fillna(0)

    prefecture_df['peopleTested'] = prefecture_df['peopleTested'].astype(int)
    prefecture_df['discharged'] = prefecture_df['discharged'].astype(int)
    prefecture_df['deaths'] = prefecture_df['deaths'].astype(int)
    prefecture_df = prefecture_df.reset_index()
    prefecture_df.drop('index', axis=1, inplace=True)

    prefecture_df.to_pickle(d.ORIGINAL_DIR_INTERIM + '/prefecture_data.pkl')