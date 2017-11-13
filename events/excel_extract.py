

import pandas as pd
import datetime

#header = ['Event','Date','Price','Overview','Detail']
#pd.read_excel(sheetname='Events', header=header, skiprows=0)

xl = pd.ExcelFile("BTC_Events.xlsx")
xl.sheet_names

df = xl.parse("Events")
df.header()

print df


data2 = [{
        'x' : datetime.datetime(2015, 6, 8),
        'title' : 'C',
        'text' : 'Stocks fall on Greece, rate concerns; US dollar dips'
    }, {
        'x' : datetime.datetime(2015, 6, 12),
        'title' : 'D',
        'text' : 'Zimbabwe ditches \'worthless\' currency for the US dollar '
    }]