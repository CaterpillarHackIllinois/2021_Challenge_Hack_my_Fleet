import pandas as pd

def loadFiles():
    part1 = pd.read_csv("./Dataset/hack_illinois_part1.csv", sep = ",", header = 0, engine='python')
    # part2 = pd.read_csv("./Dataset/hack_illinois_part2.csv", sep = ",", header = 0, engine='python')
    return part1

#AssetID        Date    Asset type  ...  Fuel Level (%)  GPS Lattitude  GPS Longitude
def fuelHistory():
    dataset = loadFiles()
    print(dataset.head())
    # Group by asset Type. for every assetId find the refil date and a count for how many days it took to refil
    # groupedData = dataset.groupby(['Asset type', 'AssetID'])
    # print(groupedData.describe())
    groupedDict = dataset.groupby(['Asset type', 'AssetID']).apply(lambda x: dict(zip(x['Date'], x['Fuel Level (%)']))).to_dict()
    return str(groupedDict)
