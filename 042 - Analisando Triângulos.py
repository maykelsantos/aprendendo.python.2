seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print ('Os segmentos acima PODEM FORMAR UM triângulo!')
    if seg1 == seg2 and seg2 == seg3:
        print ('E será um triângulo EQUILÁTERO!')
    elif seg1 == seg2 or seg2 == seg3 or seg3 == seg1:
        print ('E será um triângulo ISÓSCELES!')
    elif seg1 != seg2 and seg1 != seg3:
        print ('E será um triângulo ESCALENO!')
else:
    print ('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
