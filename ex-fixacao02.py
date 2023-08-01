def calcular_conta_com_garcom(valor_conta):
    gorjeta = valor_conta * 0.10
    total_conta_com_garcom = valor_conta + gorjeta
    return total_conta_com_garcom


valor_conta = float(input("Digite o valor da conta: "))
valor_total_com_garcom = calcular_conta_com_garcom(valor_conta)

print(f"O valor total da conta com 10% do garçom é: R$ {valor_total_com_garcom:.2f}")