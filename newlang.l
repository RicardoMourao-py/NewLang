%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "newlang.tab.h"
char* yyval;
%}
%option yylineno
%option noyywrap

%%

[ \t]                   ; /* Ignora espaços em branco e tabulações */
"declare"               { yyval = strdup(yytext); return DECLARE; }
"inteiro"               { yyval = strdup(yytext); return INTEIRO; }
"decimal"               { yyval = strdup(yytext); return DECIMAL; }
"texto"                 { yyval = strdup(yytext); return TEXTO; }
"durante"               { yyval = strdup(yytext); return DURANTE; }
"ate"                   { yyval = strdup(yytext); return ATE; }
"!"                     { yyval = strdup(yytext); return NOT; }
"enquanto"              { yyval = strdup(yytext); return ENQUANTO; }
"logico"                { yyval = strdup(yytext); return LOGICO; }
"recebe"                { yyval = strdup(yytext); return RECEBE; }
"se"                    { yyval = strdup(yytext); return SE; }
"entao"                 { yyval = strdup(yytext); return ENTAO; }
"senao"                 { yyval = strdup(yytext); return SENAO; }
"leia"                  { yyval = strdup(yytext); return LEIA; }
"em"                    { yyval = strdup(yytext); return EM; }
"mostre"                { yyval = strdup(yytext); return MOSTRE; }
"e"                     { yyval = strdup(yytext); return E; }
"ou"                    { yyval = strdup(yytext); return OU; }
"!="                    { yyval = strdup(yytext); return DIFERENTE; }
"=="                    { yyval = strdup(yytext); return IGUAL; }
">"                     { yyval = strdup(yytext); return MAIOR; }
"<"                     { yyval = strdup(yytext); return MENOR; }
">="                    { yyval = strdup(yytext); return MAIORIGUAL; }
"<="                    { yyval = strdup(yytext); return MENORIGUAL; }
"+"                     { yyval = strdup(yytext); return MAIS; }
"-"                     { yyval = strdup(yytext); return MENOS; }
"*"                     { yyval = strdup(yytext); return VEZES; }
"/"                     { yyval = strdup(yytext); return DIVIDIDO; }
"verdadeiro"            { yyval = strdup(yytext); return VERDADEIRO; }
"falso"                 { yyval = strdup(yytext); return FALSO; }
"("                     { yyval = strdup(yytext); return ABRE_PARENTESES; }
")"                     { yyval = strdup(yytext); return FECHA_PARENTESES; }
"{"                     { yyval = strdup(yytext); return ABRE_COLCHETE; }
"}"                     { yyval = strdup(yytext); return FECHA_COLCHETE; }
":"                     { yyval = strdup(yytext); return DOIS_PONTOS; }
","                     { yyval = strdup(yytext); return VIRGULA; }
[0-9]+                  { yyval = strdup(yytext); return DIGIT; }
[a-zA-Z_][a-zA-Z0-9_]*  { yyval = strdup(yytext); return IDENTIFIER; }
\"([^\\\"]|\\.)*\"      { yyval = strdup(yytext); return STRING; }

"//"                    { yyval = strdup(yytext); return COMENTARIO; }
\n                      { yyval = strdup(yytext); return QUEBRA_DE_LINHA; }
"//".*                  ; /* Ignora comentários de uma linha */
"\\\n"                  ; /* Ignora quebras de linha precedidas por \ */
.                       { yyval = strdup(yytext); printf("%s",yyval); }

%%

