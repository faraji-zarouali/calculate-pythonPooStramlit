class Calcul:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calcul_somme(self):
        return round((float(self.num1) + float(self.num2)), 2)

    def calcul_soustraction(self):
        return round(float(self.num1) - float(self.num2), 2)

    def calcul_multiplication(self):
        return round(float(self.num1) * float(self.num2), 2)

    def calcul_division(self):
        try:
            division = float(self.num1) / float(self.num2)
        except ZeroDivisionError:
            return 'the first value cannot divide by zero'
        return round(float(self.num1) / float(self.num2), 2)