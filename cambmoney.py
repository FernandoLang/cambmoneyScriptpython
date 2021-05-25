def camb():
    #Adiciona uma tabela predefinida de moedas e seus valores 
    coins = [{"index":"1", "name":"real", "value":1}, {"index":"2","name":"dolar", "value":5.37}, {"index":"3","name":"euro", "value":6.54}]

    #Verifica se o valor informado é válido
    def verify(origin):
        origin2 =""
        isok = False
        for item in coins:
            if origin == item['index']:
                isok = True;
                origin2 = origin;
        if not isok:
            print("Por favor informe um valor válido: ")
            origin2 = input(":> ")
            verify(origin2)
        return origin2;

    
    
    #Calcula o valor de conversão e a taxa e mostra na tela
    def calc(value, ocoin, dcoin):
        if ocoin['name'] == dcoin['name']:
            print("Conversão para a mesma moeda: " + value)

        #Informa o valor da conversão
        else:
            newvalue = (float(value) * ocoin['value']) / dcoin['value']
            print(f"Valor convertido: {'%.2f' % newvalue}")
            taxa = (newvalue / 100) * 10
            vvalue = newvalue - taxa
            print(f"Valor da taxa: {'%.2f' % taxa}")
            print(f"Valor com a taxa descontada: {'%.2f' % vvalue}")
    
    
    
    def verifyVAlue(val):
        nnw = ""
        try:
            nv = float(val)
            nnw = val
        except:
            input("Informe um valor válido :> ")
            verifyVAlue(val)
        return nnw
    #Pede para informar a moeda de origem
    print("Selecione a moeda de origem: ")
    print("--------------------------")
    for item in coins:
        print(f"{item['index']}: {item['name']}")
        print("--------------------------")
    origin = input(":> ")
    #Verifica se o valor informado é válido
    origin = verify(origin)

    #Pede para informar a moeda de destino
    print("Selecione a moeda de destino: ")
    print("--------------------------")
    for item in coins:
        print(f"{item['index']}: {item['name']}")
        print("--------------------------")

    dest = input(":> ")
    #Verifica se o valor informado é válido
    dest = verify(dest)

    #Pede para informar o valor de conversão
    value = input("Informe o valor para a conversão :> ")
    value = verifyVAlue(value)

    try:
        origincoin ={}
        destcoin ={}
        #Retira da tabela os itens referentes a moeda de origem e destino
        for item in coins:
            if item['index'] == origin:
                origincoin = item
        for item in coins:
            if item['index'] == dest:
                destcoin = item;
        calc(value, origincoin, destcoin)
    except:
        print("Por favor informe o valor correto")


if __name__ == '__main__':
    while True:
        camb()
        val = input("Gostaria de fazer outra conversão? S/N :>")
        if val.lower() == "s":
            pass
        else:
            break