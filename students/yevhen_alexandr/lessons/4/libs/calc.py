def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False

class Calculator():
    def __init__(self):
        self.operands = []
        self.operations = self.getOperations()
        self.operation = self.plus
        self.result = None

    def start(self):
        operand = input(self.getTip())
        while operand != 'q':
            if is_digit(operand):
                self.operands.append(float(operand))
            else:
                print(f'"{operand}" - не является числом!')
            operand = input(self.getTip())
        
        self.printOperations()
        operation = input('Выберите операцию из списка (введите номер): ')
        while self.operations.get(operation) == None:
            print('Такой операции нет.')
            self.printOperations()
            operation = input('Выберите операцию из списка (введите номер): ')
        self.operation = self.operations.get(operation).get('method')

        self.calc()

        if self.result != None:
            print(f'Итого: {self.result}')

    def calc(self):
        if (len(self.operands) > 0):
            self.result = self.operands.pop(0)
            for operand in self.operands:
                self.result = self.operation(operand)
        
    def printOperations(self):
        for index, operation in self.operations.items():
            print(f'{index}. {operation.get("name")}')

    def getTip(self):
        tip = f'Введите {len(self.operands) + 1}-e число '
        if (len(self.operands) > 1):
            tip += '("q" для выбора операции) '

        return tip

    def getOperations(self):
        return {
            '1': {
                'name': '+',
                'method': self.plus
            },
            '2': {
                'name': '-',
                'method': self.minus
            },
            '3': {
                'name': '*',
                'method': self.multiply
            },
            '4': {
                'name': '/',
                'method': self.divide
            },
        }

    def plus(self, b):
        return self.result + b

    def minus(self, b):
        return self.result - b

    def multiply(self, b):
        return self.result * b

    def divide(self, b):
        try:
            return self.result / b
        except ZeroDivisionError:
            print('Division by zero error')
