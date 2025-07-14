class Patient(): #Make a class of patient
    def __init__(self, name, age, height, weight):

        self.name=name 
        self.age=age
        self.height=height
        self.weight=weight
    def calculate_bmi(self): #Make a function to calculate the bmi
        bmi = self.weight / (self.height ** 2)
        if bmi < 18.5:
            return "underweight"
        elif 18.5 <= bmi <= 25:
            return "healthy"
        else:
            return "overweight"
#Show an example       
patient1 = Patient("Chen", 19, 1.8,65)
print(f"{patient1.name}'s BMI status: {patient1.calculate_bmi()}")

    