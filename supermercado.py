print("{:-^50}".format(" SUPERMERCADO BARATINHO "))

valor = float(input("Quanto deu sua compra? R$ "))
print('''QUAL FORMA DE PAGAMENTO?
[ 1 ] À vista no dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opcao = int(input("Qual a opção? "))

if opcao == 1:
    total = valor - (valor * 10 / 100)
elif opcao == 2:
    total = valor - (valor * 5 / 100)
elif opcao == 3:
    total = valor
elif opcao == 4:
    total = valor + (valor * 20 / 100 )
    parcela = int(input("Quantas parcelas? "))
    valorParcela = total / parcela
    print("\n" + "-"*50)
    print("Sua compra será parcelada em {}x de R${:.2f} COM JUROS".format(parcela, valorParcela))
    print("-"*50)

print("\n" + "="*50)
print("Resumo da compra:")
print("Valor original: R${:.2f}".format(valor))
print("Valor final:    R${:.2f}".format(total))
print("="*50)
