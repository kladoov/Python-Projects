# El Teorema de Pitagoras sirve para calcular la longitud de un lado de un triángulo rectángulo cuando conoces los otros dos

leg_a = float(input("Longiud del primer cateto: "))
leg_b = float(input("Longitud del segundo cateto: "))
hypo = (leg_a ** 2 + leg_b ** 2) * .5

print("La longitud de la hipotenusa es: ", hypo)