# Feito por Gustavo José da Silva Castro
# gustavocastro20042002@gmail.com

import csv

def QuantitativoIdade():
    with open('base_amostra_pessoa_201812.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter = ';')          
        colunas = next(reader) # Nome das colunas  
        indexIdade = colunas.index('idade') # Index da coluna desejada                 
        faixaEtaria = [[0, 17, 0], [18, 29, 0], [30, 49, 0], 
                    [50, 69, 0], [70, 89, 0], [90, 99, 0], 
                    [100, 130, 0]] #[idade minima, idade maxima, quantidade]        
        QtdPessoas = 0    
        QtdSemIdade = 0

        for row in reader:
            QtdPessoas += 1

            # Verifica se não possui Idade           
            if row[indexIdade] == '':
                QtdSemIdade += 1
                       
        for faixa in range(len(faixaEtaria)):
            limiteMin, limiteMax, count = faixaEtaria[faixa] # Atribui os valores da lista às variáveis        
    
            csvfile.seek(0)  # Volta ao início do arquivo
            next(reader)  # Pula a primeira linha com os nomes das colunas
        
            for row in reader:  # Itera em cada linha do CSV
                
                # Verifica se a idade está no intervalo desejado
                if int(row[indexIdade]) >= limiteMin and int (row[indexIdade]) <= limiteMax: 
                    count += 1

            faixaEtaria[faixa][2] = count # Atualiza a quantidade de pessoas em cada intervalo
        
        print(f'A base analisada possui {QtdPessoas} pessoas cadastradas.')
        print(f'{QtdSemIdade} pessoas não possuem Idade cadastrada, tratando-se de {(QtdSemIdade / QtdPessoas) * 100:.{4}f}% do total de pessoas na base de dados.')

        for i in range(len(faixaEtaria)):
            porcentagem = (faixaEtaria[i][2] / QtdPessoas) * 100
            print (f"Faixa etária entre {faixaEtaria[i][0]} e {faixaEtaria[i][1]} anos contém um total de {faixaEtaria[i][2]} pessoas, tratando-se de {porcentagem:.{4}f}% do total de pessoas na base de dados.")

def QuantitativoRenda():
    with open('base_amostra_pessoa_201812.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter = ';')
        colunas = next(reader) # Nome das colunas
        indexRenda = colunas.index('val_renda_bruta_12_meses_memb') # Index da coluna desejada
        faixaRenda = [[0, 85, 0], [85.01, 170, 0], 
                      [170.01, 477, 0], [477.01, float('inf'), 0]] # [valor minimo, valor maximo, quantidade]
        QtdPessoas = 0  
        QtdSemRenda = 0

        for row in reader:
            QtdPessoas += 1
            
            # Verifica se não possui Renda            
            if row[indexRenda] == '':
                QtdSemRenda += 1                    

        for faixa in range(len(faixaRenda)):
            limiteMin, limiteMax, count = faixaRenda[faixa] # Atribui os valores da lista às variáveis        
            
            csvfile.seek(0)  # Volta ao início do arquivo
            next(reader)  # Pula a primeira linha com os nomes das colunas
        
            for row in reader:  # Itera em cada linha do CSV

                if row[indexRenda] != '':
                    rendaMensal = float(row[indexRenda]) / 12

                    # Verifica se a renda está no intervalo desejado            
                    if limiteMin <= rendaMensal <= limiteMax: 
                        count += 1
                
            faixaRenda[faixa][2] = count # Atualiza a quantidade de pessoas em cada intervalo
        print(f'A base analisada possui {QtdPessoas} pessoas cadastradas.')
        print(f'{QtdSemRenda} pessoas não possuem renda cadastrada, tratando-se de {(QtdSemRenda / QtdPessoas) * 100:.{4}f}% do total de pessoas na base de dados.')

        for i in range(len(faixaRenda)):
            porcentagem = (faixaRenda[i][2] / QtdPessoas) * 100
            print (f"Faixa etária entre R${faixaRenda[i][0]} e R${faixaRenda[i][1]}  contém um total de {faixaRenda[i][2]} pessoas, tratando-se de {porcentagem:.{4}f}% do total de pessoas na base de dados")

QuantitativoIdade()
#QuantitativoRenda()