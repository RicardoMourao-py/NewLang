from abc import ABC, abstractmethod

class Node(ABC):
    def __init__(self):
        self.value = None
        self.children = []

    @abstractmethod
    def evaluate(self, symbol_table):
        pass

class BinOp(Node):
    def __init__(self, operator, left, right):
        super().__init__()
        self.value = operator
        self.type_value = ["inteiro", "texto"]
        self.children = [left, right]

    def evaluate(self, symbol_table):
        left = self.children[0].evaluate(symbol_table)
        right = self.children[1].evaluate(symbol_table)

        left_value, left_type = left[0], left[1]
        right_value, right_type = right[0], right[1]
        
        # Operações Aritméticas
        if self.value in ['+', '-', '*', '/']:
            if left_type != self.type_value[0] or right_type != self.type_value[0]:
                raise ValueError(f"Erro: operação {self.value} não possui inteiros")
            if self.value == '+':
                return (left_value + right_value, self.type_value[0])
            elif self.value == '-':
                return (left_value - right_value, self.type_value[0])
            elif self.value == '*':
                return (left_value * right_value, self.type_value[0])
            elif self.value == '/':
                return (left_value // right_value, self.type_value[0])
        # Operações de Comparação
        elif self.value in ['>', '<', '=']:
            if left_type != right_type:
                raise ValueError("Erro: tipos diferentes na comparação")
            if left_type not in self.type_value:
                raise ValueError(f"Erro: tipo '{left_type}' não suportado na comparação")
            elif self.value=='=':
                return (int(left_value == right_value), self.type_value[0])
            elif self.value=='<':
                return (int(left_value < right_value), self.type_value[0])
            elif self.value=='>':
                return (int(left_value > right_value), self.type_value[0])
        # Operações Lógicas
        elif self.value in ['|', '&']:
            if left_type != self.type_value[0] or right_type != self.type_value[0]:
                raise ValueError(f"Erro: operação {self.value} não possui inteiros")
            if self.value=='&':
                return (left_value and right_value, self.type_value[0])
            elif self.value=='|':
                return (left_value or right_value, self.type_value[0])
        # Concatenação String
        elif self.value == '.':
            return (f'{str(left_value)}{str(right_value)}', self.type_value[1])
        else:
            raise ValueError(f"Operador desconhecido: {self.value}")

class UnOp(Node):
    def __init__(self, operator, operand):
        super().__init__()
        self.value = operator
        self.type_value = ["inteiro", "texto"]
        self.children = [operand]

    def evaluate(self, symbol_table):
        operand_value = self.children[0].evaluate(symbol_table)[0]
        
        if self.value == '+':
            return (operand_value, self.type_value[0])
        elif self.value == '-':
            return (-operand_value, self.type_value[0])
        elif self.value=='!':
            return (not operand_value, self.type_value[0])
        else:
            raise ValueError(f"Operador desconhecido: {self.value}")

class IntVal(Node):
    def __init__(self, value):
        super().__init__()
        self.value = value
        self.type_value = ["inteiro", "texto"]

    def evaluate(self, symbol_table):
        return (self.value, self.type_value[0])

class StrVal(Node):
    def __init__(self, value):
        self.value = value
        self.type_value = ["inteiro", "texto"]

    def evaluate(self, symbol_table):
        return (self.value, self.type_value[1])

class NoOp(Node):
    def evaluate(self, symbol_table):
        return None

class BlockOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def evaluate(self, symbol_table):
        for node in self.children:
            node.evaluate(symbol_table)

class PrintOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def evaluate(self, symbol_table):
        print(self.children[0].evaluate(symbol_table)[0])

class EqualOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.type_value = ["inteiro", "texto"]
        self.children = children

    def evaluate(self, symbol_table):
        result = self.children[1].evaluate(symbol_table)
        if type(self.children[1]) is InputOp and symbol_table.get(self.children[0].value)[1] == self.type_value[1]:
            raise ValueError("Erro: Scanln() deve ser usado com variáveis inteiras.")
        return symbol_table.set(self.children[0].value, result[0], result[1])
    
class VarOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def evaluate(self, symbol_table):
        return symbol_table.get(self.value)
    
class ForOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def evaluate(self, symbol_table):
        # executa inicializador
        self.children[0].evaluate(symbol_table)
        # enquanto condição é verdadeira
        while(self.children[1].evaluate(symbol_table)[0]):
            # executa bloco 
            self.children[3].evaluate(symbol_table)
            # incrementa
            self.children[2].evaluate(symbol_table)

class IfOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def evaluate(self, symbol_table):
        # se a condição é verdadeira
        if self.children[0].evaluate(symbol_table):
            # executa o bloco
            self.children[1].evaluate(symbol_table)
        else:
            # executa bloco de else
            if(len(self.children)>2):
                self.children[2].evaluate(symbol_table)

class InputOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.type_value = ["inteiro", "texto"]
        self.children = children

    def evaluate(self, symbol_table):
        return (int(input()), self.type_value[0])

class VarDeclarateOp(Node):
    def __init__(self, value, children):
        super().__init__()    
        self.value = value
        self.children = children 
    
    def evaluate(self, symbol_table):
        if len(self.children) > 1:
            symbol_table.set(self.children[0].value,  self.children[1].evaluate(symbol_table)[0],  self.children[1].evaluate(symbol_table)[1])
        else:
            symbol_table.declarate(self.children[0].value,  None,  self.value)
        
class SymbolTable:
    def __init__(self):
        self.variables = {}

    def get(self, var):
        if var in self.variables:
            return self.variables[var]
        else:
            raise NameError("Erro: variável não existe")

    def set(self, var, value, type_value=None):
        self.variables[var] = (value, type_value)

    def declarate(self, var, value, type_value=None):
        if var in self.variables:
            raise ValueError(f"Variável '{var}' já existente.")
        else:
            self.variables[var] = (value, type_value)