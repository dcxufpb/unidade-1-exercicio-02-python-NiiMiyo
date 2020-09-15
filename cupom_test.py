import cupom;

nome_loja = "Arcos Dourados Com. de Alimentos LTDA"
logradouro = "Av. Projetada Leste"
numero = 500
complemento = "EUC F32/33/34"
bairro = "Br. Sta Genebra"
municipio = "Campinas"
estado = "SP"
cep = "13080-395"
telefone = "(19) 3756-7408"
observacao = "Loja 1317 (PDP)"
cnpj = "42.591.651/0797-34"
inscricao_estadual = "244.898.500.113"

def test_exercicio1():
    assert cupom.imprime_dados_loja() == '''Arcos Dourados Com. de Alimentos LTDA
Av. Projetada Leste, 500 EUC F32/33/34
Br. Sta Genebra - Campinas - SP
CEP:13080-395 Tel (19) 3756-7408
Loja 1317 (PDP)
CNPJ: 42.591.651/0797-34
IE: 244.898.500.113
'''

def test_exercicio2_tudo_vazio():
    global nome_loja
    global logradouro
    global numero
    global complemento
    global bairro
    global municipio
    global estado
    global cep
    global telefone
    global observacao
    global cnpj
    global inscricao_estadual
    
    nome_loja = ""
    logradouro = ""
    numero = 0
    complemento = ""
    bairro = ""
    municipio = ""
    estado = ""
    cep = ""
    telefone = ""
    observacao = ""
    cnpj = ""
    inscricao_estadual = ""

    assert cupom.imprime_dados_loja() == '''
, 0 
 -  - 
CEP: Tel 

CNPJ: 
IE: 
'''

def test_exercicio2_customizado():
    global nome_loja
    global logradouro
    global numero
    global complemento
    global bairro
    global municipio
    global estado
    global cep
    global telefone
    global observacao
    global cnpj
    global inscricao_estadual
    
    # Defina seus próprios valores para as variáveis a seguir
    nome_loja = ""
    logradouro = ""
    numero = 0
    complemento = ""
    bairro = ""
    municipio = ""
    estado = ""
    cep = ""
    telefone = ""
    observacao = ""
    cnpj = ""
    inscricao_estadual = ""

    #E atualize o texto esperado abaixo
    assert cupom.imprime_dados_loja() == '''
'''
