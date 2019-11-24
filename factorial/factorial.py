import sys

class Factorial:

    array = []
    number = None
    
    def ask_input(self):
        try:
            user_input = round(float(input("Enter integer: ")))
            if user_input <= 0:
                sys.stdout.write("Error. Inappropriate number.")
            else:
                self.number = user_input
                return True
        except ValueError:
            sys.stdout.write("Error. String. Exiting.")

    def factorize(self):
        self.array.append(self.number)
        while self.number != 0:
            self.number -= 1
            self.array.append(self.number)
        self.array.pop()

    def getResult(self):
        result = 1
        for factor in self.array:
            result = result * factor
        sys.stdout.write(str(result))
        self.number = None
        self.array = []
        

    def runner(self):
        if self.ask_input():
            self.factorize()
            self.getResult()
        else:
            sys.exit()


if __name__ == "__main__":
    Factorial().runner()