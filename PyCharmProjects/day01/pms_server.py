from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/about-us')
def about_us():
    return render_template('about_us.html')


@app.route('/add-product')
def add_product():
    return render_template('add_product.html')


@app.route('/product-list')
def product_list():
    return render_template('product_list.html')


if __name__ == '__main__':
    app.run(port=8080, debug=True)
