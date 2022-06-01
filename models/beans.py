class Bean:
    def __init__(self,name, description, date, price, on_sale, in_stock):
        self.name = name
        self.description = description
        self.date = date
        self.price =  "{:.2f}".format(price)
        self.on_sale = on_sale
        self.in_stock = in_stock