from flask import Flask, render_template

app = Flask(__name__)

app.route("/",  )
def index():
    # return render_template ('index.html')
    return 'hello'

app.route("/register")
def index():
    # return render_template ('index.html')
    return 'register here'

if __name__ == '__main__':
    app.run(debug=True)
