import re
import random

while True:
    print("Selecione a opção desejada")
    print("Opção 1: Gerar CPF")
    print("Opção 2: Checar CPF")
    print("Opção 3: SAIR")
    opcao = int(input("Opção:"))


    if opcao == 1:
        cpf_gerado = ""

        for i in range(9):
            cpf_gerado += str(random.randint(0, 9))

        soma_dos_nove = 0
        for i, digito in enumerate(cpf_gerado[:9]):
            soma_dos_nove += int(digito) * (10 - i)
        
        muiltiplicar_um = soma_dos_nove * 10
        resto_um = muiltiplicar_um % 11

        cpf_gerado = (f"{cpf_gerado}{resto_um}")
        soma_dos_dez = 0

        for i, digito in enumerate(cpf_gerado[:10]):
            soma_dos_dez += int(digito) * (11 - i)
        
        muiltiplicar_dois = soma_dos_dez * 10
        resto_dois = muiltiplicar_dois % 11

        cpf_gerado = (f"{cpf_gerado}{resto_dois}")
        print(f"CPF Gerado:{cpf_gerado}")
        
        
    if opcao == 2:
        cpf_com_pontos = ( input("Qual seu CPF: ") )
        cpf = re.sub(r'[-.]', '', cpf_com_pontos)

        primeiraca = cpf[0]
        primeirorep = primeiraca * len(cpf)

        if len(cpf) < 9:
            print("CPF inválido.")
            continue
        elif cpf == primeirorep:
            print("CPF inválido")
            continue

        soma_dos_nove = 0

        for i, digito in enumerate(cpf[:9]):
            soma_dos_nove += int(digito) * (10 - i)
        
        muiltiplicar_um = soma_dos_nove * 10
        resto_um = muiltiplicar_um % 11

        if resto_um > 9:
            print("Primeiro digito: 0")
        else:
            print(f"Primeiro digito: {resto_um}")

        cpf = (f"{cpf}{resto_um}")
        soma_dos_dez = 0

        for i, digito in enumerate(cpf[:10]):
            soma_dos_dez += int(digito) * (11 - i)
        
        muiltiplicar_dois = soma_dos_dez * 10
        resto_dois = muiltiplicar_dois % 11

        if resto_dois > 9:
            print("Segundo digito: 0")
        else:
            print(f"Segundo digito: {resto_dois}")
    elif opcao == 3:
        print("Até a proxima.")
        break