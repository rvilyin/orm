
import peewee
from models import Category, Product


def post_category(category_name):
    try:
        category = Category(name = category_name)
        category.save()
        print('SAVED!!!!!')
    except peewee.IntegrityError:
        print('ТАКАЯ КАТЕГОРИЯ УЖЕ СУЩЕСТВУЕТ!!!')

# post_category('game2')
# post_category('game3')
# post_category('game4')
# post_category('game5')


def get_categories():
    categories = Category.select()
    for category in categories:
        print(f'{category.id} -- {category.name} -- {category.created_at}')

# get_categories()

def delete_category(category_id):
    try:
        category = Category.get(id = category_id)
        category.delete_instance()
        print('DELETE!!!!!')
    except peewee.DoesNotExist:
        print('Категория не найдена!!!')

def update_category(category_id, new_name):
    try:
        category = Category.get(id = category_id)
        category.name = new_name
        category.save()
    except peewee.DoesNotExist:
        print('Категория не найдена!!!')

# get_categories()
# delete_category(1)
# update_category(3, 'John')
# get_categories()

def detail_category(id_category):
    try:
        category = Category.get(id = id_category)
        print(category.id, end = '\t')
        print(category.name, end = '\t')
        print(category.created_at)
        # print(category.products)
        for i in category.products:
            print(f'{i.name} -- {i.price} -- {i.amount}')
    except peewee.DoesNotExist:
        print('нет такой категории')


def post_product(name, price, amount, category):
    try:
        product = Product(name = name, price = price, amount = amount, category = category)
        product.save()
    except peewee.IntegrityError:
        print('такой категории не существует')


# post_product('product3', 30, 10, 8)


# detail_category(2)


def get_products():
    products = Product.select()
    for product in products:
        print(f'{product.id} -- {product.name} -- {product.price} -- {product.amount} -- {product.category}')

# get_products()

def get_product_by_name(name):
    products = Product.select().where(Product.name == name)
    for product in products:
        print(product.name, product.price)

