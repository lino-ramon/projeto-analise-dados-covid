import pandas as pd

dados = pd.read_csv("data\\INFLUD21-15-11-2021.csv", encoding='UTF-8', error_bad_lines=False)

dados = dados.loc[dados['CO_MUN_NOT'] == 250400]
dados['DT_NOTIFIC'] = pd.to_datetime(dados['DT_NOTIFIC'])   


dados = dados.loc[dados['DT_NOTIFIC'] >= '2021-06-01']
dados = dados.loc[dados['DT_NOTIFIC'] <= '2021-08-31']
dados.to_csv('sindrome_gripal.csv', index=False)



#dados = dados_.loc[dados_['vacina_dataaplicacao'] >= '2021-06-01']
# dados.drop(
#     ['paciente_endereco_coibgemunicipio',
#      'paciente_endereco_copais',
#      'paciente_endereco_nmpais',
#      'paciente_endereco_uf',
#      'paciente_nacionalidade_enumnacionalidade',
#      'estabelecimento_valor',
#      'estabelecimento_municipio_codigo',
#      'estabelecimento_uf',
#      'estabelecimento_municipio_nome',
#      'vacina_fabricante_referencia'], 
#      inplace=True, axis=1)