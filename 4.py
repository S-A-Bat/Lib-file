# Базовый класс
class BaseClass:
    def __init__(self):
        print("Конструктор базового класса")

    def base_method(self):
        print("Метод базового класса")

class DerivedClass(BaseClass):
    def __init__(self):
        super().__init__()
        print("Конструктор производного класса")

    def derived_method(self):
        print(f"Метод производного класса")

# Создание экземпляра производного класса
obj = DerivedClass()

# Вызов методов обоих классов
obj.base_method()
obj.derived_method()

