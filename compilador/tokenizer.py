from token import Token

class Tokenizer:
    def __init__(self, source: str):
        self.source = source      # codigo-fonte que será tokenizado
        self.position = 0         # posicao atual que o Tokenizador está separando 
        self.next = None          # o último token separado        

    def selectNext(self):
        '''
            Lê o próximo token e atualiza o atributo next
        '''

        # Tira espaços em branco
        while self.position < len(self.source) and (self.source[self.position]==" " or self.source[self.position]=='\t'):
            self.position += 1
        
        if self.position >= len(self.source):
            self.next = Token('EOF', '"')
            return

        char_atual = self.source[self.position]
        num = ''
        if char_atual.isalpha():
            word=''
            while self.position < len(self.source) and (self.source[self.position].isalpha() or self.source[self.position].isdigit() or self.source[self.position]=="_"):
                word += self.source[self.position]
                self.position += 1

            if word == 'mostre':
                self.next = Token('PRINT', word)
            elif word == 'durante':
                self.next = Token('FOR', word)
            elif word == 'enquanto':
                self.next = Token('WHILE', word)
            elif word == 'se':
                self.next = Token('IF', word)
            elif word == 'senao':
                self.next = Token('ELSE', word)
            elif word == 'leia':
                self.next = Token('INPUT', word)
            elif word == 'declare':
                self.next = Token('VARIABLE', word)
            elif word == 'inteiro' or word == 'texto':
                self.next = Token('TYPE', word)
            elif word == 'recebe':
                self.next = Token("ASSIGN", "=")
            elif word == 'e':
                self.next = Token("AND", "&&")
            elif word == 'ou':
                self.next = Token("OR", "||")
            elif word == 'entao':
                self.next = Token("ENTAO", "entao")
            else: 
                self.next = Token("IDENTIFIER", word)

        
        elif char_atual.isdigit():
            while self.position < len(self.source) and self.source[self.position].isdigit():
                num += char_atual
                self.position += 1
            self.next = Token('INT', int(num))
        
        elif char_atual == '"':
            self.position += 1
            num = ""
            for char in self.source[self.position:]:
                if char == '"':
                    self.position += 1
                    break
                num += char
                self.position += 1
            if self.source[self.position-1] != '"':
                raise ValueError('Erro: fechamento de aspas necessario')
            self.next = Token("STRING", num)

        elif char_atual == '+':
            self.next = Token('PLUS', '+')
            self.position += 1
        elif char_atual == '-':
            self.next = Token('MINUS', '-')
            self.position += 1
        elif char_atual == '/':
            self.next = Token('DIV', '/')
            self.position += 1
        elif char_atual == '*':
            self.next = Token('MULT', '*')
            self.position += 1
        elif char_atual == '(':
            self.next = Token('LPAREN', '(')
            self.position += 1
        elif char_atual == ')':
            self.next = Token('RPAREN', ')')
            self.position += 1
        elif char_atual == '\n':
            self.next = Token("ENTER", '\n')
            self.position+=1
        elif char_atual == '=':
            self.next = Token("ASSIGNOP", "==")
            self.position+=2
        elif char_atual == '!':
            self.next = Token("NOT", "!")
            self.position+=1
        elif char_atual == '>':
            self.next = Token("GREATER", ">")
            self.position+=1
        elif char_atual == '<':
            self.next = Token("LESS", "<")
            self.position+=1
        elif char_atual == ';':
            self.next = Token("END", ";")
            self.position+=1
        elif char_atual == '{':
            self.next = Token("LBLOCK", "{")
            self.position+=1
        elif char_atual == '}':
            self.next = Token("RBLOCK", "}")
            self.position+=1
        elif char_atual == '.':
            self.next = Token("CONCAT", ".")
            self.position+=1
        elif char_atual == ':':
            self.next = Token("DOISPONTOS", ":")
            self.position+=1
        else:
            raise ValueError(f"Token inválido: {char_atual}")