# usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by koretsunobuyasu on 2020/07/29
from datetime import datetime

# original data and interim data
# TODO: strftimeを日付は引数に変更する必要あり...?(午前に回す場合前日のデータが必要になったりするから)
ORIGINAL_CSV_DIR = f'../data/original/{datetime.now().strftime("%Y-%m-%d")}'
ORIGINAL_DIR_INTERIM = f'../data/interim/{datetime.now().strftime("%Y-%m-%d")}'
CASES = ORIGINAL_CSV_DIR + '/cases_total.csv'
DEATH = ORIGINAL_CSV_DIR + '/death_total.csv'
PCR_POSITIVE = ORIGINAL_CSV_DIR + '/pcr_positive_daily.csv'
PCR_TESTED = ORIGINAL_CSV_DIR + '/pcr_tested_daily.csv'
PREFECTURE = ORIGINAL_CSV_DIR + '/prefectures.csv'

TMP = '/tmp'