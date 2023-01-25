
# ORM (Object Relational Mapping - объектно реляционное отображение) - технология которая связывает БД с концепциями объектно ориентированных языков программирования. ORM - прослойка между БД и кодом который пишет программист, которая позволяет создавать в программе объекты, обновлять, удалять и получать их

# python:
    # peewee
    # sqlalchemy
    # DjangoORM

# Класс - Таблица в БД
# Атрибут класса - поле в БД
# Объект класса - строка в таблице

from settings import db
from views import *


db.connect()
# Category.create_table()
# Product.create_table()


# category = Category(name='game')
# category.save()

get_categories()
get_products()
get_product_by_name('product1')
