class Mobile:
    fp= "Yes"
    def __init__(self):
        self.model = "Samsung Z fold"

    def  display(self):
        print("Model Name:",self.model)

    @classmethod
    def check(cls):
        print("FingerPrint Avalable:",cls.fp)

samsung = Mobile()
samsung.display()
Mobile.check()  # class method
print()
samsung.display()
Mobile.fp="Not Avalable"
Mobile.check()