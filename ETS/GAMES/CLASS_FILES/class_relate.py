class Writer():
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__tool = None

    @property
    def tool(self):
        return self.__tool
    
    @tool.setter
    def tool(self, new_value):
        self.__tool = new_value


class Writer_tool():
    def __init__(self, name: str) -> None:
        self.__name = name 

    def write(self):
        return f'{self.__name} is writing'



if __name__ == "__main__":
    writer = Writer("Luís Beck")
    pen = Writer_tool("Pen")
    machine_writer = Writer_tool('Machine writer')

    writer.tool = pen
    
    print(pen.write())
    print(machine_writer.write())
    print()
    print(writer.tool.write())
