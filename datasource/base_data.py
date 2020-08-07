# usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by koretsunobuyasu on 2020/07/29
import pandas as pd
from datetime import datetime
from datetime import date
import os
os.chdir('../')
import defs as d
os.chdir('./datasource')
import glob


def read_basedata(date=''):
    if date == '':
        dataset = pd.read_pickle(d.ORIGINAL_DIR_INTERIM + '/basedata.pkl')
    else:
        dataset = pd.read_pickle(d.ORIGINAL_DIR_INTERIM + f'../{date}/basedata.pkl')
    return dataset

def basedata_to_pickle():
    # read csv
    cases_df = pd.read_csv(d.CASES)
    death_df = pd.read_csv(d.DEATH)
    positive_df = pd.read_csv(d.PCR_POSITIVE)
    tested_df = pd.read_csv(d.PCR_TESTED)
    final_df = pd.DataFrame()
    final_df = pd.merge(cases_df, death_df, on='日付', how='left')
    final_df = pd.merge(final_df, positive_df, on='日付', how='left')
    final_df = pd.merge(final_df, tested_df, on='日付', how='left')

    final_df = final_df.fillna(0)

    final_df.rename(columns={'日付':'date','入院治療を要する者': 'hospitalization_required', '死亡者数': 'number_of_death', 'PCR 検査陽性者数(単日)': 'pcr_number_of_positives__single_day','PCR 検査実施件数(単日)': 'pcr_number_of_cases__single_day'} , inplace=True)
    final_df['number_of_death'] = final_df['number_of_death'].astype(int)
    final_df['pcr_number_of_cases__single_day'] = final_df['pcr_number_of_cases__single_day'].astype(int)

    final_df.to_pickle(d.ORIGINAL_DIR_INTERIM + '/basedata.pkl')