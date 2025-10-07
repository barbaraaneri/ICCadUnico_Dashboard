# Feito por Gustavo José da Silva Castro
# gustavocastro20042002@gmail.com

import csv
import pandas as pd

def geraCSV():
    with open('../../BasesDeDados/base_amostra_pessoa_201812.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter = ';')        
        data = []
        
        for row in reader:
            codigo = row[0]
            if codigo.startswith('35') : # Códigos de SP
                data.append(row)  # Adiciona a linha               

        with open("CadUnicoSP.csv", "w", newline='') as f:  # Adiciona newline=''
            writer = csv.writer(f)

            # Itera sobre o array e escreve cada elemento no arquivo
            writer.writerow(['cd_ibge','estrato','classf','id_familia','id_pessoa','cod_sexo_pessoa','idade','cod_parentesco_rf_pessoa','cod_raca_cor_pessoa','cod_local_nascimento_pessoa','cod_certidao_registrada_pessoa','cod_deficiencia_memb','cod_sabe_ler_escrever_memb','ind_frequenta_escola_memb','cod_escola_local_memb','cod_curso_frequenta_memb','cod_ano_serie_frequenta_memb','cod_curso_frequentou_pessoa_memb','cod_ano_serie_frequentou_memb','cod_concluiu_frequentou_memb','cod_trabalhou_memb','cod_afastado_trab_memb','cod_agricultura_trab_memb','cod_principal_trab_memb','val_remuner_emprego_memb','cod_trabalho_12_meses_memb','qtd_meses_12_meses_memb','val_renda_bruta_12_meses_memb','val_renda_doacao_memb','val_renda_aposent_memb','val_renda_seguro_desemp_memb','val_renda_pensao_alimen_memb','val_outras_rendas_memb','peso.fam','peso.pes'])  # Deve ser uma lista

            for row in data:
                writer.writerow(row)
geraCSV()
df = pd.read_csv('CadUnicoSP.csv')
print(df)