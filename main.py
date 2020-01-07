'''
Autor: Diego Rocha Cerqueira
ComponenteCurricular: MI Algoritmos
Concluido em:19/11/2019
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
'''
from Funcoes import *;

opcao=0
contadorcomumDermatologia=1
contadorpreferencialDermatologia=1

contadorcomumEndocrinologia=1
contadorpreferencialEndocrinologia=1

dados_Pacientes={}
contadorcomumOrtopedia=1
contadorpreferencialOrtopedia=1
#Listas com o cadastro de todos os pacientes
'''listaPacienteComumDermatologia=[]
listaPacientePrioritarioDermatologia=[]

listaPacienteComumEndocrinologia=[]
listaPacientePrioritarioEndocrinologia=[]

listaPacienteComumOrtopedia=[]
listaPacientePrioritarioOrtopedia=[]
#Fim do codigo com as lista
'''
#Listas de espera do consultório
listaEsperaPacienteComumDermatologia=[]
listaEsperaPacientePrioritarioDermatologia=[]

listaEsperaPacienteComumEndocrinologia=[]
listaEsperaPacientePrioritarioEndocrinologia=[]

listaEsperaPacienteComumOrtopedia=[]
listaEsperaPacientePrioritarioOrtopedia=[]
#Fim do código com as listas

#Listas de pacientes atendidos do consultório
listaPacienteComumAtendidoDermatologia=[]
listaPacientePrioritarioAtendidoDermatologia=[]

listaPacienteComumAtendidoEndocrinologia=[]
listaPacientePrioritarioAtendidoEndocrinologia=[]

listaPacienteComumAtendidoOrtopedia=[]
listaPacientePrioritarioAtendidoOrtopedia=[]

paciente_em_antendimento_Dermatologia=[]
paciente_em_antendimento_Endocrinologia=[]
paciente_em_antendimento_Ortopedia=[]


while(opcao!=9):
    MENU()
    opcao=input("Escolha uma opção\n")
    boolOpcao=VerificarInt(opcao)
    opcao=ValidarOpcao(boolOpcao, opcao)

    if(opcao==1):
        pacientes=EmitirSenha(contadorcomumDermatologia, contadorcomumEndocrinologia,
                               contadorcomumOrtopedia, contadorpreferencialDermatologia,
                               contadorpreferencialEndocrinologia, contadorpreferencialOrtopedia)
        dados_Pacientes[pacientes[5]]=pacientes

        if(pacientes[0]=="c" or pacientes[0]=="C"):

            if(pacientes[4]=="d" or pacientes[4]=="D"):

                listaEsperaPacienteComumDermatologia.append(pacientes)
                contadorcomumDermatologia+=1
            elif(pacientes[4]=="e" or pacientes[4]=="E"):

                listaEsperaPacienteComumEndocrinologia.append(pacientes)
                contadorcomumEndocrinologia+=1
            elif(pacientes[4]=="O" or pacientes[4]=="o"):

              listaEsperaPacienteComumOrtopedia.append(pacientes)
              contadorcomumOrtopedia+=1

        elif(pacientes[0]=="p" or pacientes[0]=="P"):
            if(pacientes[4]=="d" or pacientes[4]=="D"):

              listaEsperaPacientePrioritarioDermatologia.append(pacientes)
              contadorpreferencialDermatologia+=1
            elif(pacientes[4]=="e" or pacientes[4]=="E"):

              listaEsperaPacientePrioritarioEndocrinologia.append(pacientes)
              contadorpreferencialEndocrinologia+=1
            elif(pacientes[4]=="O" or pacientes[4]=="o"):

              listaEsperaPacientePrioritarioOrtopedia.append(pacientes)
              contadorpreferencialOrtopedia+=1


        print(dados_Pacientes)

    elif(opcao==2):

        tamPrioritarioDermatologiaAtendido=len(listaPacientePrioritarioAtendidoDermatologia)
        tamPrioritarioEndocrinologiaAtendido=len(listaPacientePrioritarioAtendidoEndocrinologia)
        tamPrioritarioOrtopediaAtendido=len(listaPacientePrioritarioAtendidoOrtopedia)
        tamComumDermatologiaAtendido=len(listaPacienteComumAtendidoDermatologia)
        tamComumEndocrinologiaAtendido=len(listaPacienteComumAtendidoEndocrinologia)
        tamComumOrtopediaAtendido=len(listaPacienteComumAtendidoOrtopedia)
        Dados_paciente_chamados_para_atendimento=(ChamarPacienteParaAtendimento
                                                  (paciente_em_antendimento_Dermatologia, paciente_em_antendimento_Endocrinologia,
                                                  paciente_em_antendimento_Ortopedia, listaEsperaPacienteComumDermatologia,
                                                  listaEsperaPacientePrioritarioDermatologia, listaEsperaPacienteComumEndocrinologia,
                                                  listaEsperaPacientePrioritarioEndocrinologia, listaEsperaPacienteComumOrtopedia,
                                                  listaEsperaPacientePrioritarioOrtopedia, tamComumDermatologiaAtendido,
                                                  tamComumEndocrinologiaAtendido, tamComumOrtopediaAtendido,
                                                  tamPrioritarioDermatologiaAtendido, tamPrioritarioEndocrinologiaAtendido,
                                                  tamPrioritarioOrtopediaAtendido, dados_Pacientes))

        #A função chamada acima retorna varios valores, então é necessário fazer o desempacotamento desses dados,
        #o desempacotamento está sendo feito no trecho de código abaixo
        paciente_em_antendimento_Ortopedia=Dados_paciente_chamados_para_atendimento[0]
        paciente_em_antendimento_Endocrinologia=Dados_paciente_chamados_para_atendimento[1]
        paciente_em_antendimento_Dermatologia=Dados_paciente_chamados_para_atendimento[2]
        hora_atendimento_Dermatologia=Dados_paciente_chamados_para_atendimento[3]
        minuto_atendimento_Dermatologia=Dados_paciente_chamados_para_atendimento[4]
        hora_atendimento_Endocrinologia=Dados_paciente_chamados_para_atendimento[5]
        minuto_atendimento_Endocrinologia=Dados_paciente_chamados_para_atendimento[6]
        hora_atendimento_Ortopedia=Dados_paciente_chamados_para_atendimento[7]
        minuto_atendimento_Ortopedia=Dados_paciente_chamados_para_atendimento[8]
        listaEsperaPacienteComumDermatologia=Dados_paciente_chamados_para_atendimento[9]
        listaEsperaPacientePrioritarioDermatologia=Dados_paciente_chamados_para_atendimento[10]
        listaEsperaPacienteComumEndocrinologia=Dados_paciente_chamados_para_atendimento[11]
        listaEsperaPacientePrioritarioEndocrinologia=Dados_paciente_chamados_para_atendimento[12]
        listaEsperaPacienteComumOrtopedia=Dados_paciente_chamados_para_atendimento[13]
        listaEsperaPacientePrioritarioOrtopedia=Dados_paciente_chamados_para_atendimento[14]
        dados_Pacientes=Dados_paciente_chamados_para_atendimento[15]
        #O bloco de codigo abaixo é para inserir a data de inicio da consulta de um usuario no dicionario de dados
        if(len(paciente_em_antendimento_Ortopedia)==8):
            dados_Pacientes[paciente_em_antendimento_Ortopedia[5]].append(paciente_em_antendimento_Ortopedia[6])
            dados_Pacientes[paciente_em_antendimento_Ortopedia[5]].append(paciente_em_antendimento_Ortopedia[7])
            print('Paciente em atendimento, senha: ', dados_Pacientes[paciente_em_antendimento_Ortopedia[5]])
        if(len(paciente_em_antendimento_Endocrinologia)==8):
            dados_Pacientes[paciente_em_antendimento_Endocrinologia[5]].append(paciente_em_antendimento_Endocrinologia[6])
            dados_Pacientes[paciente_em_antendimento_Endocrinologia[5]].append(paciente_em_antendimento_Endocrinologia[7])
            print('Paciente em atendimento, senha: ', dados_Pacientes[paciente_em_antendimento_Endocrinologia[5]])
        if(len(paciente_em_antendimento_Dermatologia)==8):
            dados_Pacientes[paciente_em_antendimento_Dermatologia[5]].append(paciente_em_antendimento_Dermatologia[6])
            dados_Pacientes[paciente_em_antendimento_Dermatologia[5]].append(paciente_em_antendimento_Dermatologia[7])
            print('Paciente em atendimento, senha: ', dados_Pacientes[paciente_em_antendimento_Dermatologia[5]])



    elif(opcao==3):
        for senha, paciente in dados_Pacientes.items():
            print(senha, paciente)
        excluir_Paciente=input("Digite a chave do paciente que deseja excluir")
        #Tratamento para caso o usuario digite uma chave inexistente
        while(not dados_Pacientes.get(excluir_Paciente)):
            excluir_Paciente=input("Digite a chave do paciente que deseja excluir")

        #verificando em qual lista está a chave, para mandar a lista correspondente para a função de exclusão
        if(dados_Pacientes.get(excluir_Paciente)):
            if(len(dados_Pacientes[excluir_Paciente])==6):
                if(excluir_Paciente[0]=="c"):
                    if(excluir_Paciente[1]=="d"):
                        dados_Pacientes, listaEsperaPacienteComumDermatologia=PularPaciente(dados_Pacientes, excluir_Paciente, listaEsperaPacienteComumDermatologia)
                    elif(excluir_Paciente[1]=="e"):
                        dados_Pacientes, listaEsperaPacienteComumEndocrinologia=PularPaciente(dados_Pacientes, excluir_Paciente, listaEsperaPacienteComumEndocrinologia)
                    elif(excluir_Paciente[1]=="o"):
                        dados_Pacientes, listaEsperaPacienteComumOrtopedia=PularPaciente(dados_Pacientes, excluir_Paciente, listaEsperaPacienteComumOrtopedia)
                else:
                    if(excluir_Paciente[1]=="d"):
                        dados_Pacientes, listaEsperaPacientePrioritarioDermatologia=PularPaciente(dados_Pacientes, excluir_Paciente, listaEsperaPacientePrioritarioDermatologia)
                    elif(excluir_Paciente[1]=="e"):
                        dados_Pacientes, listaEsperaPacientePrioritarioEndocrinologia=PularPaciente(dados_Pacientes, excluir_Paciente, listaEsperaPacientePrioritarioEndocrinologia)
                    elif(excluir_Paciente[1]=="o"):
                        dados_Pacientes, listaEsperaPacientePrioritarioOrtopedia=PularPaciente(dados_Pacientes, excluir_Paciente, listaEsperaPacientePrioritarioOrtopedia)
            else:
                print("Impossível pular paciente pois ele não está na lista de espera")

    elif(opcao==4):
        Dados_pacientes_atendidos=(EncerrarConsulta(paciente_em_antendimento_Dermatologia, paciente_em_antendimento_Endocrinologia,
                         paciente_em_antendimento_Ortopedia, listaPacienteComumAtendidoDermatologia,
                         listaPacienteComumAtendidoEndocrinologia, listaPacienteComumAtendidoOrtopedia,
                         listaPacientePrioritarioAtendidoDermatologia, listaPacientePrioritarioAtendidoEndocrinologia,
                         listaPacientePrioritarioAtendidoOrtopedia, dados_Pacientes))
        paciente_em_antendimento_Dermatologia=Dados_pacientes_atendidos[0]
        paciente_em_antendimento_Endocrinologia=Dados_pacientes_atendidos[1]
        paciente_em_antendimento_Ortopedia=Dados_pacientes_atendidos[2]
        listaPacienteComumAtendidoDermatologia=Dados_pacientes_atendidos[3]
        listaPacienteComumAtendidoEndocrinologia=Dados_pacientes_atendidos[4]
        listaPacienteComumAtendidoOrtopedia=Dados_pacientes_atendidos[5]
        listaPacientePrioritarioAtendidoDermatologia=Dados_pacientes_atendidos[6]
        listaPacientePrioritarioAtendidoEndocrinologia=Dados_pacientes_atendidos[7]
        listaPacientePrioritarioAtendidoOrtopedia=Dados_pacientes_atendidos[8]
        dados_Pacientes=Dados_pacientes_atendidos[9]
        print("Consulta finalizada!!")
    elif(opcao==5):
        ExibirFilaDeEspera()
    elif(opcao==6):
        ExibirPacientesAtendidosNoDia()
    elif(opcao==7):
        ExibirTempoMedioDeEsperaDosPacientes()
    elif(opcao==8):
        ExibirTempoMedioDeAtendimentoDosPacientes()
