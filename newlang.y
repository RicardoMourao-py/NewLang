%{
#include <stdio.h>
int yylex();
void yyerror(const char *s);
%}

%token DECLARE
%token INTEIRO
%token DECIMAL
%token TEXTO
%token DURANTE
%token NOT
%token ENQUANTO
%token LOGICO
%token RECEBE
%token SE
%token ENTAO
%token SENAO
%token LEIA
%token EM
%token MOSTRE
%token E
%token OU
%token DIFERENTE
%token IGUAL
%token MAIOR
%token MENOR
%token MAIORIGUAL
%token MENORIGUAL
%token MAIS
%token MENOS
%token VEZES
%token DIVIDIDO
%token VERDADEIRO
%token FALSO
%token ABRE_PARENTESES
%token FECHA_PARENTESES
%token ABRE_COLCHETE
%token FECHA_COLCHETE
%token DOIS_PONTOS
%token VIRGULA
%token COMENTARIO
%token QUEBRA_DE_LINHA
%token DIGIT
%token IDENTIFIER
%token STRING

%%

program: statement
        | program statement;

block: ABRE_COLCHETE QUEBRA_DE_LINHA statements FECHA_COLCHETE ;

statements: statement
          | statements statement
          ;

statement: declaration
	     | assigment
         | if_statement
         | durante
         | enquanto
         | output_statement
         | comment
         ;

declaration: DECLARE type DOIS_PONTOS IDENTIFIER RECEBE bexpression QUEBRA_DE_LINHA
           | DECLARE type DOIS_PONTOS IDENTIFIER QUEBRA_DE_LINHA
           | DECLARE type DOIS_PONTOS IDENTIFIER RECEBE bexpression
           | DECLARE type DOIS_PONTOS IDENTIFIER 
           ;

assigment: IDENTIFIER RECEBE rexpression QUEBRA_DE_LINHA
          |IDENTIFIER RECEBE rexpression 
          ;

if_statement: SE bexpression block
	        | SE bexpression block QUEBRA_DE_LINHA
            | SE bexpression block SENAO block QUEBRA_DE_LINHA
            ;

durante: DURANTE assigment block QUEBRA_DE_LINHA;

enquanto: ENQUANTO bexpression block;

output_statement: MOSTRE ABRE_PARENTESES bexpression FECHA_PARENTESES QUEBRA_DE_LINHA;

type: INTEIRO
    | DECIMAL
    | TEXTO
    | LOGICO
    ;

bexpression: bexpression OU bterm
          | bterm
          ;

bterm: bterm E rexpression
     | rexpression
     ;

rexpression: rexpression IGUAL expression
           | rexpression MAIORIGUAL expression
           | rexpression MENORIGUAL expression
           | expression 
           ;

expression: expression MAIS term
          | expression MENOS term
          | term
          ;

term: term VEZES factor
    | term DIVIDIDO factor
    | factor
    ;

factor: MAIS factor
      | MENOS factor
      | NOT factor
      | DIGIT 
      | STRING
      | bool
      | ABRE_PARENTESES expression FECHA_PARENTESES
      | IDENTIFIER 
      | LEIA ABRE_PARENTESES FECHA_PARENTESES
      ;

bool: VERDADEIRO
    | FALSO
    ;

comment: COMENTARIO STRING QUEBRA_DE_LINHA
       | COMENTARIO STRING
       ;
%%

void yyerror(const char *s) {
    extern int yylineno;
    extern char *yytext;

    /* mensagem de erro exibe o símbolo que causou erro e o número da linha */
    printf("\nErro (%s): símbolo \"%s\" (linha %d)\n", s, yytext, yylineno);
}

int main() {
    yyparse();
    return 0;
}

