class Pen():
    def __init__(self, ink_color: str, cover_color: str, price: float) -> None:
        self.__ink_color = ink_color
        self.__cover_color = cover_color
        self.__price = price

    @property
    def ink_color(self):
        return self.__ink_color
    
    @ink_color.setter
    def ink_color(self, new_color):
        self.__ink_color = new_color
    
    @property
    def cover_color(self):
        return self.__cover_color
    
    @cover_color.setter
    def cover_color(self, new_collor):
        self.__cover_color = new_collor

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, new_value):
        self.__price = new_value
       
      
      
if __name__ == "__main__":
    pen1 = Pen('Blue', 'Black', 15)
    print(pen1.ink_color)
    print(pen1.cover_color)

    pen1.price = 32
    pen1.ink_color = 'Black' #setter
    pen1.cover_color = 'Blue'
    print(pen1.__dict__)
