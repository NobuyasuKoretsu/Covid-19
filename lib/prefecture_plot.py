# usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by koretsunobuyasu on 2020/07/30
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# 実行するデータの指定
prefecture_df = pd.read_pickle('../data/interim/2020-07-29/prefecture_data.pkl')

def main():
    prefectures = prefecture_df['prefectureNameE'].unique()
    prefecture_df['year'] = prefecture_df['year'].astype(str)
    prefecture_df['month'] = prefecture_df['month'].astype(str).str.pad(2, fillchar='0')
    prefecture_df['date'] = prefecture_df['date'].astype(str).str.pad(2, fillchar='0')
    prefecture_df['Date'] = pd.to_datetime(
        prefecture_df['year'] + '-' + prefecture_df['month'] + '-' + prefecture_df['date'])
    prefectures_df = prefecture_df.groupby('prefectureNameE')
    prefectures = ['Tokyo', 'Saitama', 'Kanagawa', 'Tochigi', 'Chiba', 'Hyogo', 'Osaka', 'Aichi', 'Gifu']
    plt.figure(figsize=(20, 10))
    plt.title('Death')
    for prefecture in prefectures:
        target_pref = prefectures_df.get_group(prefecture)
        print(prefecture, target_pref.tail(1)['deaths'])
        plt.bar(target_pref['Date'], target_pref['deaths'], label=f'{prefecture}')
    plt.legend()
    plt.show()
    plt.figure(figsize=(20, 10))
    plt.title('Positive')
    for prefecture in prefectures:
        target_pref = prefectures_df.get_group(prefecture)
        plt.bar(target_pref['Date'], target_pref['testedPositive'], label=f'{prefecture}')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()