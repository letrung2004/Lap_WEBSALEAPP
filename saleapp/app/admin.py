from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app import db, app
from app.models import BookCategory, Book

admin = Admin(app=app, name="E-commerce Administration",
              template_mode="bootstrap4")


class BookView(ModelView):
    # Hiển thị category dưới dạng tên thay vì khóa ngoại ID
    column_list = ['name', 'author', 'description', 'price', 'image', 'active', 'created_date', 'category']  # Hiển thị tên category
    form_columns = ['name', 'author', 'description', 'price', 'image', 'active', 'created_date', 'category_id']  # Người dùng chọn category
    column_labels = {
        'name': 'Book Name',
        'author': 'Author',
        'description': 'Description',
        'price': 'Price',
        'image': 'Image',
        'active': 'Active',
        'created_date': 'Created Date',
        'category': 'Category'
    }


admin.add_view(ModelView(BookCategory, db.session))
admin.add_view(BookView(Book, db.session))
