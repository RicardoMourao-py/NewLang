from tokenizer import *
from node import *
    
class Parser:
    def __init__(self, tokenizer: Tokenizer):
        self.tokenizer = tokenizer  # Objeto da classe que lê o código fonte e alimenta o analisador
    
    @staticmethod
    def parseAssign():
        if Parser.tokenizer.next.type == 'IDENTIFIER':
            identifier = VarOp(Parser.tokenizer.next.value,[])
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type != 'ASSIGN':
                raise ValueError('Erro: Caractere "=" faltando')
            Parser.tokenizer.selectNext()
            expression = Parser.boolExpression()
            return EqualOp("=",[identifier,expression])

    @staticmethod
    def parseStatement():
        if Parser.tokenizer.next.type == 'IDENTIFIER':
            identifier = VarOp(Parser.tokenizer.next.value,[])
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type != 'ASSIGN':
                raise ValueError('Erro: Caractere "=" faltando')
            Parser.tokenizer.selectNext()
            expression = Parser.boolExpression()
            statment = EqualOp("=",[identifier,expression])
        elif Parser.tokenizer.next.type == 'PRINT':
            Parser.tokenizer.selectNext()  
            if Parser.tokenizer.next.type == 'LPAREN':
                Parser.tokenizer.selectNext()  
                expression = Parser.boolExpression()
                if Parser.tokenizer.next.type != 'RPAREN':
                    raise ValueError("Erro de sintaxe: Parênteses desbalanceados")
                Parser.tokenizer.selectNext()  
            statment = PrintOp("Println", [expression])
        elif Parser.tokenizer.next.type == 'IF':
            Parser.tokenizer.selectNext() 
            condicao = Parser.boolExpression()
            if Parser.tokenizer.next.type != 'ENTAO':
                raise ValueError(f"erro {Parser.tokenizer.next.type}")
            Parser.tokenizer.selectNext()  
            block = Parser.parseBlock()
            if Parser.tokenizer.next.type == 'ELSE':
                Parser.tokenizer.selectNext()  
                statment = IfOp("else", [condicao, block, Parser.parseBlock()])
            else:
                Parser.tokenizer.selectNext()  
                statment = IfOp("if", [condicao, block])
        elif Parser.tokenizer.next.type == 'FOR':
            Parser.tokenizer.selectNext()
            assign = Parser.parseAssign()
            if Parser.tokenizer.next.type == 'END':
                Parser.tokenizer.selectNext()
                expression = Parser.boolExpression()
                if Parser.tokenizer.next.type == 'END':
                    Parser.tokenizer.selectNext()
                    statment = ForOp("for", [assign, expression, Parser.parseAssign(), Parser.parseBlock()])
                else:
                    raise ValueError(f"erro {Parser.tokenizer.next.type}")
            else:
                raise ValueError(f"erro {Parser.tokenizer.next.type}")
            
        elif Parser.tokenizer.next.type=='VARIABLE':
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type !="TYPE":
                raise ValueError(f"Erro: tipo {Parser.tokenizer.next.type} diferente do esperado")
            type_value=Parser.tokenizer.next.value
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type !="DOISPONTOS":
                raise ValueError(f"Erro: tipo {Parser.tokenizer.next.type} diferente do esperado")
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type!="IDENTIFIER":
                raise ValueError(f"Erro: tipo {Parser.tokenizer.next.type} não é um IDENTIFIER")
            identifier=VarOp(Parser.tokenizer.next.value,[])
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type=="ASSIGN":
                Parser.tokenizer.selectNext()
                statment= VarDeclarateOp(type_value,[identifier,Parser.boolExpression()])
            else:
                statment= VarDeclarateOp(type_value,[identifier])   
                
        elif Parser.tokenizer.next.type in ("ENTER", "EOF"):
            Parser.tokenizer.selectNext()
            statment = NoOp()
        
        return statment
    
    @staticmethod
    def parseFactor():
        if Parser.tokenizer.next.type == 'INT':
            result = IntVal(Parser.tokenizer.next.value)
            Parser.tokenizer.selectNext()
        elif Parser.tokenizer.next.type == "STRING": 
            result = StrVal(Parser.tokenizer.next.value)
            Parser.tokenizer.selectNext()
        elif Parser.tokenizer.next.type in ('PLUS', 'MINUS' , 'NOT'):
            operator = Parser.tokenizer.next
            Parser.tokenizer.selectNext()
            factor = Parser.parseFactor()
            result = UnOp(operator.value, factor)
        elif Parser.tokenizer.next.type == 'LPAREN':
            Parser.tokenizer.selectNext()
            result = Parser.boolExpression()
            if Parser.tokenizer.next.type == 'RPAREN':
                Parser.tokenizer.selectNext()
            else:
                raise ValueError("Erro de sintaxe: Parênteses desbalanceados")
        elif Parser.tokenizer.next.type == 'INPUT':
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == 'LPAREN':
                Parser.tokenizer.selectNext()
                if Parser.tokenizer.next.type == 'RPAREN':
                    Parser.tokenizer.selectNext()
                    return InputOp("Scanln",[])
                else:
                    raise ValueError("Erro de sintaxe: Parênteses desbalanceados")
            
        elif Parser.tokenizer.next.type=='IDENTIFIER':
            result=VarOp(Parser.tokenizer.next.value,[])
            Parser.tokenizer.selectNext()
            return result
        else:
            raise ValueError(f"Erro de sintaxe: Token inesperado {Parser.tokenizer.next.type}")

        return result

        
    @staticmethod
    def parseTerm():
        '''
            Consome os tokens do Tokenizer e analisa se a sintaxe está aderente 
            a gramatica proposta. Retorna o resultado da expressão analisada.
        '''
        result = Parser.parseFactor()

        while Parser.tokenizer.next.type in ('DIV', 'MULT'):
            operator = Parser.tokenizer.next
            Parser.tokenizer.selectNext()
            
            term = Parser.parseFactor()
            
            if operator.type == 'DIV':
                result = BinOp('/', result, term)
            elif operator.type == 'MULT':
                result = BinOp('*', result, term)
            else:
                raise ValueError(f"Erro de sintaxe: Operador inesperado {operator.type}")
        
        return result
    
    @staticmethod
    def parseExpression():
        '''
        Consome os tokens do Tokenizer e analisa se a sintaxe está aderente 
        a gramatica proposta. Retorna o resultado da expressão analisada.
        '''
        result = Parser.parseTerm()

        while Parser.tokenizer.next.type in ('PLUS', 'MINUS', 'CONCAT'):
            operator = Parser.tokenizer.next
            Parser.tokenizer.selectNext()
            
            term = Parser.parseTerm()
            
            if operator.type == 'PLUS':
                result = BinOp('+', result, term)
            elif operator.type == 'MINUS':
                result = BinOp('-', result, term)
            elif operator.type == 'CONCAT':
                result = BinOp('.', result, term)
            else:
                raise ValueError(f"Erro de sintaxe: Operador inesperado {operator.type}")
        
        return result

    @staticmethod
    def relExpression():
        result = Parser.parseExpression()

        while Parser.tokenizer.next.type in ('ASSIGNOP', 'GREATER','LESS'):
            operator = Parser.tokenizer.next.type
            Parser.tokenizer.selectNext()
            expression = Parser.parseExpression()
            if operator == 'ASSIGNOP':
                result = BinOp('=', result, expression)
            elif operator=='GREATER':
                result = BinOp('>', result, expression)
            elif operator=='LESS':
                result=BinOp('<', result, expression)
        return result
    
    @staticmethod
    def boolTerm():
        result=Parser.relExpression()
        while Parser.tokenizer.next.type in ('AND'):
            operator=Parser.tokenizer.next.type
            Parser.tokenizer.selectNext()
            expression=Parser.relExpression()
            if operator =='AND':
                result=BinOp('&', result, expression)
        return result

    @staticmethod
    def boolExpression():
        result=Parser.boolTerm()
        while Parser.tokenizer.next.type in ('OR'):
            operator=Parser.tokenizer.next.type
            Parser.tokenizer.selectNext()
            bool_term=Parser.boolTerm()
            if operator =='OR':
                result=BinOp('|', result, bool_term)
        return result

    @staticmethod
    def parseBlock():
        statements = []
        if Parser.tokenizer.next.type == 'LBLOCK':
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == 'ENTER':
                while Parser.tokenizer.next.type != 'RBLOCK':
                    statement = Parser.parseStatement()
                    statements.append(statement)
                Parser.tokenizer.selectNext()
                return BlockOp(None, statements)
            else:
                raise ValueError(f"Erro de sintaxe: esperado 'ENTER', obtido {Parser.tokenizer.next.type}")
        else:
            raise ValueError(f"Erro de sintaxe: esperado 'LBLOCK', obtido {Parser.tokenizer.next.type}")

    @staticmethod
    def parseProgram():
        parse_list = []
        while True:
            if Parser.tokenizer.next.type!='EOF':
                parse_list.append(Parser.parseStatement())
            else:
                break
        
        return BlockOp("Block", parse_list)
    
    @staticmethod
    def run(code: str):
        tokenizer = Tokenizer(code)
        Parser.tokenizer = tokenizer
        Parser.tokenizer.selectNext()
        result = Parser.parseProgram()

        if Parser.tokenizer.next.type == 'EOF':
            return result
        else:
            raise ValueError("Erro de sintaxe: Cadeia não consumida completamente")
