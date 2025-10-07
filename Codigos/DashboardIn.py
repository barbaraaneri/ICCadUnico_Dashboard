# Feito por Bárbara Rezende Neri
# barbaranerics@gmail.com

import streamlit as st
from streamlit_echarts import st_echarts
import pandas as pd
import folium
from streamlit_folium import st_folium

# Função para criar os dicionários de opções para cada gráfico
def CriarOpcoesGrafico(titulo, nome, data, tipoGrafico):
    #options = 
    if tipoGrafico == 'Donut':
        options = {
                    "title": {"text": titulo, "left": "center"},
                    "tooltip": {"trigger": "item",
                                "formatter": "<b>{a} <br/>{b}: {c} ({d}%)</b>"}, #Sem essa linha ele não mostra a porcentagem, mas perde a bolinha m a cor que é bonito                    
                    "legend": {"top": "5%", "left": "center"},
                    "series": [{
                        "name": nome,
                        "type": "pie",
                        "radius": ["40%", "70%"],
                        "avoidLabelOverlap": False,
                        "itemStyle": {
                            "borderRadius": 10,
                            "borderColor": "#fff",
                            "borderWidth": 2,
                        },
                        "label": {"show": False, "position": "center"},
                        "emphasis": {
                            "label": {"show": True, "fontSize": "40", "fontWeight": "bold"}
                        },
                        "labelLine": {"show": False},
                        "data": data
                    }]
                  }
    elif tipoGrafico == 'Pizza':
        options = {
                    "title": {"text": titulo, "left": "center"},
                    "tooltip": {"trigger": "item",
                                "formatter": "<b>{a} <br/>{b}: {c} ({d}%)</b>"}, #Sem essa linha ele não mostra a porcentagem, mas perde a bolinha com a cor que é bonito
                    "legend": {"top": "5%", "left": "center"},
                    "series": [{
                                "name": nome,
                                "type": "pie",
                                "radius": "50%",
                                "data": data,
                                "emphasis":{
                                            "itemStyle":{
                                                        "shadowBlur": 10,
                                                        "shadowOffsetX": 0,
                                                        "shadowColor": "rgba(0, 0, 0, 0.5)",
                                                        }
                                            },
                            }     
                            ],
                    }
    elif tipoGrafico == 'Barra':
        options = {
                    "title": {"text": titulo, "left": "center"},
                    "tooltip": {
                                "trigger": "item",
                                "formatter": "<b>{a}<br/>{b} anos: {c} pessoas </b>"
                               },
                    "legend": {"top": "5%", "left": "center"},
                    "xAxis": {
                                "type": "category",
                                "data": data[0],
                             },
                    "yAxis": {
                                "type": "value"
                             },
                    "series": [{
                                "name": nome,
                                "data": data[1], 
                                "type": "bar"
                              }],
                  }
    else:
        options = {
                    "title": [
                                {"text": titulo, "left": "center"},
                            ],
                    "dataset": [{
                                "source": [
                                            data       
                                            ]
                                },
                                {
                                "transform": {
                                            "type": "boxplot",
                                            "config": {"itemNameFormatter": ""},
                                            }
                                },
                                {"fromDatasetIndex": 1, "fromTransformResult": 1},
                            ],
                    "tooltip": {"trigger": "item", "axisPointer": {"type": "shadow"}},
                    "grid": {"left": "10%", "right": "10%", "bottom": "15%"},
                    "xAxis": {
                                "type": "category",
                                "boundaryGap": True,
                                "nameGap": 30,
                                "splitArea": {"show": False},
                                "splitLine": {"show": False},
                            },
                    "yAxis": {
                                "type": "value",
                                "name": nome,
                                "splitArea": {"show": True},
                            },
                    "series": [
                                {"name": "boxplot", "type": "boxplot", "datasetIndex": 1},
                                {"name": "outlier", "type": "scatter", "datasetIndex": 2},
                            ],
                }
    return options

def Filtragem(filtroSexo, filtroRaca, filtroDeficiencia, filtroIdade, filtroRenda,checkDivinopolis, checkOuroBranco, checkSaoJoaoDelRei, checkSeteLagoas, dfCadUnicoDivinopolis, dfCadUnicoOuroBranco, dfCadUnicoSaoJoaoDelRei, dfCadUnicoSeteLagoas):
    if filtroSexo != 'Sem Filtro':
    #cod_sexo_pessoa
    #Sexo
    #1 - Masculino
    #2 - Feminino
        if filtroSexo == 'Masculino':
            if checkDivinopolis:
                dfCadUnicoDivinopolis = dfCadUnicoDivinopolis[dfCadUnicoDivinopolis['cod_sexo_pessoa'] == 1]
            if checkOuroBranco:
                dfCadUnicoOuroBranco = dfCadUnicoOuroBranco[dfCadUnicoOuroBranco['cod_sexo_pessoa'] == 1]
            if checkSaoJoaoDelRei:
                dfCadUnicoSaoJoaoDelRei = dfCadUnicoSaoJoaoDelRei[dfCadUnicoSaoJoaoDelRei['cod_sexo_pessoa'] == 1]
            if checkSeteLagoas:
                dfCadUnicoSeteLagoas = dfCadUnicoSeteLagoas[dfCadUnicoSeteLagoas['cod_sexo_pessoa'] == 1]
            
        if filtroSexo == 'Feminino':
            if checkDivinopolis:
                dfCadUnicoDivinopolis = dfCadUnicoDivinopolis[dfCadUnicoDivinopolis['cod_sexo_pessoa'] == 2]
            if checkOuroBranco:
                dfCadUnicoOuroBranco = dfCadUnicoOuroBranco[dfCadUnicoOuroBranco['cod_sexo_pessoa'] == 2]
            if checkSaoJoaoDelRei:
                dfCadUnicoSaoJoaoDelRei = dfCadUnicoSaoJoaoDelRei[dfCadUnicoSaoJoaoDelRei['cod_sexo_pessoa'] == 2]
            if checkSeteLagoas:
                dfCadUnicoSeteLagoas = dfCadUnicoSeteLagoas[dfCadUnicoSeteLagoas['cod_sexo_pessoa'] == 2]
    
    if filtroRaca != 'Sem Filtro':
        #cod_raca_cor_pessoa
        #Cor ou raça
        #1 - Branca
        #2 - Preta
        #3 - Amarela
        #4 - Parda
        #5 - Indígena
        if filtroRaca == 'Branca':
            if checkDivinopolis:
                dfCadUnicoDivinopolis = dfCadUnicoDivinopolis[dfCadUnicoDivinopolis['cod_raca_cor_pessoa'] == 1]
            if checkOuroBranco:
                dfCadUnicoOuroBranco = dfCadUnicoOuroBranco[dfCadUnicoOuroBranco['cod_raca_cor_pessoa'] == 1]
            if checkSaoJoaoDelRei:
                dfCadUnicoSaoJoaoDelRei = dfCadUnicoSaoJoaoDelRei[dfCadUnicoSaoJoaoDelRei['cod_raca_cor_pessoa'] == 1]
            if checkSeteLagoas:
                dfCadUnicoSeteLagoas = dfCadUnicoSeteLagoas[dfCadUnicoSeteLagoas['cod_raca_cor_pessoa'] == 1]
        
        if filtroRaca == 'Preta':
            if checkDivinopolis:
                dfCadUnicoDivinopolis = dfCadUnicoDivinopolis[dfCadUnicoDivinopolis['cod_raca_cor_pessoa'] == 2]
            if checkOuroBranco:
                dfCadUnicoOuroBranco = dfCadUnicoOuroBranco[dfCadUnicoOuroBranco['cod_raca_cor_pessoa'] == 2]
            if checkSaoJoaoDelRei:
                dfCadUnicoSaoJoaoDelRei = dfCadUnicoSaoJoaoDelRei[dfCadUnicoSaoJoaoDelRei['cod_raca_cor_pessoa'] == 2]
            if checkSeteLagoas:
                dfCadUnicoSeteLagoas = dfCadUnicoSeteLagoas[dfCadUnicoSeteLagoas['cod_raca_cor_pessoa'] == 2]

        if filtroRaca == 'Amarela':
            if checkDivinopolis:
                dfCadUnicoDivinopolis = dfCadUnicoDivinopolis[dfCadUnicoDivinopolis['cod_raca_cor_pessoa'] == 3]
            if checkOuroBranco:
                dfCadUnicoOuroBranco = dfCadUnicoOuroBranco[dfCadUnicoOuroBranco['cod_raca_cor_pessoa'] == 3]
            if checkSaoJoaoDelRei:
                dfCadUnicoSaoJoaoDelRei = dfCadUnicoSaoJoaoDelRei[dfCadUnicoSaoJoaoDelRei['cod_raca_cor_pessoa'] == 3]
            if checkSeteLagoas:
                dfCadUnicoSeteLagoas = dfCadUnicoSeteLagoas[dfCadUnicoSeteLagoas['cod_raca_cor_pessoa'] == 3]

        if filtroRaca == 'Parda':
            if checkDivinopolis:
                dfCadUnicoDivinopolis = dfCadUnicoDivinopolis[dfCadUnicoDivinopolis['cod_raca_cor_pessoa'] == 4]
            if checkOuroBranco:
                dfCadUnicoOuroBranco = dfCadUnicoOuroBranco[dfCadUnicoOuroBranco['cod_raca_cor_pessoa'] == 4]
            if checkSaoJoaoDelRei:
                dfCadUnicoSaoJoaoDelRei = dfCadUnicoSaoJoaoDelRei[dfCadUnicoSaoJoaoDelRei['cod_raca_cor_pessoa'] == 4]
            if checkSeteLagoas:
                dfCadUnicoSeteLagoas = dfCadUnicoSeteLagoas[dfCadUnicoSeteLagoas['cod_raca_cor_pessoa'] == 4]

        if filtroRaca == 'Indigena':
            if checkDivinopolis:
                dfCadUnicoDivinopolis = dfCadUnicoDivinopolis[dfCadUnicoDivinopolis['cod_raca_cor_pessoa'] == 5]
            if checkOuroBranco:
                dfCadUnicoOuroBranco = dfCadUnicoOuroBranco[dfCadUnicoOuroBranco['cod_raca_cor_pessoa'] == 5]
            if checkSaoJoaoDelRei:
                dfCadUnicoSaoJoaoDelRei = dfCadUnicoSaoJoaoDelRei[dfCadUnicoSaoJoaoDelRei['cod_raca_cor_pessoa'] == 5]
            if checkSeteLagoas:
                dfCadUnicoSeteLagoas = dfCadUnicoSeteLagoas[dfCadUnicoSeteLagoas['cod_raca_cor_pessoa'] == 5]      
    
    if filtroDeficiencia != 'Sem Filtro':
        #cod_deficiencia_memb
        #Pessoa tem deficiência?
        #1 - Sim
        #2 - Não
        if filtroDeficiencia == 'Possui Deficiência':
            if checkDivinopolis:
                dfCadUnicoDivinopolis = dfCadUnicoDivinopolis[dfCadUnicoDivinopolis['cod_deficiencia_memb'] == 1]
            if checkOuroBranco:
                dfCadUnicoOuroBranco = dfCadUnicoOuroBranco[dfCadUnicoOuroBranco['cod_deficiencia_memb'] == 1]
            if checkSaoJoaoDelRei:
                dfCadUnicoSaoJoaoDelRei = dfCadUnicoSaoJoaoDelRei[dfCadUnicoSaoJoaoDelRei['cod_deficiencia_memb'] == 1]
            if checkSeteLagoas:
                dfCadUnicoSeteLagoas = dfCadUnicoSeteLagoas[dfCadUnicoSeteLagoas['cod_deficiencia_memb'] == 1]

        if filtroDeficiencia == 'Não Possui Deficiência':
            if checkDivinopolis:
                dfCadUnicoDivinopolis = dfCadUnicoDivinopolis[dfCadUnicoDivinopolis['cod_deficiencia_memb'] == 2]
            if checkOuroBranco:
                dfCadUnicoOuroBranco = dfCadUnicoOuroBranco[dfCadUnicoOuroBranco['cod_deficiencia_memb'] == 2]
            if checkSaoJoaoDelRei:
                dfCadUnicoSaoJoaoDelRei = dfCadUnicoSaoJoaoDelRei[dfCadUnicoSaoJoaoDelRei['cod_deficiencia_memb'] == 2]
            if checkSeteLagoas:
                dfCadUnicoSeteLagoas = dfCadUnicoSeteLagoas[dfCadUnicoSeteLagoas['cod_deficiencia_memb'] == 2]

    if filtroIdade != 'Sem Filtro':
        #idade
        #Idade calculada a partir da diferença entre a data de nascimento da pessoa e a data de referência da base
        #Dado inteiro de tamanho até 3
        if filtroIdade == 'Primeira Infância (0-5 anos)':
            if checkDivinopolis:
                dfCadUnicoDivinopolis = dfCadUnicoDivinopolis[dfCadUnicoDivinopolis['idade'] <= 5]
            if checkOuroBranco:
                dfCadUnicoOuroBranco = dfCadUnicoOuroBranco[dfCadUnicoOuroBranco['idade'] <= 5]
            if checkSaoJoaoDelRei:
                dfCadUnicoSaoJoaoDelRei = dfCadUnicoSaoJoaoDelRei[dfCadUnicoSaoJoaoDelRei['idade'] <= 5]
            if checkSeteLagoas:
                dfCadUnicoSeteLagoas = dfCadUnicoSeteLagoas[dfCadUnicoSeteLagoas['idade'] <= 5]

        if filtroIdade == 'Segunda Infância (6-12 anos)':
            if checkDivinopolis:
                dfCadUnicoDivinopolis = dfCadUnicoDivinopolis[(dfCadUnicoDivinopolis['idade'] >= 6) & (dfCadUnicoDivinopolis['idade'] <= 12)]
            if checkOuroBranco:
                dfCadUnicoOuroBranco = dfCadUnicoOuroBranco[(dfCadUnicoOuroBranco['idade'] >= 6) & (dfCadUnicoOuroBranco['idade'] <= 12)]
            if checkSaoJoaoDelRei:
                dfCadUnicoSaoJoaoDelRei = dfCadUnicoSaoJoaoDelRei[(dfCadUnicoSaoJoaoDelRei['idade'] >= 6) & (dfCadUnicoSaoJoaoDelRei['idade'] <= 12)]
            if checkSeteLagoas:
                dfCadUnicoSeteLagoas = dfCadUnicoSeteLagoas[(dfCadUnicoSeteLagoas['idade'] >= 6) & (dfCadUnicoSeteLagoas['idade'] <= 12)]

        if filtroIdade == 'Adolescência Inicial (13-15 anos)':
            if checkDivinopolis:
                dfCadUnicoDivinopolis = dfCadUnicoDivinopolis[(dfCadUnicoDivinopolis['idade'] >= 13) & (dfCadUnicoDivinopolis['idade'] <= 15)]
            if checkOuroBranco:
                dfCadUnicoOuroBranco = dfCadUnicoOuroBranco[(dfCadUnicoOuroBranco['idade'] >= 13) & (dfCadUnicoOuroBranco['idade'] <= 15)]
            if checkSaoJoaoDelRei:
                dfCadUnicoSaoJoaoDelRei = dfCadUnicoSaoJoaoDelRei[(dfCadUnicoSaoJoaoDelRei['idade'] >= 13) & (dfCadUnicoSaoJoaoDelRei['idade'] <= 15)]
            if checkSeteLagoas:
                dfCadUnicoSeteLagoas = dfCadUnicoSeteLagoas[(dfCadUnicoSeteLagoas['idade'] >= 13) & (dfCadUnicoSeteLagoas['idade'] <= 15)]

        if filtroIdade == 'Adolescência Tardia (16-18 anos)':
            if checkDivinopolis:
                dfCadUnicoDivinopolis = dfCadUnicoDivinopolis[(dfCadUnicoDivinopolis['idade'] >= 16) & (dfCadUnicoDivinopolis['idade'] <= 18)]
            if checkOuroBranco:
                dfCadUnicoOuroBranco = dfCadUnicoOuroBranco[(dfCadUnicoOuroBranco['idade'] >= 16) & (dfCadUnicoOuroBranco['idade'] <= 18)]
            if checkSaoJoaoDelRei:
                dfCadUnicoSaoJoaoDelRei = dfCadUnicoSaoJoaoDelRei[(dfCadUnicoSaoJoaoDelRei['idade'] >= 16) & (dfCadUnicoSaoJoaoDelRei['idade'] <= 18)]
            if checkSeteLagoas:
                dfCadUnicoSeteLagoas = dfCadUnicoSeteLagoas[(dfCadUnicoSeteLagoas['idade'] >= 16) & (dfCadUnicoSeteLagoas['idade'] <= 18)]

        if filtroIdade == 'Juventude Inicial (19-24 anos)':
            if checkDivinopolis:
                dfCadUnicoDivinopolis = dfCadUnicoDivinopolis[(dfCadUnicoDivinopolis['idade'] >= 19) & (dfCadUnicoDivinopolis['idade'] <= 24)]
            if checkOuroBranco:
                dfCadUnicoOuroBranco = dfCadUnicoOuroBranco[(dfCadUnicoOuroBranco['idade'] >= 19) & (dfCadUnicoOuroBranco['idade'] <= 24)]
            if checkSaoJoaoDelRei:
                dfCadUnicoSaoJoaoDelRei = dfCadUnicoSaoJoaoDelRei[(dfCadUnicoSaoJoaoDelRei['idade'] >= 19) & (dfCadUnicoSaoJoaoDelRei['idade'] <= 24)]
            if checkSeteLagoas:
                dfCadUnicoSeteLagoas = dfCadUnicoSeteLagoas[(dfCadUnicoSeteLagoas['idade'] >= 19) & (dfCadUnicoSeteLagoas['idade'] <= 24)]

        if filtroIdade == 'Juventude Plena (25-30 anos)':
            if checkDivinopolis:
                dfCadUnicoDivinopolis = dfCadUnicoDivinopolis[(dfCadUnicoDivinopolis['idade'] >= 25) & (dfCadUnicoDivinopolis['idade'] <= 30)]
            if checkOuroBranco:
                dfCadUnicoOuroBranco = dfCadUnicoOuroBranco[(dfCadUnicoOuroBranco['idade'] >= 25) & (dfCadUnicoOuroBranco['idade'] <= 30)]
            if checkSaoJoaoDelRei:
                dfCadUnicoSaoJoaoDelRei = dfCadUnicoSaoJoaoDelRei[(dfCadUnicoSaoJoaoDelRei['idade'] >= 25) & (dfCadUnicoSaoJoaoDelRei['idade'] <= 30)]
            if checkSeteLagoas:
                dfCadUnicoSeteLagoas = dfCadUnicoSeteLagoas[(dfCadUnicoSeteLagoas['idade'] >= 25) & (dfCadUnicoSeteLagoas['idade'] <= 30)]

        if filtroIdade == 'Adulto (31-45 anos)':
            if checkDivinopolis:
                dfCadUnicoDivinopolis = dfCadUnicoDivinopolis[(dfCadUnicoDivinopolis['idade'] >= 31) & (dfCadUnicoDivinopolis['idade'] <= 45)]
            if checkOuroBranco:
                dfCadUnicoOuroBranco = dfCadUnicoOuroBranco[(dfCadUnicoOuroBranco['idade'] >= 31) & (dfCadUnicoOuroBranco['idade'] <= 45)]
            if checkSaoJoaoDelRei:
                dfCadUnicoSaoJoaoDelRei = dfCadUnicoSaoJoaoDelRei[(dfCadUnicoSaoJoaoDelRei['idade'] >= 31) & (dfCadUnicoSaoJoaoDelRei['idade'] <= 45)]
            if checkSeteLagoas:
                dfCadUnicoSeteLagoas = dfCadUnicoSeteLagoas[(dfCadUnicoSeteLagoas['idade'] >= 31) & (dfCadUnicoSeteLagoas['idade'] <= 45)]

        if filtroIdade == 'Meia-idade (46-60 anos)':
            if checkDivinopolis:
                dfCadUnicoDivinopolis = dfCadUnicoDivinopolis[(dfCadUnicoDivinopolis['idade'] >= 46) & (dfCadUnicoDivinopolis['idade'] <= 60)]
            if checkOuroBranco:
                dfCadUnicoOuroBranco = dfCadUnicoOuroBranco[(dfCadUnicoOuroBranco['idade'] >= 46) & (dfCadUnicoOuroBranco['idade'] <= 60)]
            if checkSaoJoaoDelRei:
                dfCadUnicoSaoJoaoDelRei = dfCadUnicoSaoJoaoDelRei[(dfCadUnicoSaoJoaoDelRei['idade'] >= 46) & (dfCadUnicoSaoJoaoDelRei['idade'] <= 60)]
            if checkSeteLagoas:
                dfCadUnicoSeteLagoas = dfCadUnicoSeteLagoas[(dfCadUnicoSeteLagoas['idade'] >= 46) & (dfCadUnicoSeteLagoas['idade'] <= 60)]

        if filtroIdade == 'Idoso (60-75 anos)':
            if checkDivinopolis:
                dfCadUnicoDivinopolis = dfCadUnicoDivinopolis[(dfCadUnicoDivinopolis['idade'] >= 60) & (dfCadUnicoDivinopolis['idade'] <= 75)]
            if checkOuroBranco:
                dfCadUnicoOuroBranco = dfCadUnicoOuroBranco[(dfCadUnicoOuroBranco['idade'] >= 60) & (dfCadUnicoOuroBranco['idade'] <= 75)]
            if checkSaoJoaoDelRei:
                dfCadUnicoSaoJoaoDelRei = dfCadUnicoSaoJoaoDelRei[(dfCadUnicoSaoJoaoDelRei['idade'] >= 60) & (dfCadUnicoSaoJoaoDelRei['idade'] <= 75)]
            if checkSeteLagoas:
                dfCadUnicoSeteLagoas = dfCadUnicoSeteLagoas[(dfCadUnicoSeteLagoas['idade'] >= 60) & (dfCadUnicoSeteLagoas['idade'] <= 75)]

        if filtroIdade == 'Idade Avançada (75 anos ou mais)':
            if checkDivinopolis:
                dfCadUnicoDivinopolis = dfCadUnicoDivinopolis[dfCadUnicoDivinopolis['idade'] >= 75]
            if checkOuroBranco:
                dfCadUnicoOuroBranco = dfCadUnicoOuroBranco[dfCadUnicoOuroBranco['idade'] >= 75]
            if checkSaoJoaoDelRei:
                dfCadUnicoSaoJoaoDelRei = dfCadUnicoSaoJoaoDelRei[dfCadUnicoSaoJoaoDelRei['idade'] >= 75]
            if checkSeteLagoas:
                dfCadUnicoSeteLagoas = dfCadUnicoSeteLagoas[dfCadUnicoSeteLagoas['idade'] >= 75]

    if filtroRenda != 'Sem Filtro':
        #val_renda_bruta_12_meses_memb
        #Valor de remuneração bruta no formato NNNNN (sem casas decimais). Ex. Uma remuneração de R$ 125,00 constará na base como 125. 
        if filtroRenda == '0 a 85 Reais':
            if checkDivinopolis:
                dfCadUnicoDivinopolis = dfCadUnicoDivinopolis[(dfCadUnicoDivinopolis['val_renda_bruta_12_meses_memb'] / 12) <= 85]
            if checkOuroBranco:
                dfCadUnicoOuroBranco = dfCadUnicoOuroBranco[(dfCadUnicoOuroBranco['val_renda_bruta_12_meses_memb'] / 12) <= 85]
            if checkSaoJoaoDelRei:
                dfCadUnicoSaoJoaoDelRei = dfCadUnicoSaoJoaoDelRei[(dfCadUnicoSaoJoaoDelRei['val_renda_bruta_12_meses_memb'] / 12) <= 85]
            if checkSeteLagoas:
                dfCadUnicoSeteLagoas = dfCadUnicoSeteLagoas[(dfCadUnicoSeteLagoas['val_renda_bruta_12_meses_memb'] / 12) <= 85]

        if filtroRenda == '85,01 a 170 Reais':
            if checkDivinopolis:
                dfCadUnicoDivinopolis = dfCadUnicoDivinopolis[((dfCadUnicoDivinopolis['val_renda_bruta_12_meses_memb'] / 12) > 85) & ((dfCadUnicoDivinopolis['val_renda_bruta_12_meses_memb'] / 12) <= 170)]
            if checkOuroBranco:
                dfCadUnicoOuroBranco = dfCadUnicoOuroBranco[((dfCadUnicoOuroBranco['val_renda_bruta_12_meses_memb'] / 12) > 85) & ((dfCadUnicoOuroBranco['val_renda_bruta_12_meses_memb'] / 12) <= 170)]
            if checkSaoJoaoDelRei:
                dfCadUnicoSaoJoaoDelRei = dfCadUnicoSaoJoaoDelRei[((dfCadUnicoSaoJoaoDelRei['val_renda_bruta_12_meses_memb'] / 12) > 85) & ((dfCadUnicoSaoJoaoDelRei['val_renda_bruta_12_meses_memb'] / 12) <= 170)]
            if checkSeteLagoas:
                dfCadUnicoSeteLagoas = dfCadUnicoSeteLagoas[((dfCadUnicoSeteLagoas['val_renda_bruta_12_meses_memb'] / 12) > 85) & ((dfCadUnicoSeteLagoas['val_renda_bruta_12_meses_memb'] / 12) <= 170)]

        if filtroRenda == '170,01 a 477 Reais':
            if checkDivinopolis:
                dfCadUnicoDivinopolis = dfCadUnicoDivinopolis[((dfCadUnicoDivinopolis['val_renda_bruta_12_meses_memb'] / 12) > 170) & ((dfCadUnicoDivinopolis['val_renda_bruta_12_meses_memb'] / 12) <= 477)]
            if checkOuroBranco:
                dfCadUnicoOuroBranco = dfCadUnicoOuroBranco[((dfCadUnicoOuroBranco['val_renda_bruta_12_meses_memb'] / 12) > 170) & ((dfCadUnicoOuroBranco['val_renda_bruta_12_meses_memb'] / 12) <= 477)]
            if checkSaoJoaoDelRei:
                dfCadUnicoSaoJoaoDelRei = dfCadUnicoSaoJoaoDelRei[((dfCadUnicoSaoJoaoDelRei['val_renda_bruta_12_meses_memb'] / 12) > 170) & ((dfCadUnicoSaoJoaoDelRei['val_renda_bruta_12_meses_memb'] / 12) <= 477)]
            if checkSeteLagoas:
                dfCadUnicoSeteLagoas = dfCadUnicoSeteLagoas[((dfCadUnicoSeteLagoas['val_renda_bruta_12_meses_memb'] / 12) > 170) & ((dfCadUnicoSeteLagoas['val_renda_bruta_12_meses_memb'] / 12) <= 477)]

        if filtroRenda == 'A partir de 477,01 Reais':
            if checkDivinopolis:
                dfCadUnicoDivinopolis = dfCadUnicoDivinopolis[(dfCadUnicoDivinopolis['val_renda_bruta_12_meses_memb'] / 12) > 477]
            if checkOuroBranco:
                dfCadUnicoOuroBranco = dfCadUnicoOuroBranco[(dfCadUnicoOuroBranco['val_renda_bruta_12_meses_memb'] / 12) > 477]
            if checkSaoJoaoDelRei:
                dfCadUnicoSaoJoaoDelRei = dfCadUnicoSaoJoaoDelRei[(dfCadUnicoSaoJoaoDelRei['val_renda_bruta_12_meses_memb'] / 12) > 477]
            if checkSeteLagoas:
                dfCadUnicoSeteLagoas = dfCadUnicoSeteLagoas[(dfCadUnicoSeteLagoas['val_renda_bruta_12_meses_memb'] / 12) > 477]

    return dfCadUnicoDivinopolis, dfCadUnicoOuroBranco, dfCadUnicoSaoJoaoDelRei, dfCadUnicoSeteLagoas

def GraficoRacas(checkBoxs, bases, configuracoes):
    #cod_raca_cor_pessoa
    #Cor ou raça
    #1 - Branca
    #2 - Preta
    #3 - Amarela
    #4 - Parda
    #5 - Indígena

    def filtraDados(df):
        data = [
                    {"value": None, "name": "Branca"},
                    {"value": None, "name": "Preta"},
                    {"value": None, "name": "Amarela"},
                    {"value": None, "name": "Parda"},
                    {"value": None, "name": "Indígena"}
                ]
        for i in range(1, 6):
            data[i-1]['value'] = len(df[df['cod_raca_cor_pessoa'] == i])
        return data

    # Verificar quais gráficos devem ser plotados e criar as opções para eles
    opcoes_graficos = []
    label = 'Raça/Cor'      
    flag = False  
    if checkBoxs[0]: # Divinopolis
        flag = True
        opcoes_graficos.append(("Divinópolis", label, filtraDados(bases[0]), configuracoes[2]))
    if checkBoxs[1]: # Ouro Branco
        flag = True
        opcoes_graficos.append(("Ouro Branco", label, filtraDados(bases[1]), configuracoes[2]))
    if checkBoxs[2]: # Sao Joao
        flag = True
        opcoes_graficos.append(("São João Del Rei", label, filtraDados(bases[2]), configuracoes[2]))
    if checkBoxs[3]: # Sete Lagoas
        flag = True
        opcoes_graficos.append(("Sete Lagoas", label, filtraDados(bases[3]), configuracoes[2]))
    
    if flag:
        st.header("Divisão de Raça/Cor da População")

    # Divida os gráficos em linhas, cada uma contendo um número máximo de gráficos por linha
    for i in range(0, len(opcoes_graficos), configuracoes[0]):
        linha = opcoes_graficos[i:i+configuracoes[0]]
        colunas = st.columns(len(linha))
        for j, (titulo, nome, dados, tipoGrafico) in enumerate(linha):
            with colunas[j]:
                st_echarts(options=CriarOpcoesGrafico(titulo, nome, dados, tipoGrafico), height=configuracoes[1])

def GraficoSexo(checkBoxs, bases, configuracoes):
    #cod_sexo_pessoa
    #Sexo
    #1 - Masculino
    #2 - Feminino

    def filtraDados(df):
        data = [
                    {"value": None, "name": "Masculino"},
                    {"value": None, "name": "Feminino"}
                ]
        for i in range(1, 3):
            data[i-1]['value'] = len(df[df['cod_sexo_pessoa'] == i])
        return data

    # Verificar quais gráficos devem ser plotados e criar as opções para eles
    opcoes_graficos = []
    label = 'Sexo'
    flag = False  
    if checkBoxs[0]: # Divinopolis
        flag = True
        opcoes_graficos.append(("Divinópolis", label, filtraDados(bases[0]), configuracoes[2]))
    if checkBoxs[1]: # Ouro Branco
        flag = True
        opcoes_graficos.append(("Ouro Branco", label, filtraDados(bases[1]), configuracoes[2]))
    if checkBoxs[2]: # Sao Joao
        flag = True
        opcoes_graficos.append(("São João Del Rei", label, filtraDados(bases[2]), configuracoes[2]))
    if checkBoxs[3]: # Sete Lagoas
        flag = True
        opcoes_graficos.append(("Sete Lagoas", label, filtraDados(bases[3]), configuracoes[2]))
    
    if flag:
        st.header("Divisão de Sexo da População")

    # Divida os gráficos em linhas, cada uma contendo um número máximo de gráficos por linha
    for i in range(0, len(opcoes_graficos), configuracoes[0]):
        linha = opcoes_graficos[i:i+configuracoes[0]]
        colunas = st.columns(len(linha))
        for j, (titulo, nome, dados, tipoGrafico) in enumerate(linha):
            with colunas[j]:
                st_echarts(options=CriarOpcoesGrafico(titulo, nome, dados, tipoGrafico), height=configuracoes[1])

def GraficoDeficiencia(checkBoxs, bases, configuracoes):
    #cod_deficiencia_memb
    #Pessoa tem deficiência?
    #1 - Sim
    #2 - Não
    
    def filtraDados(df):
        data = [
                    {"value": None, "name": "Possui Deficiência"},
                    {"value": None, "name": "Não Possui Deficiência"}
                ]
        for i in range(1, 3):
            data[i-1]['value'] = len(df[df['cod_deficiencia_memb'] == i])
        return data

    # Verificar quais gráficos devem ser plotados e criar as opções para eles
    opcoes_graficos = []
    label = 'Possui Deficiência?'
    flag = False  
    if checkBoxs[0]: # Divinopolis
        flag = True
        opcoes_graficos.append(("Divinópolis", label, filtraDados(bases[0]), configuracoes[2]))
    if checkBoxs[1]: # Ouro Branco
        flag = True
        opcoes_graficos.append(("Ouro Branco", label, filtraDados(bases[1]), configuracoes[2]))
    if checkBoxs[2]: # Sao Joao
        flag = True
        opcoes_graficos.append(("São João Del Rei", label, filtraDados(bases[2]), configuracoes[2]))
    if checkBoxs[3]: # Sete Lagoas
        flag = True
        opcoes_graficos.append(("Sete Lagoas", label, filtraDados(bases[3]), configuracoes[2]))
    
    if flag:
        st.header("Divisão de Deficiência da População")

    # Divida os gráficos em linhas, cada uma contendo um número máximo de gráficos por linha
    for i in range(0, len(opcoes_graficos), configuracoes[0]):
        linha = opcoes_graficos[i:i+configuracoes[0]]
        colunas = st.columns(len(linha))
        for j, (titulo, nome, dados, tipoGrafico) in enumerate(linha):
            with colunas[j]:
                st_echarts(options=CriarOpcoesGrafico(titulo, nome, dados, tipoGrafico), height=configuracoes[1])

def GraficoDistribuiçãoIdade(checkBoxs, bases, configuracoes):
    #idade
    #Idade calculada a partir da diferença entre a data de nascimento da pessoa e a data de referência da base
    #Dado inteiro de tamanho até 3

    def filtraDados(df):
        data = []
        if configuracoes[2] == 'Boxplot':
            data = [int(x) for x in df['idade']]
            return data
        else:
            idades = df['idade'].value_counts().sort_index()
            
            data.append([int(x) for x in idades.index])
            data.append([int(x) for x in idades.values])
            return data
    
    # Verificar quais gráficos devem ser plotados e criar as opções para eles
    opcoes_graficos = []
    label = 'Idade'
    flag = False  
    if checkBoxs[0]: # Divinopolis
        flag = True
        opcoes_graficos.append(("Divinópolis", label, filtraDados(bases[0]), configuracoes[2]))
    if checkBoxs[1]: # Ouro Branco
        flag = True
        opcoes_graficos.append(("Ouro Branco", label, filtraDados(bases[1]), configuracoes[2]))
    if checkBoxs[2]: # Sao Joao
        flag = True
        opcoes_graficos.append(("São João Del Rei", label, filtraDados(bases[2]), configuracoes[2]))
    if checkBoxs[3]: # Sete Lagoas
        flag = True
        opcoes_graficos.append(("Sete Lagoas", label, filtraDados(bases[3]), configuracoes[2]))
    
    if flag:
        st.header("Distribuição de Idade da População")
        st.text("Para visualizar melhor este gráfico, ajuste as configurações no menu lateral.")
    
    # Divida os gráficos em linhas, cada uma contendo um número máximo de gráficos por linha
    for i in range(0, len(opcoes_graficos), configuracoes[0]):
        linha = opcoes_graficos[i:i+configuracoes[0]]
        colunas = st.columns(len(linha))
        for j, (titulo, nome, dados, tipoGrafico) in enumerate(linha):
            with colunas[j]:
                options = CriarOpcoesGrafico(titulo, nome, dados, tipoGrafico)
                st_echarts(options=options, height=configuracoes[1])

def GraficoLerEEscrever(checkBoxs, bases, configuracoes):
    #cod_sabe_ler_escrever_memb
    #Pessoa sabe ler e escrever?
    #1 - Sim
    #2 - Não

    def filtraDados(df):
        data = [
                    {"value": None, "name": "Não é Analfabeto"},
                    {"value": None, "name": "É Analfabeto"}
                ]
        for i in range(1, 3):
            data[i-1]['value'] = len(df[df['cod_sabe_ler_escrever_memb'] == i])
        return data

    # Verificar quais gráficos devem ser plotados e criar as opções para eles
    opcoes_graficos = []
    label = 'É Analfabeto?'
    flag = False  
    if checkBoxs[0]: # Divinopolis
        flag = True
        opcoes_graficos.append(("Divinópolis", label, filtraDados(bases[0]), configuracoes[2]))
    if checkBoxs[1]: # Ouro Branco
        flag = True
        opcoes_graficos.append(("Ouro Branco", label, filtraDados(bases[1]), configuracoes[2]))
    if checkBoxs[2]: # Sao Joao
        flag = True
        opcoes_graficos.append(("São João Del Rei", label, filtraDados(bases[2]), configuracoes[2]))
    if checkBoxs[3]: # Sete Lagoas
        flag = True
        opcoes_graficos.append(("Sete Lagoas", label, filtraDados(bases[3]), configuracoes[2]))
    
    if flag:
        st.header("Analfabetismo na População")

    # Divida os gráficos em linhas, cada uma contendo um número máximo de gráficos por linha
    for i in range(0, len(opcoes_graficos), configuracoes[0]):
        linha = opcoes_graficos[i:i+configuracoes[0]]
        colunas = st.columns(len(linha))
        for j, (titulo, nome, dados, tipoGrafico) in enumerate(linha):
            with colunas[j]:
                st_echarts(options=CriarOpcoesGrafico(titulo, nome, dados, tipoGrafico), height=configuracoes[1])

def GraficoFrenquenciaEscola(checkBoxs, bases, configuracoes):
    #ind_frequenta_escola_memb
    #Pessoa frequenta escola?
    #1 - Sim, rede pública
    #2 - Sim, rede particular
    #3 - Não, já frequentou
    #4 - Nunca frequentou

    def filtraDados(df):
        data = [
                    {"value": None, "name": "Sim, Frequenta"},
                    {"value": None, "name": "Não, já frequentou"},
                    {"value": None, "name": "Nunca Frequentou"}
                ]
        
        data[0]['value'] = len(df[(df['ind_frequenta_escola_memb'] == 1) | (df['ind_frequenta_escola_memb'] == 2)])
        data[1]['value'] = len(df[df['ind_frequenta_escola_memb'] == 3])
        data[2]['value'] = len(df[df['ind_frequenta_escola_memb'] == 4])

        return data

    # Verificar quais gráficos devem ser plotados e criar as opções para eles
    opcoes_graficos = []
    label = 'Frequenta a Escola?'
    flag = False  
    if checkBoxs[0]: # Divinopolis
        flag = True
        opcoes_graficos.append(("Divinópolis", label, filtraDados(bases[0]), configuracoes[2]))
    if checkBoxs[1]: # Ouro Branco
        flag = True
        opcoes_graficos.append(("Ouro Branco", label, filtraDados(bases[1]), configuracoes[2]))
    if checkBoxs[2]: # Sao Joao
        flag = True
        opcoes_graficos.append(("São João Del Rei", label, filtraDados(bases[2]), configuracoes[2]))
    if checkBoxs[3]: # Sete Lagoas
        flag = True
        opcoes_graficos.append(("Sete Lagoas", label, filtraDados(bases[3]), configuracoes[2]))
    
    if flag:
        st.header("Frequência Escolar da População")

    # Divida os gráficos em linhas, cada uma contendo um número máximo de gráficos por linha
    for i in range(0, len(opcoes_graficos), configuracoes[0]):
        linha = opcoes_graficos[i:i+configuracoes[0]]
        colunas = st.columns(len(linha))
        for j, (titulo, nome, dados, tipoGrafico) in enumerate(linha):
            with colunas[j]:
                st_echarts(options=CriarOpcoesGrafico(titulo, nome, dados, tipoGrafico), height=configuracoes[1])

def GraficoEscolaPublicaParticular(checkBoxs, bases, configuracoes):
    #ind_frequenta_escola_memb
    #Pessoa frequenta escola?
    #1 - Sim, rede pública
    #2 - Sim, rede particular
    #3 - Não, já frequentou
    #4 - Nunca frequentou

    def filtraDados(df):
        data = [
                    {"value": None, "name": "Escola Pública"},
                    {"value": None, "name": "Escola Particular"}
                ]
        
        data[0]['value'] = len(df[df['ind_frequenta_escola_memb'] == 1])
        data[1]['value'] = len(df[df['ind_frequenta_escola_memb'] == 2])
    
        return data

    # Verificar quais gráficos devem ser plotados e criar as opções para eles
    opcoes_graficos = []
    label = 'Qual tipo de Escola?'
    flag = False  
    if checkBoxs[0]: # Divinopolis
        flag = True
        opcoes_graficos.append(("Divinópolis", label, filtraDados(bases[0]), configuracoes[2]))
    if checkBoxs[1]: # Ouro Branco
        flag = True
        opcoes_graficos.append(("Ouro Branco", label, filtraDados(bases[1]), configuracoes[2]))
    if checkBoxs[2]: # Sao Joao
        flag = True
        opcoes_graficos.append(("São João Del Rei", label, filtraDados(bases[2]), configuracoes[2]))
    if checkBoxs[3]: # Sete Lagoas
        flag = True
        opcoes_graficos.append(("Sete Lagoas", label, filtraDados(bases[3]), configuracoes[2]))
    
    if flag:
        st.header("Tipos de Escolas Frequentadas Pela População")

    # Divida os gráficos em linhas, cada uma contendo um número máximo de gráficos por linha
    for i in range(0, len(opcoes_graficos), configuracoes[0]):
        linha = opcoes_graficos[i:i+configuracoes[0]]
        colunas = st.columns(len(linha))
        for j, (titulo, nome, dados, tipoGrafico) in enumerate(linha):
            with colunas[j]:
                st_echarts(options=CriarOpcoesGrafico(titulo, nome, dados, tipoGrafico), height=configuracoes[1])

def GraficoNivelEscolar(checkBoxs, bases, configuracoes):
    #cod_curso_frequentou_pessoa_memb
    # Curso mais elevado que a pessoa frequentou
    #1 - Creche 2 - Pré-escola (exceto CA) 3 - Classe de Alfabetização - CA 4 - Ensino Fundamental 1ª a 4ª séries, Elementar (Primário), Primeira fase do 1º grau 5 - Ensino Fundamental 5ª a 8ª séries, Médio 1º ciclo (Ginasial), Segunda fase do 1º grau 6 - Ensino Fundamental (duração 9 anos) 7 - Ensino Fundamental Especial 8 - Ensino Médio, 2º grau, Médio 2º ciclo (Científico, Clássico, Técnico, Normal) 9 - Ensino Médio Especial 10 - Ensino Fundamental EJA - séries iniciais (Supletivo 1ª a 4ª) 11 - Ensino Fundamental EJA - séries finais (Supletivo 5ª a 8ª) 12 - Ensino Médio EJA (Supletivo) 13 - Superior, Aperfeiçoamento, Especialização, Mestrado, Doutorado 14 - Alfabetização para Adultos (Mobral, etc.) 15 - Nenhum
    def filtraDados(df):
        data = [
                    {"value": None, "name": "Fundamental 1"},
                    {"value": None, "name": "Fundamental 2"},
                    {"value": None, "name": "Ensino Médio"},
                    {"value": None, "name": "Ensino Superior"}
                ]
        data[0]['value'] = len(df[(df['cod_curso_frequentou_pessoa_memb'] == 4) | (df['cod_curso_frequentou_pessoa_memb'] == 10)])
        data[1]['value'] = len(df[(df['cod_curso_frequentou_pessoa_memb'] == 5) | (df['cod_curso_frequentou_pessoa_memb'] == 6) | (df['cod_curso_frequentou_pessoa_memb'] == 7) | (df['cod_curso_frequentou_pessoa_memb'] == 11)])
        data[2]['value'] = len(df[(df['cod_curso_frequentou_pessoa_memb'] == 8) | (df['cod_curso_frequentou_pessoa_memb'] == 9) | (df['cod_curso_frequentou_pessoa_memb'] == 12)])
        data[3]['value'] = len(df[df['cod_curso_frequentou_pessoa_memb'] == 13]) 
        return data

    # Verificar quais gráficos devem ser plotados e criar as opções para eles
    opcoes_graficos = []
    label = 'Nível Escolar Mais Alto'
    flag = False  
    if checkBoxs[0]: # Divinopolis
        flag = True
        opcoes_graficos.append(("Divinópolis", label, filtraDados(bases[0]), configuracoes[2]))
    if checkBoxs[1]: # Ouro Branco
        flag = True
        opcoes_graficos.append(("Ouro Branco", label, filtraDados(bases[1]), configuracoes[2]))
    if checkBoxs[2]: # Sao Joao
        flag = True
        opcoes_graficos.append(("São João Del Rei", label, filtraDados(bases[2]), configuracoes[2]))
    if checkBoxs[3]: # Sete Lagoas
        flag = True
        opcoes_graficos.append(("Sete Lagoas", label, filtraDados(bases[3]), configuracoes[2]))
    
    if flag:
        st.header("Maior Nível Escolar Frequentado Pela População")

    # Divida os gráficos em linhas, cada uma contendo um número máximo de gráficos por linha
    for i in range(0, len(opcoes_graficos), configuracoes[0]):
        linha = opcoes_graficos[i:i+configuracoes[0]]
        colunas = st.columns(len(linha))
        for j, (titulo, nome, dados, tipoGrafico) in enumerate(linha):
            with colunas[j]:
                st_echarts(options=CriarOpcoesGrafico(titulo, nome, dados, tipoGrafico), height=configuracoes[1])

def GraficoConclusaoCurso(checkBoxs, bases, configuracoes):
    #cod_concluiu_frequentou_memb
    #A pessoa concluiu o curso?
    #1 - Sim
    #2 - Não

    def filtraDados(df):
        data = [
                    {"value": None, "name": "Sim, Concluiu o Curso"},
                    {"value": None, "name": "Não Concluiu o Curso"}
                ]
        for i in range(1, 3):
            data[i-1]['value'] = len(df[df['cod_concluiu_frequentou_memb'] == i])
        return data

    # Verificar quais gráficos devem ser plotados e criar as opções para eles
    opcoes_graficos = []
    label = 'Concluiu o Curso?'
    flag = False  
    if checkBoxs[0]: # Divinopolis
        flag = True
        opcoes_graficos.append(("Divinópolis", label, filtraDados(bases[0]), configuracoes[2]))
    if checkBoxs[1]: # Ouro Branco
        flag = True
        opcoes_graficos.append(("Ouro Branco", label, filtraDados(bases[1]), configuracoes[2]))
    if checkBoxs[2]: # Sao Joao
        flag = True
        opcoes_graficos.append(("São João Del Rei", label, filtraDados(bases[2]), configuracoes[2]))
    if checkBoxs[3]: # Sete Lagoas
        flag = True
        opcoes_graficos.append(("Sete Lagoas", label, filtraDados(bases[3]), configuracoes[2]))
    
    if flag:
        st.header("Taxa de Conclusão do Maior Nível de Escolaridade da População")

    # Divida os gráficos em linhas, cada uma contendo um número máximo de gráficos por linha
    for i in range(0, len(opcoes_graficos), configuracoes[0]):
        linha = opcoes_graficos[i:i+configuracoes[0]]
        colunas = st.columns(len(linha))
        for j, (titulo, nome, dados, tipoGrafico) in enumerate(linha):
            with colunas[j]:
                st_echarts(options=CriarOpcoesGrafico(titulo, nome, dados, tipoGrafico), height=configuracoes[1])

def GraficoFormaDeEnsino(checkBoxs, bases, configuracoes):
    #cod_curso_frequentou_pessoa_memb
    # Curso mais elevado que a pessoa frequentou
    #1 - Creche 2 - Pré-escola (exceto CA) 3 - Classe de Alfabetização - CA 4 - Ensino Fundamental 1ª a 4ª séries, Elementar (Primário), Primeira fase do 1º grau 5 - Ensino Fundamental 5ª a 8ª séries, Médio 1º ciclo (Ginasial), Segunda fase do 1º grau 6 - Ensino Fundamental (duração 9 anos) 7 - Ensino Fundamental Especial 8 - Ensino Médio, 2º grau, Médio 2º ciclo (Científico, Clássico, Técnico, Normal) 9 - Ensino Médio Especial 10 - Ensino Fundamental EJA - séries iniciais (Supletivo 1ª a 4ª) 11 - Ensino Fundamental EJA - séries finais (Supletivo 5ª a 8ª) 12 - Ensino Médio EJA (Supletivo) 13 - Superior, Aperfeiçoamento, Especialização, Mestrado, Doutorado 14 - Alfabetização para Adultos (Mobral, etc.) 15 - Nenhum
    def filtraDados(df):
        data = [
                    {"value": None, "name": "Ensino Normal"},
                    {"value": None, "name": "Ensino Especial"},
                    {"value": None, "name": "Ensino EJA"},
                ]
        data[0]['value'] = len(df[(df['cod_curso_frequentou_pessoa_memb'] == 3) | (df['cod_curso_frequentou_pessoa_memb'] == 4) | (df['cod_curso_frequentou_pessoa_memb'] == 5) | (df['cod_curso_frequentou_pessoa_memb'] == 6) | (df['cod_curso_frequentou_pessoa_memb'] == 8) | (df['cod_curso_frequentou_pessoa_memb'] == 13)])
        data[1]['value'] = len(df[(df['cod_curso_frequentou_pessoa_memb'] == 7) | (df['cod_curso_frequentou_pessoa_memb'] == 9) | (df['cod_curso_frequentou_pessoa_memb'] == 14)])
        data[2]['value'] = len(df[(df['cod_curso_frequentou_pessoa_memb'] == 10) | (df['cod_curso_frequentou_pessoa_memb'] == 11) | (df['cod_curso_frequentou_pessoa_memb'] == 12)])

        return data

    # Verificar quais gráficos devem ser plotados e criar as opções para eles
    opcoes_graficos = []
    label = 'Tipo de Ensino'
    flag = False  
    if checkBoxs[0]: # Divinopolis
        flag = True
        opcoes_graficos.append(("Divinópolis", label, filtraDados(bases[0]), configuracoes[2]))
    if checkBoxs[1]: # Ouro Branco
        flag = True
        opcoes_graficos.append(("Ouro Branco", label, filtraDados(bases[1]), configuracoes[2]))
    if checkBoxs[2]: # Sao Joao
        flag = True
        opcoes_graficos.append(("São João Del Rei", label, filtraDados(bases[2]), configuracoes[2]))
    if checkBoxs[3]: # Sete Lagoas
        flag = True
        opcoes_graficos.append(("Sete Lagoas", label, filtraDados(bases[3]), configuracoes[2]))
    
    if flag:
        st.header("Forma de Ensino Utilizada Pela População")

    # Divida os gráficos em linhas, cada uma contendo um número máximo de gráficos por linha
    for i in range(0, len(opcoes_graficos), configuracoes[0]):
        linha = opcoes_graficos[i:i+configuracoes[0]]
        colunas = st.columns(len(linha))
        for j, (titulo, nome, dados, tipoGrafico) in enumerate(linha):
            with colunas[j]:
                st_echarts(options=CriarOpcoesGrafico(titulo, nome, dados, tipoGrafico), height=configuracoes[1])

def GraficoFuncaoTrabalho(checkBoxs, bases, configuracoes):
    #cod_principal_trab_memb
    # Função principal
    #1 - Trabalhador por conta própria (bico, autônomo) 2 - Trabalhador temporário em área rural 3 - Empregado sem carteira de trabalho assinada 
    #4 - Empregado com carteira de trabalho assinada 5 - Trabalhador doméstico sem carteira de trabalho assinada 
    #6 - Trabalhador doméstico com carteira de trabalho assinada 
    #7 - Trabalhador não-remunerado 8 - Militar ou servidor público 9 - Empregador 10 - Estagiário 11 - Aprendiz

    def filtraDados(df):
        data = [
                    {"value": None, "name": "Trabalhador por conta própria (bico, autônomo)"},
                    {"value": None, "name": "Trabalhador temporário em área rural"},
                    {"value": None, "name": "Empregado sem carteira de trabalho assinada"},
                    {"value": None, "name": "Empregado com carteira de trabalho assinada"},
                    {"value": None, "name": "Trabalhador doméstico sem carteira de trabalho assinada"},
                    {"value": None, "name": "Trabalhador doméstico com carteira de trabalho assinada"},
                    {"value": None, "name": "Trabalhador não-remunerado"},
                    {"value": None, "name": "Militar ou servidor público"},
                    {"value": None, "name": "Empregador"},
                    {"value": None, "name": "Estagiário"},
                    {"value": None, "name": "Aprendiz"}
                ]
        for i in range(1, 12):
            data[i-1]['value'] = len(df[df['cod_principal_trab_memb'] == i])
        return data

    # Verificar quais gráficos devem ser plotados e criar as opções para eles
    opcoes_graficos = []
    label = 'Função Principal do Trabalho'
    flag = False  
    if checkBoxs[0]: # Divinopolis
        flag = True
        opcoes_graficos.append(("Divinópolis", label, filtraDados(bases[0]), configuracoes[2]))
    if checkBoxs[1]: # Ouro Branco
        flag = True
        opcoes_graficos.append(("Ouro Branco", label, filtraDados(bases[1]), configuracoes[2]))
    if checkBoxs[2]: # Sao Joao
        flag = True
        opcoes_graficos.append(("São João Del Rei", label, filtraDados(bases[2]), configuracoes[2]))
    if checkBoxs[3]: # Sete Lagoas
        flag = True
        opcoes_graficos.append(("Sete Lagoas", label, filtraDados(bases[3]), configuracoes[2]))
    
    if flag:
        st.header("Funções Principais da População Com Trabalho")
        st.text("Para visualizar melhor este gráfico, ajuste as configurações no menu lateral.")

    # Divida os gráficos em linhas, cada uma contendo um número máximo de gráficos por linha
    for i in range(0, len(opcoes_graficos), configuracoes[0]):
        linha = opcoes_graficos[i:i+configuracoes[0]]
        colunas = st.columns(len(linha))
        for j, (titulo, nome, dados, tipoGrafico) in enumerate(linha):
            with colunas[j]:
                st_echarts(options=CriarOpcoesGrafico(titulo, nome, dados, tipoGrafico), height=configuracoes[1])

def GraficoFaixaRenda(checkBoxs, bases, configuracoes):
    #val_renda_bruta_12_meses_memb
        #Valor de remuneração bruta no formato NNNNN (sem casas decimais). Ex. Uma remuneração de R$ 125,00 constará na base como 125. 
    def filtraDados(df):
        data = [
                    {"value": None, "name": "R$0,00 à R$85,00"},
                    {"value": None, "name": "R$85,01 à R$170,00"},
                    {"value": None, "name": "R$170,01 à R$477,00"},
                    {"value": None, "name": "À Partir de R$477,01"}
                ]
        data[0]['value'] = len(df[(df['val_renda_bruta_12_meses_memb'] / 12) <= 85])
        data[1]['value'] = len(df[((df['val_renda_bruta_12_meses_memb'] / 12) > 85) & ((df['val_renda_bruta_12_meses_memb'] / 12) <= 170)])
        data[2]['value'] = len(df[((df['val_renda_bruta_12_meses_memb'] / 12) > 170) & ((df['val_renda_bruta_12_meses_memb'] / 12) <= 477)])
        data[3]['value'] = len(df[(df['val_renda_bruta_12_meses_memb'] / 12) > 477])

        return data

    # Verificar quais gráficos devem ser plotados e criar as opções para eles
    opcoes_graficos = []
    label = 'Remuneração'
    flag = False  
    if checkBoxs[0]: # Divinopolis
        flag = True
        opcoes_graficos.append(("Divinópolis", label, filtraDados(bases[0]), configuracoes[2]))
    if checkBoxs[1]: # Ouro Branco
        flag = True
        opcoes_graficos.append(("Ouro Branco", label, filtraDados(bases[1]), configuracoes[2]))
    if checkBoxs[2]: # Sao Joao
        flag = True
        opcoes_graficos.append(("São João Del Rei", label, filtraDados(bases[2]), configuracoes[2]))
    if checkBoxs[3]: # Sete Lagoas
        flag = True
        opcoes_graficos.append(("Sete Lagoas", label, filtraDados(bases[3]), configuracoes[2]))
    
    if flag:
        st.header("Porcentagem de Remuneração Mensal da População")
        st.text("Para visualizar melhor este gráfico, ajuste as configurações no menu lateral.")
    
    # Divida os gráficos em linhas, cada uma contendo um número máximo de gráficos por linha
    for i in range(0, len(opcoes_graficos), configuracoes[0]):
        linha = opcoes_graficos[i:i+configuracoes[0]]
        colunas = st.columns(len(linha))
        for j, (titulo, nome, dados, tipoGrafico) in enumerate(linha):
            with colunas[j]:
                st_echarts(options=CriarOpcoesGrafico(titulo, nome, dados, tipoGrafico), height=configuracoes[1])

def GraficoTrabalho12Meses(checkBoxs, bases, configuracoes):
    #cod_trabalho_12_meses_memb
    #Pessoa com trabalho remunerado em algum período nos último 12 meses
    #1 - Sim
    #2 - Não
    def filtraDados(df):
        data = [
                    {"value": None, "name": "Sim, Trabalhou"},
                    {"value": None, "name": "Não Trabalhou"}
                ]
        
        data[0]['value'] = len(df[df['ind_frequenta_escola_memb'] == 1])
        data[1]['value'] = len(df[df['ind_frequenta_escola_memb'] == 2])
    
        return data

    # Verificar quais gráficos devem ser plotados e criar as opções para eles
    opcoes_graficos = []
    label = 'Trabalhou de Forma Remunerada nos Últimos 12 Meses?'
    flag = False
    flag = False  
    if checkBoxs[0]: # Divinopolis
        flag = True
        opcoes_graficos.append(("Divinópolis", label, filtraDados(bases[0]), configuracoes[2]))
    if checkBoxs[1]: # Ouro Branco
        flag = True
        opcoes_graficos.append(("Ouro Branco", label, filtraDados(bases[1]), configuracoes[2]))
    if checkBoxs[2]: # Sao Joao
        flag = True
        opcoes_graficos.append(("São João Del Rei", label, filtraDados(bases[2]), configuracoes[2]))
    if checkBoxs[3]: # Sete Lagoas
        flag = True
        opcoes_graficos.append(("Sete Lagoas", label, filtraDados(bases[3]), configuracoes[2]))
    
    if flag:
        st.header("Trabalho Remunerado na População nos Últimos 12 Meses")

    # Divida os gráficos em linhas, cada uma contendo um número máximo de gráficos por linha
    for i in range(0, len(opcoes_graficos), configuracoes[0]):
        linha = opcoes_graficos[i:i+configuracoes[0]]
        colunas = st.columns(len(linha))
        for j, (titulo, nome, dados, tipoGrafico) in enumerate(linha):
            with colunas[j]:
                st_echarts(options=CriarOpcoesGrafico(titulo, nome, dados, tipoGrafico), height=configuracoes[1])

def TabelaPCDaS(dfPolisPCDaSUFSJ, checkDivinopolis, checkOuroBranco, checkSaoJoaoDelRei, checkSeteLagoas):
    #Montando os dados da tabela
    populacao_2019 = dfPolisPCDaSUFSJ['POPULACAO_2019'].apply(lambda x: '{:,.0f}'.format(x).replace('.', '|').replace(',', '.').replace('|', ',')).tolist()
    qtd_NASC_2019 = dfPolisPCDaSUFSJ['qtd_NASC_2019'].apply(lambda x: '{:,.0f}'.format(x).replace('.', '|').replace(',', '.').replace('|', ',')).tolist()
    tx_nasc_mae_10_14_2019 = dfPolisPCDaSUFSJ['tx_nasc_mae_10_14_2019'].apply(lambda x: '{:,.2f}'.format(x).replace('.', '|').replace(',', '.').replace('|', ',')).tolist()
    tx_nasc_mae_15_17_2019 = dfPolisPCDaSUFSJ['tx_nasc_mae_15_17_2019'].apply(lambda x: '{:,.2f}'.format(x).replace('.', '|').replace(',', '.').replace('|', ',')).tolist()
    qtd_OBITOS_2019 = dfPolisPCDaSUFSJ['qtd_OBITOS_2019'].apply(lambda x: '{:,.0f}'.format(x).replace('.', '|').replace(',', '.').replace('|', ',')).tolist()
    tx_obitos_2019 = dfPolisPCDaSUFSJ['tx_obitos_2019'].apply(lambda x: '{:,.2f}'.format(x).replace('.', '|').replace(',', '.').replace('|', ',')).tolist()
    tx_obitos_homicidio_2019 = dfPolisPCDaSUFSJ['tx_obitos_homicidio_2019'].apply(lambda x: '{:,.2f}'.format(x).replace('.', '|').replace(',', '.').replace('|', ',')).tolist()
    tx_obitos_suicidio_2019 = dfPolisPCDaSUFSJ['tx_obitos_suicidio_2019'].apply(lambda x: '{:,.2f}'.format(x).replace('.', '|').replace(',', '.').replace('|', ',')).tolist()
    tx_obitos_maternos_diretos_2019 = dfPolisPCDaSUFSJ['qtd_OBITOS_2019'].apply(lambda x: '{:,.2f}'.format(x).replace('.', '|').replace(',', '.').replace('|', ',')).tolist()
    qtd_INTERNACOES_2019 = dfPolisPCDaSUFSJ['qtd_INTERNACOES_2019'].apply(lambda x: '{:,.0f}'.format(x).replace('.', '|').replace(',', '.').replace('|', ',')).tolist()
    tx_interdrsai_2019 = dfPolisPCDaSUFSJ['tx_interdrsai_2019'].apply(lambda x: '{:,.2f}'.format(x).replace('.', '|').replace(',', '.').replace('|', ',')).tolist()
    tx_intersap_2019 = dfPolisPCDaSUFSJ['tx_intersap_2019'].apply(lambda x: '{:,.2f}'.format(x).replace('.', '|').replace(',', '.').replace('|', ',')).tolist()

    tabela = {
                'Cidade': [],
                'População': [],
                'Nascidos vivos': [],
                'Percentual de Mães 10-14 anos': [],
                'Percentual de Mães 15-17 anos': [],
                'Óbitos': [],
                'Percentual de óbitos': [],
                'Percentual de homicídios': [],
                'Número de suicídios': [],
                'Número de óbitos maternos': [],            
                'Internações hospitalares': [],
                'Percentual de internações atenção primária': [],
                'Percentual de internações saneamento': []
             }
    
    flag = False
    if checkDivinopolis:
        tabela['Cidade'].append('Divinópolis')
        tabela['População'].append(populacao_2019[0])
        tabela['Nascidos vivos'].append(qtd_NASC_2019[0])
        tabela['Percentual de Mães 10-14 anos'].append(tx_nasc_mae_10_14_2019[0])
        tabela['Percentual de Mães 15-17 anos'].append(tx_nasc_mae_15_17_2019[0])
        tabela['Óbitos'].append(qtd_OBITOS_2019[0])
        tabela['Percentual de óbitos'].append(tx_obitos_2019[0])
        tabela['Percentual de homicídios'].append(tx_obitos_homicidio_2019[0])
        tabela['Número de suicídios'].append(tx_obitos_suicidio_2019[0])
        tabela['Número de óbitos maternos'].append(tx_obitos_maternos_diretos_2019[0])
        tabela['Internações hospitalares'].append(qtd_INTERNACOES_2019[0])
        tabela['Percentual de internações atenção primária'].append(tx_interdrsai_2019[0])
        tabela['Percentual de internações saneamento'].append(tx_intersap_2019[0])
        flag = True

    if checkOuroBranco:
        tabela['Cidade'].append('Ouro Branco')
        tabela['População'].append(populacao_2019[1])
        tabela['Nascidos vivos'].append(qtd_NASC_2019[1])
        tabela['Percentual de Mães 10-14 anos'].append(tx_nasc_mae_10_14_2019[1])
        tabela['Percentual de Mães 15-17 anos'].append(tx_nasc_mae_15_17_2019[1])
        tabela['Óbitos'].append(qtd_OBITOS_2019[1])
        tabela['Percentual de óbitos'].append(tx_obitos_2019[1])
        tabela['Percentual de homicídios'].append(tx_obitos_homicidio_2019[1])
        tabela['Número de suicídios'].append(tx_obitos_suicidio_2019[1])
        tabela['Número de óbitos maternos'].append(tx_obitos_maternos_diretos_2019[1])
        tabela['Internações hospitalares'].append(qtd_INTERNACOES_2019[1])
        tabela['Percentual de internações atenção primária'].append(tx_interdrsai_2019[1])
        tabela['Percentual de internações saneamento'].append(tx_intersap_2019[1])
        flag = True

    if checkSaoJoaoDelRei:
        tabela['Cidade'].append('São João del Rei')
        tabela['População'].append(populacao_2019[2])
        tabela['Nascidos vivos'].append(qtd_NASC_2019[2])
        tabela['Percentual de Mães 10-14 anos'].append(tx_nasc_mae_10_14_2019[2])
        tabela['Percentual de Mães 15-17 anos'].append(tx_nasc_mae_15_17_2019[2])
        tabela['Óbitos'].append(qtd_OBITOS_2019[2])
        tabela['Percentual de óbitos'].append(tx_obitos_2019[2])
        tabela['Percentual de homicídios'].append(tx_obitos_homicidio_2019[2])
        tabela['Número de suicídios'].append(tx_obitos_suicidio_2019[2])
        tabela['Número de óbitos maternos'].append(tx_obitos_maternos_diretos_2019[2])
        tabela['Internações hospitalares'].append(qtd_INTERNACOES_2019[2])
        tabela['Percentual de internações atenção primária'].append(tx_interdrsai_2019[2])
        tabela['Percentual de internações saneamento'].append(tx_intersap_2019[2])
        flag = True

    if checkSeteLagoas:
        tabela['Cidade'].append('Sete Lagoas')
        tabela['População'].append(populacao_2019[3])
        tabela['Nascidos vivos'].append(qtd_NASC_2019[3])
        tabela['Percentual de Mães 10-14 anos'].append(tx_nasc_mae_10_14_2019[3])
        tabela['Percentual de Mães 15-17 anos'].append(tx_nasc_mae_15_17_2019[3])
        tabela['Óbitos'].append(qtd_OBITOS_2019[3])
        tabela['Percentual de óbitos'].append(tx_obitos_2019[3])
        tabela['Percentual de homicídios'].append(tx_obitos_homicidio_2019[3])
        tabela['Número de suicídios'].append(tx_obitos_suicidio_2019[3])
        tabela['Número de óbitos maternos'].append(tx_obitos_maternos_diretos_2019[3])
        tabela['Internações hospitalares'].append(qtd_INTERNACOES_2019[3])
        tabela['Percentual de internações atenção primária'].append(tx_interdrsai_2019[3])
        tabela['Percentual de internações saneamento'].append(tx_intersap_2019[3])
        flag = True

    if flag:
        tabela['Cidade'].append('Descrição')
        tabela['População'].append('População para o ano de 2019')
        tabela['Nascidos vivos'].append('Quantidade de nascidos vivos para o ano de 2019')
        tabela['Percentual de Mães 10-14 anos'].append('Participação percentual de meninas de 10 a 14 anos (inclusive) que tiveram filhos nascidos vivos no total de nascidos vivos para o ano de 2019')
        tabela['Percentual de Mães 15-17 anos'].append('Participação percentual de adolescentes de 15 a 17 anos (inclusive) que tiveram filhos nascidos vivos no total nascidos vivos para o ano de 2019')
        tabela['Óbitos'].append('Quantidade de óbitos para o ano de 2019')
        tabela['Percentual de óbitos'].append('Percentual do total de óbitos no total da população para o ano de 2019')
        tabela['Percentual de homicídios'].append('Percentual de óbitos por homicídio no total da população para o ano de 2019')
        tabela['Número de suicídios'].append('Número de óbitos por suicídio, por 100.000 habitantes para o ano de 2019')
        tabela['Número de óbitos maternos'].append('Número de óbitos maternos diretos, por 100.000 nascidos vivos para o ano de 2019')
        tabela['Internações hospitalares'].append('Quantidade de internações hospitalares no ano de 2019')
        tabela['Percentual de internações atenção primária'].append('Participação percentual de internações hospitalares por condições sensíveis à atenção primária no total de internações hospitalares no ano de 2019')
        tabela['Percentual de internações saneamento'].append('Participação percentual de internações hospitalares por doenças relacionadas ao saneamento ambiental inadequado no total de internações hospitalares no ano de 2019')
    
        df = pd.DataFrame(tabela)
        
        # Definindo a coluna 'Cidade' como índice do DataFrame
        df.set_index('Cidade', inplace=True)
        
        df_invertido = df.transpose()
        
        st.header('Dados da Saúde Pólis PCDaS')
        st.text('Dados de saúde e socioeconômicos municipais reunidos e construídos pela Plataforma de Ciência de Dados aplicada à Saúde (PCDaS)')
        # Exibindo a tabela no Streamlit
        st.dataframe(df_invertido)

# NOVAS FUNÇÕES PARA MAPAS INTERATIVOS
def MapaInterativoUFSJ(dfPolisPCDaSUFSJ):
    """
    Cria um mapa interativo com as cidades da UFSJ
    """
    st.header("Mapa Interativo")
    
    # Criar o mapa centralizado em Minas Gerais
    mapa = folium.Map(
        location=[-20, -44],  # Coordenadas aproximadas do centro de MG
        zoom_start=8,
        tiles='OpenStreetMap'
    )
    
    # Dados das cidades
    cidades_ufsj = {
        'Divinópolis': {'lat': -20.139, 'lon': -44.884, 'pop': 238230},
        'Ouro Branco': {'lat': -20.521, 'lon': -43.692, 'pop': 39500},
        'São João del Rei': {'lat': -21.136, 'lon': -44.262, 'pop': 90082},
        'Sete Lagoas': {'lat': -19.466, 'lon': -44.247, 'pop': 239639}
    }
    
    # Adicionar marcadores para cada cidade
    for cidade, info in cidades_ufsj.items():
        # Buscar dados específicos da cidade no DataFrame
        cidade_data = dfPolisPCDaSUFSJ[dfPolisPCDaSUFSJ['mun_MUNNOME'] == cidade].iloc[0]
        
        # Criar popup com informações
        popup_text = f"""
        <b>{cidade}</b><br>
        <b>População (2019):</b> {info['pop']:,}<br>
        <b>Nascidos vivos (2019):</b> {cidade_data['qtd_NASC_2019']:,}<br>
        <b>Óbitos (2019):</b> {cidade_data['qtd_OBITOS_2019']:,}<br>
        <b>Internações (2019):</b> {cidade_data['qtd_INTERNACOES_2019']:,}<br>
        <b>Taxa de homicídios:</b> {cidade_data['tx_obitos_homicidio_2019']:.2f}<br>
        <b>Mães 15-17 anos:</b> {cidade_data['tx_nasc_mae_15_17_2019']:.2f}%
        """
        
        # Adicionar marcador ao mapa
        folium.Marker(
            location=[info['lat'], info['lon']],
            popup=folium.Popup(popup_text, max_width=300),
            tooltip=f"Clique para ver dados de {cidade}",
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(mapa)
    
    # Adicionar camada de calor baseada na população
    from folium.plugins import HeatMap
    
    heat_data = []
    for cidade, info in cidades_ufsj.items():
        cidade_data = dfPolisPCDaSUFSJ[dfPolisPCDaSUFSJ['mun_MUNNOME'] == cidade].iloc[0]
        heat_data.append([info['lat'], info['lon'], info['pop']/1000])  # Normalizar população
    
    HeatMap(heat_data, 
            name='Densidade Populacional', 
            min_opacity=0.3,
            max_zoom=10,
            radius=25,
            blur=15,
            gradient={0.4: 'blue', 0.65: 'lime', 1: 'red'}).add_to(mapa)
    
    # Adicionar controle de camadas
    folium.LayerControl().add_to(mapa)
    
    # Exibir o mapa no Streamlit
    st_folium(mapa, width=800, height=600)
    
    # Legenda e explicações
    st.markdown("""
    **Legenda do Mapa:**
    - **Marcadores azuis**: Clique para ver dados detalhados de cada cidade
    - **Mapa de calor**: Mostra a densidade populacional (vermelho = maior população)
    
    **Dados mostrados:**
    - População total (2019)
    - Nascidos vivos
    - Óbitos totais
    - Internações hospitalares
    - Taxa de homicídios
    - Percentual de mães adolescentes (15-17 anos)
    """)

def MapaComparativoSaude(dfPolisPCDaSUFSJ):
    """
    Cria um mapa comparativo focado em indicadores de saúde
    """
    st.header("Mapa Comparativo - Indicadores de Saúde")
    
    # Selecionar indicador para comparar
    indicadores = {
        'Taxa de Mortalidade Infantil': 'tx_mortalidade_infantil_2019',
        'Taxa de Óbitos': 'tx_obitos_2019',
        'Taxa de Homicídios': 'tx_obitos_homicidio_2019',
        'Taxa de Suicídios': 'tx_obitos_suicidio_2019',
        'Internações por Atenção Primária': 'tx_interdrsai_2019',
        'Mães Adolescentes (15-17 anos)': 'tx_nasc_mae_15_17_2019'
    }
    
    indicador_selecionado = st.selectbox(
        "Selecione o indicador de saúde para visualizar:",
        list(indicadores.keys())
    )
    
    coluna_indicador = indicadores[indicador_selecionado]
    
    # Criar mapa
    mapa_saude = folium.Map(
        location=[-20, -44],
        zoom_start=8
    )
    
    cidades_ufsj = {
        'Divinópolis': {'lat': -20.139, 'lon': -44.884},
        'Ouro Branco': {'lat': -20.521, 'lon': -43.692},
        'São João del Rei': {'lat': -21.136, 'lon': -44.262},
        'Sete Lagoas': {'lat': -19.466, 'lon': -44.247}
    }
    
    # Adicionar círculos proporcionais ao indicador
    for cidade, coord in cidades_ufsj.items():
        cidade_data = dfPolisPCDaSUFSJ[dfPolisPCDaSUFSJ['mun_MUNNOME'] == cidade].iloc[0]
        valor_indicador = cidade_data[coluna_indicador]
        
        # Tamanho do círculo baseado no valor do indicador
        raio = max(valor_indicador * 2, 10)  # Ajuste de escala
        
        popup_text = f"""
        <b>{cidade}</b><br>
        <b>{indicador_selecionado}:</b> {valor_indicador:.2f}<br>
        <b>População:</b> {cidade_data['POPULACAO_2019']:,}
        """
        
        folium.CircleMarker(
            location=[coord['lat'], coord['lon']],
            radius=raio,
            popup=folium.Popup(popup_text, max_width=300),
            tooltip=f"{cidade}: {valor_indicador:.2f}",
            color='crimson',
            fill=True,
            fillOpacity=0.6
        ).add_to(mapa_saude)
    
    st_folium(mapa_saude, width=800, height=600)
    
    # Tabela comparativa
    st.subheader("Comparativo de Indicadores")
    dados_comparativos = []
    for cidade in cidades_ufsj.keys():
        cidade_data = dfPolisPCDaSUFSJ[dfPolisPCDaSUFSJ['mun_MUNNOME'] == cidade].iloc[0]
        dados_comparativos.append({
            'Cidade': cidade,
            'População': cidade_data['POPULACAO_2019'],
            indicador_selecionado: cidade_data[coluna_indicador],
            'Nascidos Vivos': cidade_data['qtd_NASC_2019'],
            'Óbitos Totais': cidade_data['qtd_OBITOS_2019']
        })
    
    df_comparativo = pd.DataFrame(dados_comparativos)
    st.dataframe(df_comparativo)

def main():
    dfCadUnicoDivinopolis = pd.read_csv('CadUnicoDivinopolis.csv')
    dfCadUnicoOuroBranco = pd.read_csv('CadUnicoOuroBranco.csv')
    dfCadUnicoSaoJoaoDelRei = pd.read_csv('CadUnicoSaoJoaoDelRei.csv')
    dfCadUnicoSeteLagoas = pd.read_csv('CadUnicoSeteLagoas.csv')
    dfPolisPCDaSUFSJ = pd.read_csv('PolisPCDaSUFSJ.csv')

    #Substituindo os NaNs da coluna por 0
    dfCadUnicoDivinopolis['val_renda_bruta_12_meses_memb'] = dfCadUnicoDivinopolis['val_renda_bruta_12_meses_memb'].fillna(0)
    dfCadUnicoOuroBranco['val_renda_bruta_12_meses_memb'] = dfCadUnicoOuroBranco['val_renda_bruta_12_meses_memb'].fillna(0)
    dfCadUnicoSaoJoaoDelRei['val_renda_bruta_12_meses_memb'] = dfCadUnicoSaoJoaoDelRei['val_renda_bruta_12_meses_memb'].fillna(0)
    dfCadUnicoSeteLagoas['val_renda_bruta_12_meses_memb'] = dfCadUnicoSeteLagoas['val_renda_bruta_12_meses_memb'].fillna(0)

    st.set_page_config(
        page_title="CadUnico UFSJ",
        page_icon="📊",
        initial_sidebar_state="expanded",
        layout="wide",
        menu_items={
                    'Get Help': 'https://www.extremelycoolapp.com/help',
                    'Report a bug': "https://www.extremelycoolapp.com/bug",
                    'About': "# This is a header. This is an *extremely* cool app!"
                    }
    )

    with st.sidebar:
        st.markdown("<h1 style='text-align: center;'>Filtros</h1>", unsafe_allow_html=True)
        st.text("Marque as cidades que deseja ver:")
        
        checkDivinopolis = st.checkbox("Divinópolis", value=False)
        checkOuroBranco = st.checkbox("Ouro Branco", value=False)
        checkSaoJoaoDelRei = st.checkbox("São João Del Rei", value=True)
        checkSeteLagoas = st.checkbox("Sete Lagoas", value=False)

        st.text("Marque os temas que deseja ver:")
        checkDadosGerais = st.checkbox("Dados Gerais", value=True)
        checkEducacao = st.checkbox("Educação")
        checkRendaFinanceira = st.checkbox("Renda Financeira")
        checkSaude = st.checkbox("Saúde")
        
        # NOVA SEÇÃO PARA MAPAS
        st.markdown("---")
        st.markdown("###  Visualização Geográfica")
        checkMapaInterativo = st.checkbox("Mapa Interativo UFSJ", value=True)
        checkMapaSaude = st.checkbox("Mapa Comparativo de Saúde")

        st.text("Marque os filtros que deseja aplicar aos dados:")
        with st.expander("Sexo"):
            filtroSexo = st.radio("Qual filtro você deseja aplicar?", ['Sem Filtro', 'Feminino', 'Masculino'])

        with st.expander("Raça/Cor"):
            filtroRaca = st.radio("Qual filtro você deseja aplicar?", ['Sem Filtro', 'Branca', 'Preta', 'Amarela', 'Parda', 'Indígena'])

        with st.expander("Deficiência"):
            filtroDeficiencia = st.radio("Qual filtro você deseja aplicar?", ['Sem Filtro', 'Não Possui Deficiência', 'Possui Deficiência'])

        with st.expander("Idade"):
            filtroIdade = st.radio("Qual faixa de idade você deseja aplicar?", ['Sem Filtro', 'Primeira Infância (0-5 anos)', 'Segunda Infância (6-12 years)', 'Adolescência Inicial (13-15 anos)', 'Adolescência Tardia (16-18 anos)', 'Juventude Inicial (19-24 anos)', 'Juventude Plena (25-30 anos)', 'Adulto (31-45 anos)', 'Meia-idade (46-60 anos)', 'Idoso (60-75 anos)', 'Idade Avançada (75 anos ou mais)'])

        with st.expander("Renda Mensal"):
            filtroRenda = st.radio("Qual filtro você deseja aplicar?", ['Sem Filtro', '0 a 85 Reais', '85,01 a 170 Reais', '170,01 a 477 Reais', 'A partir de 477,01 Reais'])

        with st.expander("Configurações dos Gráficos"):
            # Definir o número máximo de gráficos por linha e o tamanho inicial dos gráficos
            maxGraficosPorLinha = st.slider("Número máximo de gráficos por linha", min_value=1, max_value=4, value=4)
            tamanhoGrafico = st.slider("Tamanho dos gráficos", min_value=350, max_value=1000, value=350)
            tipoGraficoDonutPizza = st.radio("Qual tipo de gráfico você prefere?", ['Donut', 'Pizza'])
            tipoGraficoBarraBoxplot = st.radio("Qual tipo de gráfico você prefere?", ['Barra', 'Boxplot'])

    dfCadUnicoDivinopolis, dfCadUnicoOuroBranco, dfCadUnicoSaoJoaoDelRei, dfCadUnicoSeteLagoas = Filtragem(filtroSexo, filtroRaca, filtroDeficiencia, filtroIdade, filtroRenda,checkDivinopolis, checkOuroBranco, checkSaoJoaoDelRei, checkSeteLagoas, dfCadUnicoDivinopolis, dfCadUnicoOuroBranco, dfCadUnicoSaoJoaoDelRei, dfCadUnicoSeteLagoas)
    
    st.markdown("<h1 style='text-align: center;'>Amostra CadÚnico 2018</h1>", unsafe_allow_html=True)

    # NOVA SEÇÃO PARA MAPAS - COLOCAR NO INÍCIO PARA MELHOR VISUALIZAÇÃO
    if checkMapaInterativo:
        MapaInterativoUFSJ(dfPolisPCDaSUFSJ)
        st.markdown("---")
    
    if checkMapaSaude:
        MapaComparativoSaude(dfPolisPCDaSUFSJ)
        st.markdown("---")

    if checkDadosGerais:
        bases = [dfCadUnicoDivinopolis, dfCadUnicoOuroBranco, dfCadUnicoSaoJoaoDelRei, dfCadUnicoSeteLagoas]
        checkBoxs = [checkDivinopolis, checkOuroBranco, checkSaoJoaoDelRei, checkSeteLagoas]
        configuracoes = [maxGraficosPorLinha, tamanhoGrafico, tipoGraficoDonutPizza]

        GraficoRacas(checkBoxs, bases, configuracoes)
        GraficoSexo(checkBoxs, bases, configuracoes)
        GraficoDeficiencia(checkBoxs, bases, configuracoes)
        GraficoDistribuiçãoIdade(checkBoxs, bases, [maxGraficosPorLinha, tamanhoGrafico, tipoGraficoBarraBoxplot])        
    
    if checkEducacao:
        bases = [dfCadUnicoDivinopolis, dfCadUnicoOuroBranco, dfCadUnicoSaoJoaoDelRei, dfCadUnicoSeteLagoas]
        checkBoxs = [checkDivinopolis, checkOuroBranco, checkSaoJoaoDelRei, checkSeteLagoas]
        configuracoes = [maxGraficosPorLinha, tamanhoGrafico, tipoGraficoDonutPizza]

        GraficoLerEEscrever(checkBoxs, bases, configuracoes)
        GraficoFrenquenciaEscola(checkBoxs, bases, configuracoes)
        GraficoEscolaPublicaParticular(checkBoxs, bases, configuracoes)
        GraficoNivelEscolar(checkBoxs, bases, configuracoes)
        GraficoConclusaoCurso(checkBoxs, bases, configuracoes)
        GraficoFormaDeEnsino(checkBoxs, bases, configuracoes)

    if checkRendaFinanceira:
        bases = [dfCadUnicoDivinopolis, dfCadUnicoOuroBranco, dfCadUnicoSaoJoaoDelRei, dfCadUnicoSeteLagoas]
        checkBoxs = [checkDivinopolis, checkOuroBranco, checkSaoJoaoDelRei, checkSeteLagoas]
        configuracoes = [maxGraficosPorLinha, tamanhoGrafico, tipoGraficoDonutPizza]

        GraficoFuncaoTrabalho(checkBoxs, bases, configuracoes)
        GraficoFaixaRenda(checkBoxs, bases, configuracoes)
        GraficoTrabalho12Meses(checkBoxs, bases, configuracoes)
        
    if checkSaude:
        TabelaPCDaS(dfPolisPCDaSUFSJ, checkDivinopolis, checkOuroBranco, checkSaoJoaoDelRei, checkSeteLagoas)

if __name__ == "__main__":
    main()
