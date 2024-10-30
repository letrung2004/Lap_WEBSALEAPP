from flask import render_template
from app import app, dao


@app.route("/")
def index():
    cates = dao.load_categories()
    pros = dao.load_products()
    return render_template('index.html', categories=cates, products=pros)


if __name__ == '__main__':
    app.run(debug=True)
