# NewLang

![image](https://github.com/RicardoMourao-py/NewLang/assets/72896483/9c5dd24b-8b3d-4977-a699-027ad3eac8ea)

Linguagem de programação criada para simplificar tarefas do cotidiano e com um vocabulário agradável para o usuário.

## Executando as ferramentas Flex e Bison para realizar as etapas de Análise Léxica e Sintática. 

Com a execução abaixo é possível efetuar a compilação da linguagem e realizar testes de verificação:

```
sudo apt install flex
sudo apt install bison
git clone https://github.com/RicardoMourao-py/NewLang.git
cd NewLang/
./main.sh
```

## EBNF
```
PROGRAM = { STATEMENT };

BLOCK = { "{", "\n", STATEMENT, "}" };

STATEMENT = ( λ | DECLARATION | FOREACH | WHILE |ASSIGNMENT | IF_STATEMENT | OUTPUT_STATEMENT | COMMENT ), "\n";

DECLARATION = "declare", TYPE, ":", IDENTIFIER, { "recebe", BEXPRESSION };

TYPE = "inteiro" | "decimal" | "texto" | "logico";

FOREACH = "durante", ASSIGNMENT, BLOCK;

WHILE = "enquanto", BEXPRESSION, BLOCK;

ASSIGNMENT = IDENTIFIER, "recebe", REXPRESSION;

IF_STATEMENT= "se", BEXPRESSION, "entao", {"senao", BLOCK};

BEXPRESSION = BTERM, {("ou"), BTERM};

BTERM = REXPRESSION, {("e"), REXPRESSION};

REXPRESSION = EXPRESSION, {("==" | ">" | "<"), EXPRESSION};

EXPRESSION = TERM, {("+" | "-" ), TERM};

TERM = FACTOR, {("*" | "/"), FACTOR };

FACTOR = (("+" | "-" | "!"), FACTOR | DIGIT | STRING_LITERAL | BOOL_LITERAL | "(", EXPRESSION, ")" | IDENTIFIER | INPUT_STATEMENT);

INPUT_STATEMENT =  "leia", "(", ")";

OUTPUT_STATEMENT = "mostre", "(", BEXPRESSION, ")";

COMMENT = "//", { Any valid character }, "\n";

LITERAL = INT_LITERAL | STRING_LITERAL | BOOL_LITERAL;

INT_LITERAL = DIGIT, { DIGIT };

STRING_LITERAL = "'", { Any valid character }, "'";

BOOL_LITERAL = "1" | "0";

IDENTIFIER = LETTER, { LETTER | DIGIT | "_" };

LETTER = ( "a" | ... | "z" | "A" | ... | "Z" );

DIGIT = ( "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" );

Any valid character = Qualquer caractere válido, incluindo letras, números e caracteres especiais.


```

## Exemplo 1

```
declare inteiro: idade
idade recebe 25
declare texto: nome recebe "Alice"
```

## Exemplo 2

```
se idade > 18 entao {
    declare texto: alerta recebe "Você é maior de idade."
    mostre(alerta)
} senao {
    declare texto: alerta recebe "Você é menor de idade."
    mostre(alerta)
}
```

## Exemplo 3

```
declare inteiro: contador
contador recebe 1

enquanto contador < 5 {
    mostre(contador)
    contador recebe contador + 1
}
```

## Exemplo 4

```
declare inteiro: x_1
x_1 recebe leia()
```

## Exemplo 5

```
// Isso é um comentário simples
declare decimal: pi recebe 3.14

/*
Este é um comentário
de várias linhas.
*/

```

## Exemplo 6

```
declare inteiro: a recebe 5
declare inteiro: b recebe 3
declare inteiro: resultado recebe a + b * 2

```
