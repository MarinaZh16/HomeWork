class Product():
    def __init__(self, price, category, name, unit):
        self.price=price
        self.category=category
        self.name=name
        self.unit=unit
    def is_eatable(self):
        if self.category=="household chemicals":
            return False
        return True
    
    def price_total(self, quantity):
        return quantity*self.price

    
class Basket():
    def __init__(self, buy_list):
        self.buy_list=buy_list
    
    def total(self):
        total_sum=0
        for p, q in self.buy_list:
            total_sum+=p.price_total(q)
        return ('Общая сумма покупки = %s грн.' %(total_sum))
    
        
    def totally_eatable(self):
        for i in self.buy_list:
            if i[0].is_eatable()==False:
                return ('Не все продукты съедобны!')
        return ('Все продукты съедобны!')
                
        

bread=Product(price=10, category='food', name='bread', unit='шт.')
shampoo=Product(price=150, category='household chemicals', name='Nivea', unit='шт.')
cheese=Product(price=50, category='food', name='Maasdamer', unit='кг.')
bananas=Product(price=25, category='food', name='banana', unit='кг')
milk=Product(price=28.90, category='food', name='Ферми', unit='л')
wine=Product(price=150, category='alcohol', name='VinishKo', unit='бут.')
b=Basket([[bananas, 1.5], [bread, 3], [cheese, 0.3], [shampoo, 2], [milk, 1], [wine, 3]])
print(b.total())
print(b.totally_eatable())


