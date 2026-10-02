boletim = {}

while True:
    opcao = input("Deseja adicionar um aluno? (sim/nao): ").strip().lower()
    
    if opcao == 'sim':
        nome = input("Digite o nome do aluno: ").strip()
        nota = float(input(f"Digite a nota de {nome}: "))
        boletim[nome] = nota  # Nome como chave, nota como valor
    elif opcao == 'nao':
        print("\nCadastro encerrado. Gerando relatório...\n")
        break  
    else:
        print("Opção inválida! Digite apenas 'sim' ou 'nao'.")

print("--- RELATÓRIO DE APROVAÇÃO ---")
for aluno, nota in boletim.items():
    if nota >= 6.0:
        status = "Aprovado"
    else:
        status = "Reprovado"
    
    print(f"Aluno(a): {aluno} | Nota: {nota:.1f} -> Status: {status}")
