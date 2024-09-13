import os
import re
import random


mecanicos = [{'nome': 'Auto Conserto', 'categoria': 'Conserto', 'avaliação': '4.8', 'orçamento': 'R$423', 'endereço': 'Rua Computer Thinking, 123', 'aberto':True},
            {'nome': 'Peças+', 'categoria': 'Venda de Peças', 'avaliação': '4.8', 'orçamento': 'R$387', 'endereço': 'Avenida Front-End, 456', 'aberto':False},
            {'nome': 'Mecânico 24h', 'categoria': 'Conserto e Venda de Peças', 'avaliação': '4.8', 'orçamento': 'R$456', 'endereço': 'Rua dos Javas, 789', 'aberto':True},
            {'nome': 'Oficina do João', 'categoria': 'Conserto', 'avaliação': '4.7', 'orçamento': 'R$399', 'endereço': 'Rua das Startups, 1010', 'aberto':True},
            {'nome': 'Auto Peças e Serviços', 'categoria': 'Venda de Peças e Conserto', 'avaliação': '4.9', 'orçamento': 'R$499', 'endereço': 'Avenida da Inovação, 2020', 'aberto':True},
            {'nome': 'Mecânica Express', 'categoria': 'Conserto', 'avaliação': '3.8', 'orçamento': 'R$350', 'endereço': 'Rua do Desenvolvimento, 3030', 'aberto':False}]

usuarios = {
    "000.000.000-00": "senha123",
}


def efetuar_login_ou_cadastro():

    while True:

        print("1. Login")
        print("2. Cadastro")
        print("3. Entrar como Professor [Debug]")
        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            
            while True:
                cpf = input("\nCPF (000.000.000-00): ")
                if re.match(r"\d{3}\.\d{3}\.\d{3}-\d{2}", cpf):
                    senha = input("Senha: ")
                    if cpf in usuarios and usuarios[cpf] == senha:
                        entrar_no_menu_principal()
                        break
                    else:
                        print("CPF ou senha inválidos.")
                else:
                    os.system('cls')
                    print("CPF inválido. Digite um CPF válido.")
        elif opcao == '2':
            
            while True:
                cpf = input("\nCPF (000.000.000-00): ")
                if re.match(r"\d{3}\.\d{3}\.\d{3}-\d{2}", cpf):
                    if cpf not in usuarios:
                        senha = input("Senha: ")
                        usuarios[cpf] = senha
                        print("Cadastro realizado com sucesso!")
                        break
                    else:
                        print("CPF já cadastrado.")
                else:
                    os.system('cls')
                    print("CPF inválido. Digite um CPF válido.")
        elif opcao == '3':
            
            entrar_no_menu_principal()
            break
            
        else:
            print("Opção inválida.")


def exibir_nome_do_programa ():
    print('''
█▀ █▀█ █▀   █▀▄▀█ █▀▀ █▀▀ ▄▀█ █▄░█ █ █▀▀ █▀█
▄█ █▄█ ▄█   █░▀░█ ██▄ █▄▄ █▀█ █░▀█ █ █▄▄ █▄█  𝙴𝚖 𝚌𝚘𝚕𝚊𝚋𝚘𝚛𝚊𝚌̧𝚊̃𝚘 𝚌𝚘𝚖 a Porto Seguro
       ''')


def exibir_opcoes ():
    print('1. Integrantes')
    print('2. Atendimento Online')
    print('3. Listar Mecânicos na Área')
    print('4. Buscar Mecânico')
    print('5. Cadastrar Mecânico')
    print('6. Modificar Mecânico')
    print('7. Excluir Mecânico')
    print('8. Chamar Reboque')
    print('9. Logout\n')


def escolher_opcoes():
    while True:
        try: 
            opcao_escolhida = int(input('Escolha uma opção: '))

            if 1 <= opcao_escolhida <= 9:
                if opcao_escolhida == 1:
                    mostrar_integrantes()
                elif opcao_escolhida == 2:
                    atendimento_online()
                elif opcao_escolhida == 3:
                    listar_mecanicos()
                elif opcao_escolhida == 4:
                    buscar_mecanico()
                elif opcao_escolhida == 5:
                    cadastrar_novo_mecanico()
                elif opcao_escolhida == 6:
                    modificar_mecanico()
                elif opcao_escolhida == 7:
                    excluir_mecanico()
                elif opcao_escolhida == 8:
                    chamar_reboque()
                else:
                    finalizar_app()
                break
            else:
                print("\nOpção inválida. Por favor, escolha um número entre 1 e 9.")
        except ValueError:
            print("\nEntrada inválida. Por favor, digite um número inteiro.")



def mostrar_integrantes():

    os.system('cls')
    exibir_subtitulo('Integrantes do Grupo SOS Mecânico:')

    print('Enzo Prado Soddano \tRM557937')
    print('Enzo Dias Alfaia Mendes RM558438')
    print('Danilo Correia e Silva \tRM557540')

    voltar_ao_menu_principal()



def atendimento_online():

    os.system('cls')
    exibir_subtitulo('Iniciando Atendimento...')
    
    modelo_carro = input("Qual o modelo do seu carro? ")
    montadora = input("Qual a montadora do seu carro? ")
    ano_fabricacao = input("Qual o ano de fabricação do seu carro? ")
    problema = input("Descreva o problema que você está enfrentando: ")

    os.system('cls')
    print (f'Dados do veículo: Modelo: {modelo_carro}, Montadora: {montadora}, Ano: {ano_fabricacao} [Após conseguir as informações necessárias e a descrição do problema, o chatbot irá apresentar a resposta que ele acredita ser a mais provável para a causa do problema e exibirá a lista de mecânicos na área, assim como os mecânicos manualmente cadastrados pelo usuário.]')

    print('\nListando mecânicos na sua área:')
    print()

    for mecanico in mecanicos:
        nome_mecanico = mecanico ['nome']
        categoria_mecanico = mecanico ['categoria']
        avaliacao_mecanico = mecanico ['avaliação']
        orcamento_mecanico = mecanico ['orçamento']
        endereco_mecanico = mecanico ['endereço']
        ativo = 'Sim' if mecanico ['aberto'] == True else 'Não'
        print(f'- {nome_mecanico} | {categoria_mecanico} | {avaliacao_mecanico} | {orcamento_mecanico} | {endereco_mecanico} | Aberto: {ativo}')

    voltar_ao_menu_principal()


def listar_mecanicos():

    exibir_subtitulo('Listando Mecânicos na sua área')

    for mecanico in mecanicos:
        nome_mecanico = mecanico ['nome']
        categoria_mecanico = mecanico ['categoria']
        avaliacao_mecanico = mecanico ['avaliação']
        orcamento_mecanico = mecanico ['orçamento']
        endereco_mecanico = mecanico ['endereço']
        ativo = 'Sim' if mecanico ['aberto'] == True else 'Não'
        print(f'- {nome_mecanico} | {categoria_mecanico} | Avaliação: {avaliacao_mecanico} | {orcamento_mecanico} | {endereco_mecanico} | Aberto: {ativo}')

    voltar_ao_menu_principal()


def buscar_mecanico():

    exibir_subtitulo('Permite buscar mecânicos por nome ou endereço.')

    opcao_busca = input("Deseja buscar por nome (N) ou por endereço (E)? ").upper()

    if opcao_busca == 'N':
        nome_buscado = input("Digite o nome do mecânico: ")
        resultados = buscar_por_nome(nome_buscado)
        voltar_ao_menu_principal()
    elif opcao_busca == 'E':
        endereco_buscado = input("Digite o endereço do mecânico: ")
        resultados = buscar_por_endereco(endereco_buscado)
        voltar_ao_menu_principal()
    else:
        print("Opção inválida. Por favor, digite 'N' para buscar por nome ou 'E' para buscar por endereço.")
        return

    if resultados:
        print("Resultados da busca:")
        for mecanico in resultados:
            print(f"- {mecanico['nome']} | {mecanico['endereço']}")
    else:
        print("Nenhum mecânico encontrado.")



def buscar_por_nome(nome_buscado):
    
    resultados = []
    for mecanico in mecanicos:
        if nome_buscado.lower() in mecanico['nome'].lower():
            resultados.append(mecanico)
    print(resultados)



def buscar_por_endereco(endereco_buscado):
    
    resultados = []
    for mecanico in mecanicos:
        if endereco_buscado.lower() in mecanico['endereço'].lower():
            resultados.append(mecanico)
    print(resultados)



def cadastrar_novo_mecanico():

    exibir_subtitulo('''Cadastro de novos mecânicos
    Caso tenha preferência por uma localização específica, serviços cadastrados serão sempre mostrados, independente de sua localização.''')

    try:
        
        nome_do_mecanico = input('\nDigite o nome do mecânico que deseja cadastrar: ')
        if not nome_do_mecanico:
            os.system('cls')
            raise ValueError("O nome do mecânico é obrigatório.")

        categoria_mecanico = input(f'Digite a categoria do mecânico {nome_do_mecanico} (Conserto, Venda de peças, Conserto e Venda de Peças, Troca de óleo): ')
        if categoria_mecanico not in ['Conserto', 'Venda de Peças', 'Conserto e Venda de Peças', 'Troca de óleo']:
            os.system('cls')
            raise ValueError("Categoria inválida. Opções: 'Conserto', 'Venda de Peças', 'Conserto e Venda de Peças' e 'Troca de óleo'.")

        endereco_mecanico = input(f'Digite o endereço (rua/avenida, número) do mecânico {nome_do_mecanico}: ')
        if not endereco_mecanico:
            os.system('cls')
            raise ValueError("O endereço do mecânico é obrigatório.")

        status_mecanico = input('O mecânico cadastrado está aberto? (sim/não): ').lower()
        if status_mecanico not in ['sim', 'não']:
            os.system('cls')
            raise ValueError("Resposta inválida para o status. Digite 'sim' ou 'não'.")

        avaliacao_mecanico = random.uniform(2, 5)  #Gera um número aleatório entre 2 e 5
        orcamento_mecanico = f'R$ {random.uniform(300, 700):.2f}'  # Gera um número float aleatório entre 300 e 700 e adiciona "R$" antes do número
        avaliacao_mecanico = round(avaliacao_mecanico, 1)  # Arredonda o número para uma casa decimal

        dados_do_mecanico = {
            'nome': nome_do_mecanico,
            'categoria': categoria_mecanico,
            'avaliação': avaliacao_mecanico,
            'orçamento': orcamento_mecanico,
            'endereço': endereco_mecanico,
            'aberto': status_mecanico == 'sim'
        }

        mecanicos.insert(0, dados_do_mecanico)

        print(f'O mecânico {dados_do_mecanico} foi cadastrado com sucesso!\n')

    except ValueError as e:
        print(f"Erro ao cadastrar mecânico: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

    voltar_ao_menu_principal()



def modificar_mecanico():
    
    os.system('cls')
    nome_do_mecanico = input("Digite o nome completo do mecânico que deseja modificar: ")

    for indice, mecanico in enumerate(mecanicos):

        if mecanico['nome'].lower() == nome_do_mecanico.lower():

            print(f"\nDados atuais do mecânico '{nome_do_mecanico}':")

            for chave, valor in mecanico.items():
                print(f"{chave.capitalize()}: {valor}")

            nova_categoria = input("\nDigite a nova categoria (deixe em branco para manter a atual): ")
            nova_avaliacao = input("Digite a nova avaliação (número entre 2 e 5): ")
            novo_orcamento = input("Digite o novo orçamento: R$")
            novo_endereco = input("Digite o novo endereço (deixe em branco para manter a atual): ")
            novo_status = input("Digite o novo status (aberto/fechado): ")

            mecanico['categoria'] = nova_categoria if nova_categoria else mecanico['categoria']
            mecanico['endereço'] = novo_endereco if novo_endereco else mecanico['endereço']
            mecanico['avaliação'] = nova_avaliacao if nova_avaliacao else mecanico['avaliação']
            mecanico['orçamento'] = novo_orcamento if novo_orcamento else mecanico['orçamento']
            mecanico['aberto'] = True if novo_status.lower() == 'aberto' else False if novo_status.lower() == 'fechado' else mecanico['aberto']

            print("\nOs dados do mecânico foram atualizados com sucesso!")
            voltar_ao_menu_principal()
        else:
            print(f"\nNão foi encontrado nenhum mecânico com o nome {nome_do_mecanico}.")



def excluir_mecanico():

    exibir_subtitulo('Exclui um mecânico da lista com base no nome.')

    nome_mecanico = input("Digite o nome do mecânico que deseja excluir: ")

    for i, mecanico in enumerate(mecanicos):

        if mecanico['nome'].lower() == nome_mecanico.lower():

            del mecanicos[i]
            print(f"\nO mecânico '{nome_mecanico}' foi excluído com sucesso.")
            voltar_ao_menu_principal()
        else:
            print(f"\nNão foi encontrado nenhum mecânico com o nome '{nome_mecanico}'.")
            voltar_ao_menu_principal()



def chamar_reboque():
    exibir_subtitulo('Emergência')
    while True:
        permissao = input('\nVocê permite que esse aparelho use a sua localização? ')
        if permissao == 'Sim' or permissao == 'sim' or permissao == 'S' or permissao == 's':
            print('\nUm reboque está a caminho, não desligue a sua localização. ')
            break
        elif permissao == 'Não' or permissao == 'não' or permissao == 'nao' or permissao == 'N' or permissao == 'n':
            print('\nListando mecânicos abertos na sua área:')
            for mecanico in mecanicos:
                if mecanico['aberto'] == True:
                    print(f"- {mecanico['nome']} | {mecanico['categoria']} | Avaliação: {mecanico['avaliação']} | {mecanico['orçamento']} | Endereço: {mecanico['endereço']} | {mecanico['aberto']}")
            voltar_ao_menu_principal()
        else:
            print('\nResposta inválida. Por favor, responda com Sim ou Não. ')



def finalizar_app():
    exibir_subtitulo('Logout realizado com sucesso!')
    efetuar_login_ou_cadastro()



def entrar_no_menu_principal():
    print('\nLogin efetuado com sucesso!')
    input('\nDigite uma tecla para entrar no menu principal')
    main2()



def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal ')
    main2()



def opcao_invalida():
    os.system('cls')
    print('Opção inválida!\n')
    voltar_ao_menu_principal()



def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()



def main():
    os.system ('cls')
    efetuar_login_ou_cadastro()
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()



def main2():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()



if __name__ == '__main__':
    main()

