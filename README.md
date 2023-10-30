# NewLang
Linguagem de programação criada para simplificar tarefas do cotidiano e com um vocabulário agradável para o usuário.

## EBNF
```
PROGRAM = { STATEMENT };

BLOCK = { "{", STATEMENT, "}" };

STATEMENT = ( λ | DECLARATION | ASSIGNMENT | IF_STATEMENT | INPUT_STATEMENT | OUTPUT_STATEMENT | COMMENT ), "\n";

DECLARATION = "declare", IDENTIFIER, ":", TYPE, [ "inicializado_com", EXPRESSION ];

TYPE = "inteiro" | "decimal" | "texto" | "logico";

ASSIGNMENT = IDENTIFIER, "recebe", EXPRESSION;

IF_STATEMENT = "se", CONDITION, "entao", BLOCK, [ "senao", BLOCK ];

CONDITION = EXPRESSION, ( "=" | "!=" | ">" | "<" | ">=" | "<=" ), EXPRESSION;

INPUT_STATEMENT = "leia", STRING_LITERAL, "em", IDENTIFIER;

OUTPUT_STATEMENT = "mostre", "(", EXPRESSION, ")";

COMMENT = "//", { Any valid character }, "\n";

EXPRESSION = TERM, { ( "+" | "-" | "ou" ), TERM };

TERM = FACTOR, { ( "*" | "/" | "e" ), FACTOR };

FACTOR = ( "+" | "-" ), FACTOR | LITERAL | IDENTIFIER | "(" , EXPRESSION, ")";

LITERAL = INT_LITERAL | FLOAT_LITERAL | STRING_LITERAL | BOOL_LITERAL;

INT_LITERAL = DIGIT, { DIGIT };

FLOAT_LITERAL = DIGIT, { DIGIT }, ".", DIGIT, { DIGIT };

STRING_LITERAL = "'", { Any valid character }, "'";

BOOL_LITERAL = "verdadeiro" | "falso";

IDENTIFIER = LETTER, { LETTER | DIGIT | "_" };

LETTER = ( "a" | ... | "z" | "A" | ... | "Z" );

DIGIT = ( "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" );

Any valid character = Qualquer caractere válido, incluindo letras, números e caracteres especiais.


```

## Exemplo 1

```
declare inteiro idade
idade recebe 25
declare texto nome inicializado_com "Alice"
```

## Exemplo 2

```
se idade > 18 entao {
    mostre("Você é maior de idade.")
} senao {
    mostre("Você é menor de idade.")
}
```

## Exemplo 3

```
declare inteiro contador
contador recebe 1

enquanto contador <= 5 {
    mostre("Contador:", contador)
    contador recebe contador + 1
}
```

## Exemplo 4

```
leia("Digite seu nome: " em nome)
mostre("Olá, ", nome, "!")
```

## Exemplo 5

```
// Isso é um comentário simples
declare decimal pi recebe 3.14

/*
Este é um comentário
de várias linhas.
*/

```

## Exemplo 6

```
declare inteiro a recebe 5
declare inteiro b recebe 3
declare inteiro resultado recebe a + b * 2

```
