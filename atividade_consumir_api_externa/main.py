from services import consultar_bolsa_familia_por_cpf_ou_nis, consultar_bolsa_familia_por_municipio, consultar_garantia_safra_por_cpf_ou_nis, consultar_seguro_defeso_por_cpf_ou_nis,consultar_servidor_do_poder_executivo_por_cpf

while True:
    opcao = input('1 - Consultar bolsa família por CPF ou NIS\n2 - Consultar Bolsa Família por Municipio\n3 - Consultar Garantia-Safra por CPF ou NIS\n4 - Consultar Seguro Defeso por CPF ou NIS\n5 - Consultar Servidor do Poder Executivo por CPF\n6 - Sair\nDigite uma opção:')
    if opcao == '1':     
        cpf_ou_nis = input('Digite o CPF ou NIS:')
        consultar_bolsa_familia_por_cpf_ou_nis(cpf_ou_nis)

    elif opcao == '2':
        ano = input('Digite o ano:')
        mes = input('Digite o mês:')
        codigo_ibge = input('Digite o código do municipio:')
        ano_mes = ano+mes
        consultar_bolsa_familia_por_municipio(ano_mes,codigo_ibge)
    
    elif opcao == '3':
        cpf_ou_nis = input('Digite o CPF ou NIS:')
        consultar_garantia_safra_por_cpf_ou_nis(cpf_ou_nis)

    elif opcao == '4':
        cpf_ou_nis = input('Digite o CPF ou NIS:')
        consultar_seguro_defeso_por_cpf_ou_nis(cpf_ou_nis)
    
    elif opcao == '5':
        cpf = input('Digite o CPF:')
        consultar_servidor_do_poder_executivo_por_cpf(cpf)

    elif opcao == '6':
        print('finalizando...')
        break

    else:
        pass
