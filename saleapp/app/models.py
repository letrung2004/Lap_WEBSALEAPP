from sqlalchemy.orm import relationship
from app import db, app
from sqlalchemy import Column, Integer, String, Float, ForeignKey


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=False)
    description = Column(String(250), nullable=True)
    price = Column(Float, default=0)
    image = Column(String(250), nullable=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)


if __name__ == '__main__':
    with app.app_context():
        # db.create_all()
        # c1 = Category(name='Mobile')
        # c2 = Category(name='Tablet')
        # c3 = Category(name='Desktop')
        #
        # db.session.add_all([c1, c2, c3])
        # db.session.commit()
        data = [{
            "id": 1,
            "name": "iPhone 14 Pro",
            "description": "Apple, 32GB, RAM: 3GB, iOS13",
            "price": 17000000,
            "image":
                "https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:90/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone-12.png",
            "category_id": 1
        }, {
            "id": 2,
            "name": "iPad Pro 2024",
            "description": "Apple, 128GB, RAM: 6GB",
            "price": 37000000,
            "image":
                "https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:90/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone-12.png",
            "category_id": 2
        },
            {
                "id": 3,
                "name": "Galaxy Note 10 Plus",
                "description": "Samsung, 64GB, RAML: 6GB",
                "price": 24000000,
                "image":
                    "https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:90/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone-12.png",
                "category_id": 1
            }
            , {
                "id": 4,
                "name": "Galaxy Note 10 Plus",
                "description": "Samsung, 64GB, RAML: 6GB",
                "price": 24000000,
                "image":
                    "https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:90/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone-12.png",
                "category_id": 1
            }

            , {
                "id": 5,
                "name": "Galaxy Note 10 Plus",
                "description": "Samsung, 64GB, RAML: 6GB",
                "price": 24000000,
                "image":
                    "https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:90/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone-12.png",
                "category_id": 1
            }

            , {
                "id": 6,
                "name": "Galaxy Note 10 Plus",
                "description": "Samsung, 64GB, RAML: 6GB",
                "price": 24000000,
                "image":
                    "https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:90/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone-12.png",
                "category_id": 1
            }

            , {
                "id": 7,
                "name": "Galaxy Note 10 Plus",
                "description": "Samsung, 64GB, RAML: 6GB",
                "price": 24000000,
                "image":
                    "https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:90/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone-12.png",
                "category_id": 1
            }
            , {
                "id": 8,
                "name": "Galaxy Note 10 Plus",
                "description": "Samsung, 64GB, RAML: 6GB",
                "price": 24000000,
                "image":
                    "https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:90/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone-12.png",
                "category_id": 1
            }
        ]
        for p in data:
            pro = Product(name=p['name'], description=p['description'], price=p['price'],
                          image=p['image'], category_id=p['category_id'])
            db.session.add(pro)
        db.session.commit()
