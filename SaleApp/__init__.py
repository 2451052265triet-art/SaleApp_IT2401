from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    categories = [{
        'id': 1,
        'name': 'Ứng dụng'
    }, {
        'id': 2,
        'name': 'Sản Phẩm'
    }, {
        'id': 3,
        'name': 'Tiện ích'
    }]
    return render_template("index.html", categories=categories)


if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)
