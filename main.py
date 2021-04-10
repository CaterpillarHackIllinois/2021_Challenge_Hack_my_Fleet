from flask import Flask, render_template
from Insights.Fuel import fuelHistory
app = Flask(__name__)


print("HELLO HACKATHON")

@app.route('/')
def upload_file():
    return render_template('index.html')

@app.route('/fuel_insights')
def fuel_insights():
    value = fuelHistory()
    print(value)
    return value

if __name__ == '__main__':
    app.run(debug=True)


