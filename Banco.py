saldo = 0
limite_por_saque = 500
limite_de_saques = 3
quantidade_de_saques = 0
extrato = ""
operação = """"
------------------------
[1] Extrato            -
[2] Depósito           -
[3] Saque              -
[4] Encerrar           -
------------------------
=> Escolha """

while True:

   escolha = input(operação)

   if escolha == "1":

     print("Você escolheu ver o extrato, verifique-o abaixo:\n")

     print("//////////EXTRATO//////////")

     if extrato != "":

      print(f"\nSaldo : {saldo: .2f}")

      print(f"\n{extrato}")

     else: 
      print("NÃO HOUVERAM MOVIMENTAÇÕES EM SUA CONTA, SEU SALDO É DE R$0.00")

   
   elif escolha == "2":
     valor_depósito = float(input("Você escolheu depositar, escolha qualquer valor acima de 0 reais: "))
     
     if valor_depósito > 0:
      print(f"Você depositou {valor_depósito}, verifique o extrato para saber mais")

      saldo += valor_depósito

      extrato += f"Depósito de {valor_depósito: .2f}\n"

     else: print("Você não pode depositar valores menores que 1 real, tente novamente")



   elif escolha == "3":

    if limite_de_saques > 0 and saldo > 0:

      valor_saque = float(input(f"Você escolheu sacar, você possui {limite_de_saques} restantes, qual valor deseja sacar?"))

      if valor_saque > 0 and valor_saque <= 500 and valor_saque <= saldo: 

       print(f"Parabéns, você sacou {valor_saque} em sua conta, verifique o extrato para saber mais") 

       extrato += f"Saque no valor de  R$ {valor_saque: .2f}\n"
       limite_de_saques -= 1
       saldo -= valor_saque

      elif valor_saque <= 0: print("Tente novamente, você não pode sacar valores abaixo de 1 real")

      else: print("Tente novamnente, seu limite por saque é de 500 reais")

    elif limite_de_saques <= 0: print("Você excedeu seu limite de saques diários, tente novamente amanhã")
       
    else: print("Seu saque não pode ser realizado, pois negativaria sua conta")

   elif escolha == "4": 
    print("Você escolheu sair, obrigado pela visita") 
    break
   
   else: 
    print("Por favor, selecione alguma opção válida")
  