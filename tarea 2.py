PrimerLado = int(input("ingrese valor de lado 1:"))
SegundoLado = int(input("ingrese valor de lado 2:"))
TercerLado = int(input("ingrese valor de lado 3:"))
PrimerSuma = PrimerLado + SegundoLado
SegundaSuma = SegundoLado + TercerLado
TercerSuma = PrimerLado + TercerLado
if PrimerSuma > TercerLado and SegundaSuma > PrimerLado and TercerSuma > SegundoLado: 
    print("es un triangulo")
    if PrimerLado == SegundoLado and SegundoLado == TercerLado and TercerLado == PrimerLado:
        print("y se trata de un triangulo equilatero")
    elif PrimerLado == SegundoLado or SegundoLado == TercerLado or TercerLado == PrimerLado:
            print("y se trata de un triangulo isosceles")
    else:
         print("y se trata de un triangulo escaleno")
else:
    print("no es un triangulo")
    
    
