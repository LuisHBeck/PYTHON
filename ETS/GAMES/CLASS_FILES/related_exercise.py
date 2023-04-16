class Car():
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__engine = None
        self.__automaker = None

    @property
    def name(self):
        return self.__name

    @property
    def engine(self):
        return self.__engine

    @engine.setter
    def engine(self, value: str):
        self.__engine = value

    @property
    def automaker(self):
        return self.__automaker
    
    @automaker.setter
    def automaker(self, value: str):
        self.__automaker = value


class Engine():
    def __init__(self, model: str) -> None:
        self.model = model


class Automakers():
    def __init__(self, name: str) -> None:
        self.name = name
        
        
if __name__ == "__main__":
    cayenne = Car("Cayenne")
    engine = Engine("BI turbo")
    automaker = Automakers("Porsche")

    cayenne.engine = engine
    cayenne.automaker = automaker

    print(cayenne.name)
    print(cayenne.engine.model)
    print(cayenne.automaker.name)
    print()
    
    xc40 = Car("XC40")
    engine = Engine("Eletric")
    automaker = Automakers("Volvo")

    xc40.engine = engine
    xc40.automaker = automaker

    print(xc40.name)
    print(xc40.engine.model)
    print(xc40.automaker.name)
