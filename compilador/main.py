import sys
from prepro import *
from tokenizer import *
from parser import Parser
from node import *

if __name__ == "__main__":
    archive = sys.argv[1]
    # Ler o código-fonte de um arquivo .go
    with open(archive, "r") as file:
        source_code = file.read()
    
    # Remove comentários usando a classe PrePro
    clean_code = PrePro.filter(source_code)
    
    # Inicializa o Tokenizador com o código limpo
    tokenizer = Tokenizer(clean_code)
    parser = Parser(tokenizer)
    
    # Obtem a AST
    ast = parser.run(clean_code)
    
    # Executa a AST e obtem o resultado final
    symbol_table = SymbolTable()
    result = ast.evaluate(symbol_table)