#Product
product_1 = "Woreless Mouse"
product_2 = "Gaming Keyboard"
product_3 = "USB-C Adapter"

#Prices
price_1 = "25"
price_2 = "$50"
price_3 = "10"

#Avaliability
in_stock_1 = True
in_stock_2 = False
in_stock_3 = True

cart_summary = "Your Cart items:\n"
cart_summary += "-" + product_1 + ": " + price_1 + (" (In sock)" if in_stock_1 else "(Out of Stock)") + "\n"
cart_summary += "-" + product_2 + ": " + price_1 + (" (In sock)" if in_stock_2 else "(Out of Stock)") + "\n"
cart_summary += "-" + product_3 + ": " + price_1 + (" (In sock)" if in_stock_3 else "(Out of Stock)") + "\n"

print(cart_summary)