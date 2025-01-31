#input
cant_minutos=input("dijite el minuto:")
cant_minutos=int(cant_minutos)

#processing
print("calculando ")
print("espere")
if cant_minutos <= 3:
    valor_llamada= 300
else:
    valor_llamada= ( 300+50*(cant_minutos-3))
#output 
print ("el valor es:" + str(valor_llamada))

