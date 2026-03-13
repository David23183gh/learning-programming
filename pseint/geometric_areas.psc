Algoritmo geometric_areas
	//declarar variables o constants//
	definir lado, baserect, alturarect, basetri, alturatri, radio, cuadrado, rectangulo Como Entero
	Definir numpi, triangulo, circulo Como Real
	
	numpi <- 3.1416
	
	lado <- 0
	baserect <- 0
	alturarect <- 0
	basetri <- 0
	alturatri <- 0
	radio <- 0
	cuadrado <- 0
	rectangulo <- 0
	triangulo <- 0
	circulo <- 0
	
	//inputs
	Escribir "para el area de cuadrado dar los siguientes datos"
	Escribir "Cuanto mide el lado del cuadrado?"
	leer lado
	
	Escribir "Para el area del rectangulo pedir los siguientes datos"
	Escribir "Escribe la base del rectangulo"
	Leer baserect
	
	Escribir "Escribe la altura del rectangulo"
	Leer alturarect
	
	Escribir "para el area el triangulo dar los siguientes datos"
	Escribir "escribe la base del triangulo"
	Leer basetri
	
	Escribir "escribir la altura del triangulo"
	Leer alturatri
	
	Escribir "Para el area de un circulo pedir los siguientes datos"
	Leer radio
	
	//process
	cuadrado <- lado * lado
	rectangulo <- baserect * alturarect
	triangulo <- (basetri * alturatri) / 2
	circulo <- numpi * (radio * radio)
	
	//outputs
	Escribir "el area del cuadrado es ", cuadrado
	Escribir "el area del rectangulo es ", rectangulo
	Escribir "el area del triangulo es ", triangulo
	Escribir "el area del circulo es ", circulo
	
FinAlgoritmo