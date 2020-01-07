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

contadorcomumOrtopedia=1
contadorpreferencialOrtopedia=1
#Listas com o cadastro de todos os pacientes
listaPacienteComumDermatologia=[]
listaPacientePrioritarioDermatologia=[]

listaPacienteComumEndocrinologia=[]
listaPacientePrioritarioEndocrinologia=[]

listaPacienteComumOrtopedia=[]
listaPacientePrioritarioOrtopedia=[]
#Fim do codigo com as lista

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

paciente_em_antendimento_Dermatologia=""
paciente_em_antendimento_Endocrinologia=""
paciente_em_antendimento_Ortopedia=""


while(opcao!=9):
    MENU()
    opcao=input("Escolha uma opção\n")
    boolOpcao=VerificarInt(opcao)
    opcao=ValidarOpcao(boolOpcao, opcao)

    if(opcao==1):
        pacientes=EmitirSenha(contadorcomumDermatologia, contadorcomumEndocrinologia,
                               contadorcomumOrtopedia, contadorpreferencialDermatologia,
                               contadorpreferencialEndocrinologia, contadorpreferencialOrtopedia)

        if(pacientes[0]=="c" or pacientes[0]=="C"):

            if(pacientes[4]=="d" or pacientes[4]=="D"):
              listaPacienteComumDermatologia.append(pacientes)
              listaEsperaPacienteComumDermatologia.append(pacientes)
              contadorcomumDermatologia+=1
            elif(pacientes[4]=="e" or pacientes[4]=="E"):
              listaPacienteComumEndocrinologia.append(pacientes)
              listaEsperaPacienteComumEndocrinologia.append(pacientes)
              contadorcomumEndocrinologia+=1
            elif(pacientes[4]=="O" or pacientes[4]=="o"):
              listaPacienteComumOrtopedia.append(pacientes)
              listaEsperaPacienteComumOrtopedia.append(pacientes)
              contadorcomumOrtopedia+=1

        elif(pacientes[0]=="p" or pacientes[0]=="P"):
            if(pacientes[4]=="d" or pacientes[4]=="D"):
              listaPacientePrioritarioDermatologia.append(pacientes)
              listaEsperaPacientePrioritarioDermatologia.append(pacientes)
              contadorpreferencialDermatologia+=1
            elif(pacientes[4]=="e" or pacientes[4]=="E"):
              listaPacientePrioritarioEndocrinologia.append(pacientes)
              listaEsperaPacientePrioritarioEndocrinologia.append(pacientes)
              contadorpreferencialEndocrinologia+=1
            elif(pacientes[4]=="O" or pacientes[4]=="o"):
              listaPacientePrioritarioOrtopedia.append(pacientes)
              listaEsperaPacientePrioritarioOrtopedia.append(pacientes)
              contadorpreferencialOrtopedia+=1


        print(listaPacienteComumDermatologia)
        print(listaPacienteComumEndocrinologia)
        print(listaPacienteComumEndocrinologia)

        print(listaPacientePrioritarioDermatologia)
        print(listaPacientePrioritarioEndocrinologia)
        print(listaPacientePrioritarioOrtopedia)

    elif(opcao==2):

        tamPrioritarioDermatologiaAtendido=len(listaPacientePrioritarioAtendidoDermatologia)
        tamPrioritarioEndocrinologiaAtendido=len(listaPacientePrioritarioAtendidoEndocrinologia)
        tamPrioritarioOrtopediaAtendido=len(listaPacientePrioritarioAtendidoOrtopedia)
        tamComumDermatologiaAtendido=len(listaPacienteComumAtendidoDermatologia)
        tamComumEndocrinologiaAtendido=len(listaPacienteComumAtendidoEndocrinologia)
        tamComumOrtopediaAtendido=len(listaPacienteComumAtendidoOrtopedia)

        ChamarPacienteParaAtendimento(paciente_em_antendimento_Dermatologia, paciente_em_antendimento_Endocrinologia,
                                      paciente_em_antendimento_Ortopedia, listaEsperaPacienteComumDermatologia,
                                      listaEsperaPacientePrioritarioDermatologia, listaEsperaPacienteComumEndocrinologia,
                                      listaEsperaPacientePrioritarioEndocrinologia, listaEsperaPacienteComumOrtopedia,
                                      listaEsperaPacientePrioritarioOrtopedia, tamComumDermatologiaAtendido,
                                      tamComumEndocrinologiaAtendido, tamComumOrtopediaAtendido,
                                      tamPrioritarioDermatologiaAtendido, tamPrioritarioEndocrinologiaAtendido,
                                      tamPrioritarioOrtopediaAtendido)
    elif(opcao==3):
        PularPaciente()
    elif(opcao==4):
        EncerrarConsulta()
    elif(opcao==5):
        ExibirFilaDeEspera()
    elif(opcao==6):
        ExibirPacientesAtendidosNoDia()
    elif(opcao==7):
        ExibirTempoMedioDeEsperaDosPacientes()
    elif(opcao==8):
        ExibirTempoMedioDeAtendimentoDosPacientes()
