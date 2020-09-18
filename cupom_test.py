import cupom

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

    cupom.nome_loja = ""
    cupom.logradouro = ""
    cupom.numero = 0
    cupom.complemento = ""
    cupom.bairro = ""
    cupom.municipio = ""
    cupom.estado = ""
    cupom.cep = ""
    cupom.telefone = ""
    cupom.observacao = ""
    cupom.cnpj = ""
    cupom.inscricao_estadual = ""

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
    cupom.nome_loja = "Top 10 nomes de lojas"
    cupom.logradouro = "Rua Tchurusbango Tchurusmago"
    cupom.numero = 13
    cupom.complemento = "Do lado da casa vizinha"
    cupom.bairro = "Bairro do Limoeiro"
    cupom.municipio = "São Paulo"
    cupom.estado = "SP"
    cupom.cep = "08090-284"
    cupom.telefone = "(11) 4002-8922"
    cupom.observacao = "Entre o Campinho e a Lua de Baixo"
    cupom.cnpj = "43.745.249/0001-39"
    cupom.inscricao_estadual = "564.213.199.866"

    expected = "Top 10 nomes de lojas\n"
    expected += "Rua Tchurusbango Tchurusmago, 13 Do lado da casa vizinha\n"
    expected += "Bairro do Limoeiro - São Paulo - SP\n"
    expected += "CEP:08090-284 Tel (11) 4002-8922\n"
    expected += "Entre o Campinho e a Lua de Baixo\n"
    expected += "CNPJ: 43.745.249/0001-39\n"
    expected += "IE: 564.213.199.866\n"

    # E atualize o texto esperado abaixo
    assert cupom.imprime_dados_loja() == expected
