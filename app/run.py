from flask import Flask, render_template, flash , redirect, url_for,session, logging, request
from data import Inventory
from data import Currency
import logging
app = Flask(__name__)
money = Currency()
invo = Inventory()
shop_items = invo.items()


@app.route('/')
def index():
    app.logger.info('Hello World')
    app.logger.info(shop_items[1].title)
    for i in shop_items.values():
        app.logger.info(i.filepath)

    amount = money.get_rupee()
    return render_template('index.html', shop_items=shop_items.values(),amount=amount)


@app.route('/add_rupee/<int:amount>')
def add_rupee(amount):    
    total = money.get_rupee() + amount
    money.set_rupee(total)
    return redirect(url_for('index'))

@app.route('/purchase_item/<int:id>')
def purchase_item(id):
    shop_items[id]
    flash(f'Hey...nice choice...Everyone needs a {shop_items[id].title} !')
    return redirect(url_for('index'))

@app.route('/confirm_purchase/<int:current_id>')
def confirm_purchase(current_id):
    
    app.logger.info(current_id)
   
    if money.get_rupee() >= shop_items[current_id].price:
        flash(f'Thanks! Enjoy! Buy more?')
        money.set_rupee(money.get_rupee() - shop_items[current_id].price)
        return redirect(url_for('index'))
    else:
        flash('Not enough rupees!')
    return redirect(url_for('index'))    

if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)

