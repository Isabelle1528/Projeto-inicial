nota1 = float (input("Digite a primeira nota do aluno:"))
nota2 = float (input("Digite a segunda nota do aluno:"))
nota3 = float (input("Digite a terceira nota do aluno:"))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print(f"Parabéns por sua nota. Você foi aprovado! Sua média é {media:.1f}")
elif media >= 3 and media < 7:
    print("Você esta em recuperação!")
    fez_recuperacao = input("Aluno já fez a recuperação?")
    if fez_recuperacao == "Sim":
        nota_recuperacao = float(input("Digite a nota de recuperação:"))
        if nota_recuperacao >= 5:
            print("Aluno(a) foi aprovado por meio da nota de recuperação.")
        else:
            print("Aluno(a) não obteve a nota suficient5e para ser aprovado após a recuperação.")
else:
    print(f"Que pena. Você não foi aprovado! Sua média é {media:.1f}")
