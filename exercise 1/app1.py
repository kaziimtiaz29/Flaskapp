from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'hello world'

@app.route('/about')
def about():
    return 'This is the about page'
@app.route('/about/<int:n>')
def about1(n):
    return str(n*n)

if __name__ == "__main__":
    app.run(debug=True)