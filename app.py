from flask import Flask,render_template
from middleware import middleware

app = Flask(__name__)

app.wsgi_app = middleware(app.wsgi_app)

@app.route('/', methods=['GET'])
def index():
    return render_template("some_random.html")


if __name__ == "__main__":
    app.run(debug=True)
