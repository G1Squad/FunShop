from flask import Blueprint, render_template
from .services import getCategory, getTrendingCategories, getProduct, getTrendingProducts
from flask_security import current_user

productBluePrint = Blueprint('product', __name__)

@productBluePrint.route('/')
def index() -> str:
    trendingCategories = []
    trendingCategories = getTrendingCategories()
    trendingProducts = getTrendingProducts()
    return render_template('products/index.html',trendingCategories=trendingCategories,
        products=trendingProducts
    )

@productBluePrint.route('/category/<id>')
def category(id) -> str:
    category = getCategory(id)
    return render_template('products/category.html',category=category)

@productBluePrint.route('/product/<id>')
def product(id) -> str:
    product = getProduct(id)
    return render_template('products/product.html',product=product)

@productBluePrint.route('/debug-auth')
def debug_auth():
    return f"Is authenticated: {current_user.is_authenticated}"