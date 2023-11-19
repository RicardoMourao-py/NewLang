# NewLang
Linguagem de programação criada para simplificar tarefas do cotidiano e com um vocabulário agradável para o usuário.

## EBNF
```
PROGRAM = { STATEMENT };

BLOCK = { "{", "\n", STATEMENT, "}" };

STATEMENT = ( λ | DECLARATION | FOREACH | WHILE |ASSIGNMENT | IF_STATEMENT | OUTPUT_STATEMENT | COMMENT ), "\n";

DECLARATION = "declare", TYPE, ":", IDENTIFIER, { "recebe", BEXPRESSION };

TYPE = "inteiro" | "decimal" | "texto" | "logico";

FOREACH = "durante", ASSIGNMENT, "ate", ASSIGNMENT, BLOCK;

WHILE = "enquanto", BEXPRESSION, BLOCK;

ASSIGNMENT = IDENTIFIER, "recebe", REXPRESSION;

IF_STATEMENT= "se", BEXPRESSION, "entao", {"senao", BLOCK};

BEXPRESSION = BTERM, {("ou"), BTERM};

BTERM = REXPRESSION, {("e"), REXPRESSION};

REXPRESSION = EXPRESSION, {("==" | ">" | "<"), EXPRESSION};

EXPRESSION = TERM, {("+" | "-" ), TERM};

TERM = FACTOR, {("*" | "/"), FACTOR };

FACTOR = (("+" | "-" | "!"), FACTOR | LITERAL | "(", EXPRESSION, ")" | IDENTIFIER | INPUT_STATEMENT);

INPUT_STATEMENT = "leia", STRING_LITERAL, "em", IDENTIFIER;

OUTPUT_STATEMENT = "mostre", "(", BEXPRESSION, ")";

COMMENT = "//", { Any valid character }, "\n";

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
declare inteiro: idade
idade recebe 25
declare texto: nome recebe "Alice"
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
