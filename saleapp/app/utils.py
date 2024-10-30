from flask import render_template
from app import app, dao
from flask import request


@app.route("/")
def index():
    cates = dao.load_categories()
    kw = request.args.get('kw')
    prods = dao.load_products(kw)
    return render_template('index.html', categories=cates, products=prods)


if __name__ == '__main__':
    app.run(debug=True)
