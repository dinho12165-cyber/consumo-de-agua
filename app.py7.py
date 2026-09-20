# entrada de dados, aqui produzo e envio o codigo: 

imovel = input("digite o tipo de imovel")
consumo = float(input("digite o consumo_mensal"))

# processamento: aqui combino as estruturas de decisao com os operadores  logicos e relacionais.

if ("apartamento") and consumo < 10:
   print("consumo economico - excelente controle de agua")
elif  ("casa") and consumo < 25:
   print("consumo moderado - dentro do padrao residencial")
elif  ("apartamento") + ("casa")  and consumo == 25:
   print("consumo moderado - dentro do padrao residencial")
else:
   print("consumo excessivo - adote medidas de economia e verifique vazamentos")

   ##  aqui faco a etapa de integracao com o match case para o programa

imovel = ("digite o tipo de imovel")
match imovel:
   case:
    print("consumo moderado < 25 - dentro do padrao residencial")
   case:
    print("consumo economico < 10 - excelente controle de agua")
   case _:
    print("tarifa comercial aplicada - consulte plano corporativo")