from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app import db, app
from app.models import Category, Product

admin = Admin(app, name="Quan ly ban hang",
              template_mode="bootstrap3")
admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Product, db.session))
