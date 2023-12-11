declare inteiro: contador
contador recebe 1

enquanto contador < 5 {
    mostre(contador)
    contador recebe contador + 1
}

//teste1
declare inteiro: x_1
x_1 recebe leia()

mostre(x_1)

se (x_1 > 1 e !!!(x_1 < 1)) ou x_1 == 3 entao {
	x_1 recebe 2
}

declare inteiro: x recebe 3+6/3   *  2 -+-  +  2*4/2 + 0/1 -((6+ ((4)))/(2)) // Teste // Teste 2
declare inteiro: y_1 recebe 3
y_1 recebe y_1 + x_1
declare inteiro: z__
z__ recebe x + y_1

se x_1 == 2 entao {
	x_1 recebe 2
}

se x_1 == 3 entao {
	x_1 recebe 2
} senao {
	x_1 recebe 3
}

durante x_1 recebe 0; x_1 < 1 ou x == 2; x_1 recebe x_1 + 1 {
	mostre(x_1)
}



// // Saida final
mostre(x_1)
mostre(x)
mostre(z__+1)

// All bool and inteiro operations
declare inteiro: y recebe 2
declare inteiro: z
z recebe (y == 2)
mostre(y+z)
mostre(y-z)
mostre(y*z)
mostre(y/z)
mostre(y == z)
mostre(y < z)
mostre(y > z)

// All str operations 
declare texto: a 
declare texto: b

x_1 recebe 1 
y recebe 1 
z recebe 2
a recebe "abc"
b recebe "def"
mostre(a.b)
mostre(a.x_1)
mostre(x_1.a)
mostre(y.z)
mostre(a.(x_1==1))
mostre(a == a)
mostre(a < b)
mostre(a > b)

//teste2

declare texto: x_3 
x_3 recebe leia()