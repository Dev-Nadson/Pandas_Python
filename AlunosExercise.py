# Exercícios — Entregar até o fim do dia
# Carregue os dados do arquivo alunos.csv em um DataFrame. Ok
# Mostre apenas os alunos do curso de Engenharia. Ok
# Calcule a média das notas (Nota1 e Nota2) para cada aluno e crie uma nova coluna chamada MediaFinal. Ok
# Filtre os alunos com média final maior ou igual a 7. Ok
# Exiba o número total de faltas por cidade. Ok
# Liste a média de MediaFinal por curso. OK
# Qual cidade tem a maior média geral de MediaFinal?
# Crie uma nova coluna chamada Situação com os valores 'Aprovado' se a média for ≥7 e faltas ≤5, senão 'Reprovado'.
# Ordene os dados por curso e, dentro de cada curso, por média final decrescente.
# Salve o novo DataFrame com a coluna MediaFinal e Situação em um arquivo relatorio_final.csv.

import pandas as pd
DF_Students = pd.read_csv("./DataBases/alunos.csv")
DF_Students["MediaFinal"] = (DF_Students["Nota1"] + DF_Students["Nota2"]) / 2
Absences = DF_Students.groupby('Cidade')['Faltas'].sum() #Groutpby agrupa os valor por indice, ex: agrupa todos os valores em Recife
CousesAverages = DF_Students.groupby('Curso')['MediaFinal'].mean()

print("Options:" 
      "\n1. All Data"
      "\n2. Engineer Students"
      "\n3. Averages higher than seven"
      "\n4. Number of absences per city"
      "\n5. Final average of courses"
      "\n6. Course with the highest average")

option = input("Choose an option: ")
match option:
    case "1":
        print(f"All Data: \n\n{DF_Students}\n")
    case "2":
        print(f"Engineer Students: \n\n{DF_Students.loc[DF_Students['Curso'] == "Engenharia"]}")
    case "3":
        print(f"Students with average higher than seven: \n\n{DF_Students.loc[DF_Students['MediaFinal'] >= 7]}")
    case "4":
        print("Absences per city:\n")
        for city, absence in Absences.items():
            print(f"{city}: {absence}")
    case "5":
        for couse, average in CousesAverages.items():
            print(f"{couse}: {average:.2f}")
    case "6":
        print(f"Course with the highest average: \n{CousesAverages.idxmax()} {CousesAverages.max():.2f}")
    case _:
        print("Invalid Option")