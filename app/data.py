class Item:
    def __init__(self,id,title,filepath, price):
        self.id=id
        self.title=title
        self.filepath=filepath
        self.price=price


class Inventory:
    def items(self):

        database = {}

        arrow = Item(1,'Arrows','static/arrows.png',50)    
        bomb = Item(2,'Bombs','static/bomb.png',100)
        boomerang = Item(3,'Boomerang','static/boomerang.png',500)

        database[arrow.id] = arrow
        database[bomb.id] = bomb
        database[boomerang.id] = boomerang

        return database

    
class Currency():
    def __init__(self):
        self.userAmount = 0

    def set_rupee(self, newAmount):
        self.userAmount = newAmount

    def get_rupee(self):
        return self.userAmount   
            
        