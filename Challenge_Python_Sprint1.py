import os
import re
import random


mecanicos = [{'nome': 'Auto Conserto', 'categoria': 'Conserto', 'avaliação': '4.8', 'orçamento': 'R$423', 'endereço': 'Rua Computer Thinking, 123', 'aberto':True},
            {'nome': 'Peças+', 'categoria': 'Venda de Peças', 'avaliação': '4.8', 'orçamento': 'R$387', 'endereço': 'Avenida Front-End, 456', 'aberto':False},
            {'nome': 'Mecânico 24h', 'categoria': 'Conserto e Venda de Peças', 'avaliação': '4.8', 'orçamento': 'R$456', 'endereço': 'Rua dos Javas, 789', 'aberto':True},
            {'nome': 'Oficina do João', 'categoria': 'Conserto', 'avaliação': '4.7', 'orçamento': 'R$399', 'endereço': 'Rua das Startups, 1010', 'aberto':True},
            {'nome': 'Auto Peças e Serviços', 'categoria': 'Venda de Peças e Conserto', 'avaliação': '4.9', 'orçamento': 'R$499', 'endereço': 'Avenida da Inovação, 2020', 'aberto':True},
            {'nome': 'Mecânica Express', 'categoria': 'Conserto', 'avaliação': '3.8', 'orçamento': 'R$350', 'endereço': 'Rua do Desenvolvimento, 3030', 'aberto':False}]



def efetuar_login():
    print("[Considerando um usuário já cadastrado]")

    while True:
        cpf = input("\nCPF (000.000.000-00): ")

        if re.match(r"\d{3}\.\d{3}\.\d{3}-\d{2}", cpf):
            senha = input("Senha: ")
            entrar_no_menu_principal()
            break
        else:
            os.system('cls')
            print("CPF inválido. Digite um CPF válido.")


def exibir_nome_do_programa ():
    print('''
█▀ █▀█ █▀   █▀▄▀█ █▀▀ █▀▀ ▄▀█ █▄░█ █ █▀▀ █▀█
▄█ █▄█ ▄█   █░▀░█ ██▄ █▄▄ █▀█ █░▀█ █ █▄▄ █▄█  𝙴𝚖 𝚌𝚘𝚕𝚊𝚋𝚘𝚛𝚊𝚌̧𝚊̃𝚘 𝚌𝚘𝚖 a Porto Seguro
       ''')


def exibir_opcoes ():
    print('1. Atendimento Online')
    print('2. Listar Mecânicos na Área')
    print('3. Cadastrar Mecânico')
    print('4. Chamar Reboque')
    print('5. Sair\n')


def escolher_opcoes ():
    
    try: 
        opcao_escolhida = int(input ('Escolha uma opção: '))

        if opcao_escolhida == 1:
            atendimento_online()
        elif opcao_escolhida == 2:
            listar_mecanicos()
        elif opcao_escolhida == 3:
            cadastrar_novo_mecanico ()
        elif opcao_escolhida == 4:
            chamar_reboque()
        elif opcao_escolhida == 5:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def atendimento_online():
    os.system('cls')
    exibir_subtitulo('Iniciando Atendimento...')
    
    modelo_carro = input("Qual o modelo do seu carro? ")
    montadora = input("Qual a montadora do seu carro? ")
    ano_fabricacao = input("Qual o ano de fabricação do seu carro? ")
    problema = input("Descreva o problema que você está enfrentando: ")

    os.system('cls')
    print (f'Dados do veículo: Modelo: {modelo_carro}, Montadora: {montadora}, Ano: {ano_fabricacao} [Após conseguir as informações necessárias e a descrição do problema, o chatbot irá apresentar a resposta que ele acredita ser a mais provável para a causa do problema e exibirá a lista de mecânicos na área, assim como os mecânicos manualmente cadastrados pelo usuário.]')

    # É bom notar que, com exceção das informações sobre o veículo em si, é o usuário que irá explicar qual é o problema. Lendo o feedback, talvez o foco nas perguntas tenha dado a impressão de que o chatbot faria pergunta por pergunta. Esse não é o caso, peço desculpas pela impressão, as perguntas foram colocadas para que o programa não simplesmente descrevesse o processo por print(), mas sim para que tentasse recriá-lo.

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


def cadastrar_novo_mecanico():
    exibir_subtitulo('''Cadastro de novos mecânicos
    Caso tenha preferência por uma localização específica, serviços cadastrados serão sempre mostrados, independente de sua localização.''')
    
    nome_do_mecanico = input('\nDigite o nome do mecânico que deseja cadastrar: ')
    categoria_mecanico = input(f'Digite a categoria do mecânico {nome_do_mecanico} (Conserto; Venda de peças; Troca de óleo; Etc): ')
    avaliacao_mecanico = random.uniform(2, 5)  #Gera um número aleatório entre 2 e 5
    orcamento_mecanico = f'R$ {random.uniform(300, 700):.2f}'  # Gera um número float aleatório entre 300 e 700 e adiciona "R$" antes do número
    avaliacao_mecanico = round(avaliacao_mecanico, 1)  # Arredonda o número para uma casa decimal
    endereco_mecanico = input(f'Digite o endereço (rua/avenida, número) do mecânico {nome_do_mecanico}: ')
    status_mecanico = input('O mecânico cadastrado está aberto? (Essa opção não estará na versão final, visto que o aplicativo já terá essa informação) ')

    if status_mecanico == 'Sim' or status_mecanico == 'sim' or status_mecanico == 'S' or status_mecanico == 's':
        status_mecanico = True
    else:
        status_mecanico = False

    dados_do_mecanico = {'nome':nome_do_mecanico, 'categoria':categoria_mecanico, 'avaliação':avaliacao_mecanico, 'orçamento':orcamento_mecanico, 'endereço':endereco_mecanico, 'aberto':status_mecanico}
    mecanicos.append (dados_do_mecanico)

    print(f'O mecânico {dados_do_mecanico} foi cadastrado com sucesso!\n')
    
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
                    print(f'- {mecanico['nome']} | {mecanico['categoria']} | Avaliação: {mecanico['avaliação']} | {mecanico['orçamento']} | Endereço: {mecanico['endereço']} | {mecanico['aberto']}')
            voltar_ao_menu_principal()
        else:
            print('\nResposta inválida. Por favor, responda com Sim ou Não. ')



def finalizar_app():
    exibir_subtitulo('Finalizando a aplicação...')
    voltar_ao_menu_principal()


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
    efetuar_login()
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

