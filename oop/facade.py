class Facade:
    def __init__(self, input):
        self.input = input
        self.run()
    
    def run(self):
        result = self.validate(self.input)
        output = self.processor(result)
        self.outputSystem(output)

    # validuje jestli user zadal správný command
    def validate(self, input):
        if input == "start":
            return 1
        elif input == "shutdown":
            return 2
        elif input == "hibernate":
            return 3
        else:
            return "Invalid input"

    # zpracuje command a vrátí hodnotu
    def processor(self, result):
        if result == 1:
            return "System starting..."
        elif result == 2:
            return "System shutting down..."
        elif result == 3:
            return "System hibernating..."
        else:
            return "Invalid input"

    # vypíše hodnotu z processor classy
    def outputSystem(self, output):
        print(output)

print(50*"-")
print("Simulation of a computer system")
print("Commands: start, shutdown, hibernate")
print(50*"-")

user_input = Facade(input("Enter input: "))