import pandas as pd

dados_ = pd.read_csv("data\\dados_federais_vacinacao_cg.csv", encoding='UTF-8', error_bad_lines=False)

#dados_ = dados_.loc[dados_['vacina_dataaplicacao'] >= '2021-06-01']
dados_.drop(
    ['paciente_endereco_coibgemunicipio',
     'paciente_endereco_copais',
     'paciente_endereco_nmpais',
     'paciente_endereco_uf',
     'paciente_nacionalidade_enumnacionalidade',
     'estabelecimento_valor',
     'estabelecimento_municipio_codigo',
     'estabelecimento_uf',
     'estabelecimento_municipio_nome',
     'vacina_fabricante_referencia'], 
     inplace=True, axis=1)
dados_.to_csv('dados_federais_vacinacao_cg.csv', index=False)