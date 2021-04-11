from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)


def loadFiles():
    part1 = pd.read_csv("./Dataset/hack_illinois_part1.csv", sep = ",", header = 0, engine='python')
    print("Loaded part1")
    part2 = pd.read_csv("./Dataset/hack_illinois_part2.csv", sep = ",", header = 0, engine='python')
    print("Loaded part 2")
    return part1.append(part2)

print("Hello Hackathon!!!")
@app.route('/')
def upload_file():
    print("In upload file")
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    print("Loading files....")
    loadFiles()

if __name__ == '__main__':
    app.run(debug=True)


