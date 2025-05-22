# Exercícios — Entregar até o fim do dia
# Carregue os dados do arquivo alunos.csv em um DataFrame. Ok
# Mostre apenas os alunos do curso de Engenharia. Ok
# Calcule a média das notas (Nota1 e Nota2) para cada aluno e crie uma nova coluna chamada MediaFinal. Ok
# Filtre os alunos com média final maior ou igual a 7.
# Exiba o número total de faltas por cidade.
# Liste a média de MediaFinal por curso.
# Qual cidade tem a maior média geral de MediaFinal?
# Crie uma nova coluna chamada Situação com os valores 'Aprovado' se a média for ≥7 e faltas ≤5, senão 'Reprovado'.
# Ordene os dados por curso e, dentro de cada curso, por média final decrescente.
# Salve o novo DataFrame com a coluna MediaFinal e Situação em um arquivo relatorio_final.csv.

import pandas as pd
DF_Students = pd.read_csv("./DataBases/alunos.csv")
DF_Students["MediaFinal"] = (DF_Students["Nota1"] + DF_Students["Nota2"]) / 2

print("Options:" 
      "\n1. All Data"
      "\n2. Engineer Students")

option = input("Choose an option: ")
match option:
    case "1":
        print(f"All Data: \n\n{DF_Students}\n")
    case "2":
        print(f"Engineer Students: \n\n{DF_Students.loc[DF_Students['Curso'] == "Engenharia"]}")
    case "3":
        print(f"Average higer than seven: \n\n{DF_Students.loc[DF_Students['MediaFinal'] >= 7]}")
    case "4":
        Recife = DF_Students.loc[DF_Students['Cidade'] == "Recife"]
        Fortaleza = DF_Students.loc[DF_Students['Cidade'] == "Fortaleza"]
        Natal = DF_Students.loc[DF_Students['Cidade'] == "Natal"]
        print(f"Recife: {Recife['Faltas'].sum()}")
        print(f"Fortaleza: {Fortaleza['Faltas'].sum()}")
        print(f"Natal: {Natal['Faltas'].sum()}")