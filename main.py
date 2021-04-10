from flask import Flask, render_template
app = Flask(__name__)


print("HELLO HACKATHON")

@app.route('/')
def upload_file():
   return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

