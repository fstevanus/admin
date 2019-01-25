from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "sdsds"

@app.route("/base")
def base():
    data = [
        {
            'Name' : 'as',
            'Position' : 'as',
            'Office' : 'as',
            'Age': 'as',
            'Start' : 'as',
            'Salary' : 'as'
        },
        {
            'Name' : 'sa',
            'Position' : 'sa',
            'Office' : 'sa',
            'Age': 'sa',
            'Start' : 'sa',
            'Salary' : 'sa'
        }
    ]
    return render_template("app.html", data = data)

if __name__ == "__main__":
    app.run(debug=True)