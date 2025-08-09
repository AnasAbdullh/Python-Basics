class Cat:
    def __init__(self, name, color, type, age):
        self.name = name
        self.color = color
        self.type = type
        self.age = age

    def walk(self, steps_per_second):
        print(f"{self.name} يمشي {steps_per_second} خطوة/الثانية.")

    def run(self, steps_per_second):
        print(f"{self.name} يجري {steps_per_second} خطوة/الثانية.")

    def print_info(self):
        print("الاسم:", self.name)
        print("اللون:", self.color)
        print("النوع:", self.type)
        print("العمر:", self.age, "شهر")
        print("-" * 20)


cat1 = Cat("حنفي", "مشمشي", "أنثى", 6)
cat2 = Cat("عاتز", "أسود", "ذكر", 9)
cat3 = Cat("سمسمة", "أبيض", "أنثى", 3)

cat1.print_info()
cat2.print_info()
cat3.print_info()

cat1.walk(3)
cat1.run(20)

cat2.walk(1)
cat2.run(15)

cat3.walk(2)
cat3.run(5)