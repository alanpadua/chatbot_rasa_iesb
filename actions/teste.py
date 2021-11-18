
import re

def somar_valores(pedido:str):
    pedido_formatado = ''
    valor_total = 5.0

    itens_pedido = re.split("; |, |\*|\n|e ", pedido)
    # print(len(pedido_formatado))

    for item in itens_pedido:
        if item == 'jantinha':
            valor_total += 14.0
        else:
            valor_total += 7.0
    
    return itens_pedido, valor_total


pedidos, valor = somar_valores('carne, queijo, frango e jantinha')

print(str(pedidos).replace('[','').replace(']',''))
print(valor)