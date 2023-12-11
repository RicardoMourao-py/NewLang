flex newlang.l
bison -d newlang.y
gcc lex.yy.c newlang.tab.c -o newlang
./newlang < teste.nl
rm -rf lex.yy.c newlang.tab.c newlang.tab.h