class Facade:
    def __init__(self, input):
        self.input = input
        self.validate = Validate()
        self.processor = Processor()
        self.display = OutputSystem()
        self.run()
    
    def run(self):
        result = self.validate.validate(self.input)
        output = self.processor.process(result)
        self.display.output(output)

class Validate:
    def validate(self, input):
        if input == "start":
            return 1
        elif input == "shutdown":
            return 2
        elif input == "hibernate":
            return 3
        else:
            return "Invalid input"

class Processor:
    def process(self, result):
        if result == 1:
            return "System starting..."
        elif result == 2:
            return "System shutting down..."
        elif result == 3:
            return "System hibernating..."
        else:
            return "Invalid input"

class OutputSystem:
    def output(self, output):
        print(output)

print(50*"-")
print("Simulation of a computer system")
print("Commands: start, shutdown, hibernate")
print(50*"-")

user_input = Facade(input("Enter input: "))