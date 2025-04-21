from abc import abstractmethod, ABC

class Animal(ABC):
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    @abstractmethod
    def make_sound(self):
        pass

    def feed(self):
        print(f"{self.name} is being fed!")

class cow_class(Animal):
    def make_sound(self):
        print("cow sound")
    def milk(self):
        print("Cow is producing Milk")

class chicken_class(Animal):
    def make_sound(self):
        print("chicken sound")
    def lay_egg(self):
        print("Chikcen is producing eggs")

class sheep_class(Animal):
    def make_sound(self):
        print("sheep sound")
    def shear(self):
        print("sheep is producing wool")

class farm:
    def __init__(self,farm_name):
        self.cow_list = []
        self.chicken_list = []
        self.sheep_list = []
        self.barn_list = []
        self.coop_list = []
        self.farm_name=farm_name
        print(f"Welcome to The {self.farm_name} Farm! ")

    def show_population(self):
        print("Farm Population:")
        print(f"- Cow: {len(self.cow_list)}")
        print(f"- Chicken: {len(self.chicken_list)}")
        print(f"- Sheep: {len(self.sheep_list)}")

    def list_structures(self):
        print("Structures:")
        for barn in self.barn_list:
            print(f"{barn} (Barn)")
        for coop in self.coop_list:
            print(f"{coop} (Coop)")

    def add(self, name, type):
        if type == "barn":
            self.barn_list.append(name)
        elif type == "coop":
            self.coop_list.append(name)
        elif type == "cow":
            self.cow_list.append(name)
        elif type == "chicken":
            self.chicken_list.append(name)
        elif type == "sheep":
            self.sheep_list.append(name)
        else:
            print("no type like this")

    def daily_routine(self):
        print(" ----- Morning Routine ------")
        products = []
        for cow in self.cow_list:
            print(f"{cow} the cow is being fed!")
            products.append(f"{cow}'s Milk")
        for chicken in self.chicken_list:
            print(f"{chicken} the chicken is being fed!")
            products.append(f"{chicken}'s egg")
        for sheep in self.sheep_list:
            print(f"{sheep} the sheep is being fed!")
            products.append(f"{sheep}'s Wool")
        print("Collected products: " + ", ".join(products))
my_farm = farm("belval")
my_farm.add("cow1", "cow")
my_farm.add("cow2", "cow")
my_farm.add("chicken1", "chicken")
my_farm.add("chicken2", "chicken")
my_farm.add("sheep1", "sheep")
my_farm.add("sheep2", "sheep")
my_farm.add("Red Barn", "barn")
my_farm.add("Hen Palace", "coop")

my_farm.show_population()
my_farm.list_structures()
my_farm.daily_routine()
