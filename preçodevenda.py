x = float (input ("Valor de venda do produto:"))

lucro70 = x * 70 /100
lucro50 = x * 50 / 100
lucro40 = x * 40 /100
lucro30 = x * 30 /100

if x<0 : print ("VALOR INVALIDO")
else:  
    if x<10 : venda = x + lucro70
    if x>=10 and x<30 : venda =  x + lucro50
    if x>=30 and x<50 : venda = x + lucro40
    if x>=50 : venda = x + lucro30
 

print ("Resultado do cálculo :" , venda  )