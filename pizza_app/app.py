from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Меню піц
menu = [
    {"name": "Маргарита", "price": 150, "icon": "🍕"},
    {"name": "Пепероні", "price": 180, "icon": "🍕"},
    {"name": "Гавайська", "price": 170, "icon": "🍍"},
    {"name": "4 Сири", "price": 200, "icon": "🧀"},
    {"name": "М’ясна", "price": 220, "icon": "🥩"},
    {"name": "Кола", "price": 50, "icon": "🥤"}
]

cart = []

@app.route("/")
def index():
    return render_template("index.html", menu=menu, cart_count=len(cart))

@app.route("/add_to_cart/<item_name>")
def add_to_cart(item_name):
    for item in menu:
        if item["name"] == item_name:
            cart.append(item)
            break
    return redirect(url_for("index"))

@app.route("/cart")
def view_cart():
    total = sum(item["price"] for item in cart)
    return render_template("cart.html", cart=cart, total=total)

@app.route("/clear_cart")
def clear_cart():
    cart.clear()
    return redirect(url_for("view_cart"))

if __name__ == "__main__":
    app.run(debug=True)
