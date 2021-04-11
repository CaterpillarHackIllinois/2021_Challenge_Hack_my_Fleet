# 2021_Challenge_Hack_my_Fleet
### Show your ninja skills hacking a ***Fleet Management System*** data and be the coolest dude in town!
### Sponsored by *Caterpillar*

Follow these links to download the full datasets		

- https://www.dropbox.com/s/84r4qoj1exk3u5g/hack_illinois_part1.csv?dl=0		
- https://www.dropbox.com/s/u806pe2tabf4qo6/hack_illinois_part2.csv?dl=0		

## Description
The challenge is described in pdf : Caterpillar Challenge HackIllinois. 

## Team 

Anagh Seshagiri Sharma (Github: anagh0sharma) <br>
Anisha Jauhari (Github: anisha1095) <br>
Nikhil Shenoy (Github: nshenoy3) <br>

## Installation

```bash
pip install flask
pip install bokeh
```
Since the dataset files are huge, we could not include them in out github project.
Create a Dataset folder in the project directory and copy the dataset files to this directory.

## Project Implementation Idea : 
1. **Asset Tracking :** This feature aims to show the path traveled by each assetId over the course of a year. For this we have used Google Maps and Bokeh geomaps to view the position of each assetId on a particular day. A future development of this could include a geofencing application and alerting for a particular assetId if it goes out of its confined area.
2. **Fuel Refill Prediction** : This feature analyses the past data and calculates the refill dates of each assetId based on the fuel level percentage. Further it predicts the future refill dates based on the past trend and usage. 
3. **Best Performing Asset** : This feature aims to rank each assetId per asset type based on its fuel consumption and total hours it worked for. This is just a indicator chart to inform product managers which asset needs maintenance or is performing poorly.

## Files
**maps.py** : Implements the Asset Tracking Idea. Produces templates/maps.html.<br>
**asset.py** : Implements the Best performing asset Idea. Produces templates/asset.html<br>
**Fuel.py** : Implements the Fuel Refill Prediction. Produces templates/Fuel.html <br>

## Usage

## Screenshots
