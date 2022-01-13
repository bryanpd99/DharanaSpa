def vcedula(texto):
    validado=0
    if(texto.isdecimal() and len(texto)==10):
            # sin ceros a la izquierda
        nocero = texto.strip("0")
        cedula = int(nocero,0)
        verificador = cedula%10
        numero = cedula//10
        # mientras tenga números
        suma = 0
        while (numero > 0):
            
            # posición impar
            posimpar = numero%10
            numero   = numero//10
            posimpar = 2*posimpar
            if (posimpar  > 9):
                posimpar = posimpar-9
            # posición par
            pospar = numero%10
            numero = numero//10
            suma = suma + posimpar + pospar
        decenasup = suma//10 + 1
        calculado = decenasup*10 - suma
        if (calculado  >= 10):
            calculado = calculado - 10
        if (calculado == verificador):
            validado = 1
    else:
        validado = 0
        
    return (validado)
