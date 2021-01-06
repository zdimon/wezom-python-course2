# class Calculator:
#     def __init__(self):
#         self.operands = []
#         self.operations = self.getOperations()
#         self.operation = self.plus
#         self.result = None
#
#     def start(self):
#         operand = input(self.getTip())
#         while operand != 'q':
#             if self.is_digit(operand):
#                 self.operands.append(float(operand))
#             else:
#                 print(f'"{operand}" - не является числом!')
#             operand = input(self.getTip())
#
#         self.printOperations()
#         operation = input('Выберите операцию из списка (введите номер): ')
#         while self.operations.get(operation) == None:
#             print('Такой операции нет.')
#             self.printOperations()
#             operation = input('Выберите операцию из списка (введите номер): ')
#         self.operation = self.operations.get(operation).get('method')
#
#         self.calc()
#
#         if self.result != None:
#             print(f'Итого: {self.result}')
#
#     def is_digit(self, string):
#         if string.isdigit():
#             return True
#         else:
#             try:
#                 float(string)
#                 return True
#             except ValueError:
#                 return False
#
#     def calc(self):
#         if (len(self.operands) > 0):
#             self.result = self.operands.pop(0)
#             for operand in self.operands:
#                 self.result = self.operation(operand)
#
#     def printOperations(self):
#         for index, operation in self.operations.items():
#             print(f'{index}. {operation.get("name")}')
#
#     def getTip(self):
#         tip = f'Введите {len(self.operands) + 1}-e число '
#         if (len(self.operands) > 1):
#             tip += '("q" для выбора операции) '
#         return tip
#
#     def getOperations(self):
#         return {
#             '1': {
#                 'name': '+',
#                 'method': self.plus
#             },
#             '2': {
#                 'name': '-',
#                 'method': self.minus
#             },
#             '3': {
#                 'name': '*',
#                 'method': self.multiply
#             },
#             '4': {
#                 'name': '/',
#                 'method': self.divide
#             },
#         }
#
#     def plus(self, b):
#         return self.result + b
#
#     def minus(self, b):
#         return self.result - b
#
#     def multiply(self, b):
#         return self.result * b
#
#     def divide(self, b):
#         try:
#             return self.result / b
#         except ZeroDivisionError:
#             print('Division by zero error')


class Calculator:
    def __init__(self):
        self.args = []
        self.result = None
        self.break_input = 'q'

    @property
    def operations(self):
        return {
            '1': 'plus',
            '2': 'minus',
            '3': 'multiply',
            '4': 'divide'
        }

    def is_number(self, num):
        if num.isdigit():
            return True
        else:
            try:
                float(num)
                return True
            except ValueError:
                return False

    def start(self):
        num = input(self.tip())
        while num != self.break_input:
            if self.is_number(num):
                self.args.append(float(num))
            else:
                print(f'"{num}" должно быть числом')
            num = input(self.tip())

        operation = input(self.print_operations())

        while self.operations.get(operation) is None:
            print('Такой операции нет.')
            operation = input(self.print_operations())

        print(operation)
        self.calc(operation)

    def calc(self, operation):
        if len(self.args) > 0:
            self.result = self.args.pop(0)
            for arg in self.args:
                # execute method by it's name
                self.result = getattr(self, self.operations.get(operation))(arg)
        if self.result is not None:
            print(f'Итого: {self.result}')

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
            print('Division by zero')

    def tip(self):
        tip = f'Введите {len(self.args) + 1}-e число '
        if len(self.args) > 1:
            tip += '("%s" для выбора операции) ' % self.break_input
        return tip

    def print_operations(self):
        print("Выберите номер операции")
        for operation in self.operations:
            print(f'{operation}: {self.operations.get(operation)}')
