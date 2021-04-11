import pandas as pd
import datetime
from bokeh.plotting import figure, show
from bokeh.models import DatetimeTickFormatter
from math import pi
import statistics


def getFuelInsights (dataset):
    groupedDict = dataset.groupby(['Asset type', 'AssetID']).apply(lambda x: dict(zip(x['Date'], x['Fuel Level (%)']))).to_dict()
    fuelData = {}
    for key in groupedDict.keys():
        value = groupedDict[key]
        tmp = 0
        lastDate = '0'
        refilDates = {}
        for date in value.keys():
            if tmp == 0:
                tmp = value[date]
                lastDate = date
                continue
            if (int(value[date]) > int(tmp)):
                d0 = datetime.datetime(int(lastDate.split("-")[0]), int(lastDate.split("-")[1]), int(lastDate.split("-")[2]))
                d1 = datetime.datetime(int(date.split("-")[0]), int(date.split("-")[1]), int(date.split("-")[2]))
                delta = d1 - d0
                refilDates[pd.to_datetime(date, format='%Y-%m-%d')] = delta.days
                lastDate = date
            tmp = value[date]
        fuelData[str(key[0])+"_"+str(key[1])] = refilDates
    return fuelData


def showFuelInsightsFor(fuelData, asssetId = "1022017", assetType = "Excavator"):
    output_file("./templates/Fuel.html")
    p = figure(title="Fuel Refill Dates vs days it worked before refill", x_axis_label='Refill Date',
               y_axis_label='No of Days', plot_width=1000)
    x = list(fuelData[assetType + "_" + asssetId].keys())
    y = list(fuelData[assetType + "_" + asssetId].values())
    p.circle(x, y, fill_alpha=0.2, size=5)
    p.xaxis.formatter = DatetimeTickFormatter(
            hours=["%d %B %Y"],
            days=["%d %B %Y"],
            months=["%d %B %Y"],
            years=["%d %B %Y"],
        )
    p.xaxis.major_label_orientation = pi/4
    lastDate = datetime.datetime.strptime(x[-1], "%m/%d/%y")
    # A naive approach to choose the next prediction date.
    # We can use Machine learning time series prediction (ARIMA Approach) to predict the next few dates for refill.
    delta = statistics.mode(y)
    nextPredictedDate = lastDate + datetime.timedelta(days=delta)
    print("Next Refill Date : " + nextPredictedDate)
    show(p)


