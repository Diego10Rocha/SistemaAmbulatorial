#Esta função foi criada para gerar senhas para os pacientes por ordem de chegada
def gerarSenha(tipo, consultorio, contadorcomumDermatologia, contadorcomumEndocrinologia,
               contadorcomumOrtopedia, contadorpreferencialDermatologia,
               contadorpreferencialEndocrinologia, contadorpreferencialOrtopedia):

    if(tipo=="C" or tipo=="c"):
        if(consultorio=="d" or consultorio=="D"):
            if(contadorcomumDermatologia<10):
                senha="cd00"+str(contadorcomumDermatologia)

            elif(contadorcomumDermatologia>=10 and contadorcomumDermatologia<100):
                senha="cd0"+str(contadorcomumDermatologia)

            elif(contadorcomumDermatologia>=100):
                senha="cd"+str(contadorcomumDermatologia)

        elif(consultorio=="E" or consultorio=="e"):
            if(contadorcomumEndocrinologia<10):
                senha="ce00"+str(contadorcomumEndocrinologia)

            elif(contadorcomumEndocrinologia>=10 and contadorcomumEndocrinologia<100):
                senha="ce0"+str(contadorcomumEndocrinologia)

            elif(contadorcomumEndocrinologia>=100):
                senha="ce"+str(contadorcomumEndocrinologia)

        elif(consultorio=="O" or consultorio=="o"):
            if(contadorcomumOrtopedia<10):
                senha="co00"+str(contadorcomumOrtopedia)

            elif(contadorcomumOrtopedia>=10 and contadorcomumOrtopedia<100):
                senha="co0"+str(contadorcomumOrtopedia)

            elif(contadorcomumOrtopedia>=100):
                senha="co"+str(contadorcomumOrtopedia)

    else:
        if(consultorio=="d" or consultorio=="D"):
            if(contadorpreferencialDermatologia<10):
                senha="pd00"+str(contadorpreferencialDermatologia)

            elif(contadorpreferencialDermatologia>=10 and contadorpreferencialDermatologia<100):
                senha="pd0"+str(contadorpreferencialDermatologia)

            elif(contadorpreferencialDermatologia>=100):
                senha="pd"+str(contadorpreferencialDermatologia)

        elif(consultorio=="E" or consultorio=="e"):
            if(contadorpreferencialEndocrinologia<10):
                senha="pe00"+str(contadorpreferencialEndocrinologia)

            elif(contadorpreferencialEndocrinologia>=10 and contadorpreferencialEndocrinologia<100):
                senha="pe0"+str(contadorpreferencialEndocrinologia)

            elif(contadorpreferencialEndocrinologia>=100):
                senha="pe"+str(contadorpreferencialEndocrinologia)

        elif(consultorio=="O" or consultorio=="o"):
            if(contadorpreferencialOrtopedia<10):
                senha="po00"+str(contadorpreferencialOrtopedia)

            elif(contadorpreferencialOrtopedia>=10 and contadorpreferencialOrtopedia<100):
                senha="po0"+str(contadorpreferencialOrtopedia)

            elif(contadorpreferencialOrtopedia>=100):
                senha="po"+str(contadorpreferencialOrtopedia)

    return senha

#Esta função serve para verificar se um valor digitado é composto apenas por numeros
def VerificarInt(valor):
    if(valor.isdigit()):
        return True
    else:
      return False

#Esta função serve para validar a hora, visto que tem que ser um valor inteiro e estar no intervalo de 0 a 24
def SolicitarHora():
    print("Para inserir o horário você deve primeiro digitar a hora ex: são 12:40, então você deve digitar 12 e apertar enter\n"
                        "Depois você digita os minutos ex: são 12:40, então você deve digitar 40 e apertar enter")
    hora=input("Digite a hora\n")
    boolhora=VerificarInt(hora)
    boolh=False
    while True:
        while(boolhora):
            hora=int(hora)
            if(hora<=0 or hora>24):
                hora=input("Hora inserida inválida para inserir o horário você deve primeiro digitar a hora ex: são 12:40,\n"
                       "então você deve digitar 12 e apertar enter. OBS.: 0<=hora<=24\n")
                boolhora=VerificarInt(hora)
            else:
                boolh=True
                break
        if(boolh):
            break
        while not boolhora:
            hora=input("Hora inserida inválida para inserir o horário você deve primeiro digitar a hora ex: são 12:40,\n"
                       "então você deve digitar 12 e apertar enter\n")
            boolhora=VerificarInt(hora)
    return hora

#Esta função serve para validar o minuto da hora, visto que tem que ser um valor inteiro e estar no intervalo de 0 a 60
def SolicitarMinuto():
    minuto=input("Digite o minuto\n")
    boolminuto=VerificarInt(minuto)
    boolm=False
    while True:
        while(boolminuto):
            minuto=int(minuto)
            if(minuto<0 or minuto>60):
                minuto=input("Minuto inserido inválido para inserir o minuto você deve digitar o minuto ex: são 12:40,\n"
                       "então você deve digitar 40 e apertar enter. OBS.: 0<=minuto<=60\n")
                boolminuto=VerificarInt(minuto)
            else:
                boolm=True
                break
        if(boolm):
            break
        while(not boolminuto):
            minuto=input("Hora inserida inválida para inserir o horário você deve primeiro digitar a hora ex: são 12:40,\n"
                       "então você deve digitar 12 e apertar enter\n")
            boolminuto=VerificarInt(minuto)
    return minuto

#Esta função serve para validar a opção de entrada do menu, visto que tem que ser um valor inteiro e estar no intervalo de 1 a 9
def ValidarOpcao(boolOpcao, opcao):
    boolo=False
    while True:
        while(boolOpcao):
            opcao=int(opcao)
            if(opcao<0 and opcao>9):
                MENU()
                opcao=input("Digite uma opção válida\n")
                boolOpcao=VerificarInt(opcao)
            else:
                boolo=True
                break
        if(boolo):
            break
        while(not boolOpcao):
            MENU()
            opcao=input("Opção invalida, por favor escolha uma opção válida")
            boolOpcao=VerificarInt(opcao)
    return opcao

#Esta função serve para imprimir o menu
def MENU():

    print("##########################################################")
    print("#                         MENU                           #")
    print("##########################################################")
    print("#  [1] - Emitir nova senha                               #")
    print("#  [2] - Chamar paciente para atendimento                #")
    print("#  [3] - Pular paciente                                  #")
    print("#  [4] - Encerrar uma consulta realizada                 #")
    print("#  [5] - Exibir fila de espera                           #")
    print("#  [6] - Exibir pacientes atendidos no dia               #")
    print("#  [7] - Exibir tempo médio de espera dos pacientes      #")
    print("#  [8] - Exibir tempo médio de atendimento dos pacientes #")
    print("#  [9] - Encerrar programa                               #")
    print("##########################################################")

def EmitirSenha(contadorcomumDermatologia, contadorcomumEndocrinologia,
                contadorcomumOrtopedia, contadorpreferencialDermatologia,
                contadorpreferencialEndocrinologia, contadorpreferencialOrtopedia):

    #pacienteComum=[]
    #pacientePrioritario=[]
    tipo=input("Digite 'C' para paciente comum e 'P' para preferencial\n")
    while(tipo!="c" and tipo!="C" and tipo!="p" and tipo!="P"):
        tipo=input("Tipo inválido, digite 'C' para paciente comum e 'P' para preferencial\n")
    nome=input("Digite seu nome\n")
    while(nome==""):
        nome=input("Valor inválido. Digite seu nome\n")

    hora=SolicitarHora()
    minuto=SolicitarMinuto()
    consultorio=input("Digite o consultório de atendimento do paciente:\n"
                     "D - Dermatologia\n"
                     "E - Endocrinologia\n"
                     "O - Ortopedia\n")
    while(consultorio!="D" and consultorio!="d" and consultorio!="E" and consultorio!="e"
          and consultorio!="O" and consultorio!="o"):
     consultorio=input("Consultório digitado inválido, digite o consultório de atendimento do paciente:\n"
                     "D - Dermatologia\n"
                     "E - Endocrinologia\n"
                     "O - Ortopedia\n")
    senha=gerarSenha(tipo, consultorio, contadorcomumDermatologia, contadorcomumEndocrinologia, contadorcomumOrtopedia, contadorpreferencialDermatologia, contadorpreferencialEndocrinologia, contadorpreferencialOrtopedia)
    return [tipo, nome, hora, minuto, consultorio, senha]



def ChamarPacienteParaAtendimento(paciente_em_antendimento_Dermatologia, paciente_em_antendimento_Endocrinologia,
                                  paciente_em_antendimento_Ortopedia, listaEsperaPacienteComumDermatologia,
                                  listaEsperaPacientePrioritarioDermatologia, listaEsperaPacienteComumEndocrinologia,
                                  listaEsperaPacientePrioritarioEndocrinologia, listaEsperaPacienteComumOrtopedia,
                                  listaEsperaPacientePrioritarioOrtopedia, tamComumDermatologiaAtendido,
                                  tamComumEndocrinologiaAtendido, tamComumOrtopediaAtendido,
                                  tamPrioritarioDermatologiaAtendido, tamPrioritarioEndocrinologiaAtendido,
                                  tamPrioritarioOrtopediaAtendido):

    opcao=0
    hora_atendimento_Dermatologia=0
    minuto_atendimento_Dermatologia=0
    hora_atendimento_Endocrinologia=0
    minuto_atendimento_Endocrinologia=0
    hora_atendimento_Ortopedia=0
    minuto_atendimento_Ortopedia=0
    MSG="O paciente não compareceu, selecione a opção 3 para pular o paciente"
    comparecimento="n"
    while(opcao!="4"):
        print("##########################################################")
        print("#                         MENU                           #")
        print("##########################################################")
        print("#  [1] - Chamar para consultório de Dermatologia         #")
        print("#  [2] - Chamar para consultório de Endocrinologia       #")
        print("#  [3] - Chamar para consultório de Ortopedia            #")
        print("#  [4] - SAIR                                            #")
        print("##########################################################")
        opcao=input("Escolha uma opção: \n")

        if(opcao=="1"):
            if(not paciente_em_antendimento_Dermatologia and
                    (listaEsperaPacientePrioritarioDermatologia or listaEsperaPacienteComumDermatologia)):
                while(comparecimento=="n" or comparecimento=="N"):
                    if(tamComumDermatologiaAtendido>tamPrioritarioDermatologiaAtendido):
                        print("Próxima senha do consultório de DERMATOLOGIA:")
                        print(listaEsperaPacientePrioritarioDermatologia[0][5], "-", listaEsperaPacientePrioritarioDermatologia[0][1],
                              "- Consultório de Dermatologia")
                        comparecimento=input("O paciente compareceu? Digite 'N' para voltar ao menu e pular paciente. "
                                    "Digite 'S' para continuar com o atendimento")
                        if(comparecimento=="S" or comparecimento=="s"):
                            paciente_em_antendimento_Dermatologia=listaEsperaPacientePrioritarioOrtopedia[0]
                            hora_atendimento_Dermatologia=SolicitarHora()
                            minuto_atendimento_Dermatologia=SolicitarMinuto()
                            paciente_em_antendimento_Dermatologia.append(hora_atendimento_Dermatologia)
                            paciente_em_antendimento_Dermatologia.append(minuto_atendimento_Dermatologia)
                            listaEsperaPacientePrioritarioDermatologia.pop(0)
                        else:
                            print(MSG)
                            break
                    elif(not paciente_em_antendimento_Dermatologia and listaEsperaPacienteComumDermatologia):
                        print("Próxima senha do consultório de DERMATOLOGIA:")
                        print(listaEsperaPacienteComumDermatologia[0][5], "-", listaEsperaPacienteComumDermatologia[0][1],
                              "- Consultório de Dermatologia")
                        comparecimento=input("O paciente compareceu? Digite 'N' para voltar ao menu e pular paciente. "
                                    "Digite 'S' para continuar com o atendimento")
                        if(comparecimento=="S" or comparecimento=="s"):
                            paciente_em_antendimento_Dermatologia=listaEsperaPacienteComumDermatologia[0]
                            hora_atendimento_Dermatologia=SolicitarHora()
                            minuto_atendimento_Dermatologia=SolicitarMinuto()
                            paciente_em_antendimento_Dermatologia.append(hora_atendimento_Dermatologia)
                            paciente_em_antendimento_Dermatologia.append(minuto_atendimento_Dermatologia)
                            listaEsperaPacienteComumDermatologia.pop(0)
                        else:
                            print(MSG)
                            break
            else:
                print("Não há pacientes na lista de espera de dermatologia")
        elif(opcao=="2"):
            if(not paciente_em_antendimento_Endocrinologia and listaEsperaPacienteComumEndocrinologia and
                    listaEsperaPacientePrioritarioEndocrinologia):
                if(tamComumEndocrinologiaAtendido>tamPrioritarioEndocrinologiaAtendido):
                    print("Próxima senha do consultório de ENDOCRINOLOGIA:")
                    print(listaEsperaPacientePrioritarioEndocrinologia[0][5], "-" , listaEsperaPacientePrioritarioEndocrinologia[0][1],
                          "- Consultório de Endocrinologia")
                    comparecimento=input("O paciente compareceu? Digite 'N' para voltar ao menu e pular paciente. "
                                "Digite 'S' para continuar com o atendimento")
                    if(comparecimento=="S" or comparecimento=="s"):
                        paciente_em_antendimento_Endocrinologia=listaEsperaPacientePrioritarioEndocrinologia[0]
                        hora_atendimento_Endocrinologia=SolicitarHora()
                        minuto_atendimento_Endocrinologia=SolicitarMinuto()
                        paciente_em_antendimento_Endocrinologia.append(hora_atendimento_Endocrinologia)
                        paciente_em_antendimento_Endocrinologia.append(minuto_atendimento_Endocrinologia)
                        listaEsperaPacientePrioritarioEndocrinologia.pop(0)
                    else:
                        print(MSG)
                        break
                else:
                    print("Próxima senha do consultório de ENDOCRINOLOGIA:")
                    print(listaEsperaPacienteComumEndocrinologia[0][5], "-", listaEsperaPacienteComumEndocrinologia[0][1],
                          "- Consultório de Endocrinologia")
                    comparecimento=input("O paciente compareceu? Digite 'N' para voltar ao menu e pular paciente. "
                                "Digite 'S' para continuar com o atendimento")
                    if(comparecimento=="S" or comparecimento=="s"):
                        paciente_em_antendimento_Endocrinologia=listaEsperaPacientePrioritarioEndocrinologia[0]
                        hora_atendimento_Endocrinologia=SolicitarHora()
                        minuto_atendimento_Endocrinologia=SolicitarMinuto()
                        paciente_em_antendimento_Endocrinologia.append(hora_atendimento_Endocrinologia)
                        paciente_em_antendimento_Endocrinologia.append(minuto_atendimento_Endocrinologia)
                        listaEsperaPacienteComumEndocrinologia.pop(0)
                    else:
                        print(MSG)
                        break
            else:
                print("Não há pacientes na lista de espera de endocrinologia")
        elif(opcao=="3"):
            if(not paciente_em_antendimento_Ortopedia and listaEsperaPacienteComumOrtopedia
                    and listaEsperaPacientePrioritarioOrtopedia):
                if(tamComumOrtopediaAtendido>tamPrioritarioOrtopediaAtendido):
                    print("Próxima senha do consultório de ORTOPEDIA:")
                    print(listaEsperaPacientePrioritarioOrtopedia[0][5], "-", listaEsperaPacientePrioritarioOrtopedia[0][1],
                          "- Consultório de Ortopedia")
                    comparecimento=input("O paciente compareceu? Digite 'N' para voltar ao menu e pular paciente. "
                                "Digite 'S' para continuar com o atendimento")
                    if(comparecimento=="S" or comparecimento=="s"):
                        paciente_em_antendimento_Ortopedia=listaEsperaPacientePrioritarioOrtopedia[0]
                        hora_atendimento_Ortopedia=SolicitarHora()
                        minuto_atendimento_Ortopedia=SolicitarMinuto()
                        paciente_em_antendimento_Ortopedia.append(hora_atendimento_Ortopedia)
                        paciente_em_antendimento_Ortopedia.append(minuto_atendimento_Ortopedia)
                        listaEsperaPacientePrioritarioOrtopedia.pop(0)
                    else:
                        print(MSG)
                        break
                else:
                    print("Próxima senha do consultório de ORTOPEDIA:")
                    print(listaEsperaPacienteComumOrtopedia[0][5], "-", listaEsperaPacienteComumOrtopedia[0][1],
                          "- Consultório de Ortopedia")
                    comparecimento=input("O paciente compareceu? Digite 'N' para voltar ao menu e pular paciente. "
                                "Digite 'S' para continuar com o atendimento")
                    if(comparecimento=="S" or comparecimento=="s"):
                        paciente_em_antendimento_Ortopedia=listaEsperaPacientePrioritarioOrtopedia[0]
                        hora_atendimento_Ortopedia=SolicitarHora()
                        minuto_atendimento_Ortopedia=SolicitarMinuto()
                        paciente_em_antendimento_Ortopedia.append(hora_atendimento_Ortopedia)
                        paciente_em_antendimento_Ortopedia.append(minuto_atendimento_Ortopedia)
                        listaEsperaPacienteComumOrtopedia.pop(0)
                    else:
                        print(MSG)
                        break
        else:
            print("Não há pacientes na lista de espera de ortopedia")
        return paciente_em_antendimento_Ortopedia, paciente_em_antendimento_Endocrinologia, \
               paciente_em_antendimento_Dermatologia, hora_atendimento_Dermatologia, \
               minuto_atendimento_Dermatologia, hora_atendimento_Endocrinologia, \
               minuto_atendimento_Endocrinologia, hora_atendimento_Ortopedia, \
               minuto_atendimento_Ortopedia, listaEsperaPacienteComumDermatologia, \
               listaEsperaPacientePrioritarioDermatologia, listaEsperaPacienteComumEndocrinologia, \
               listaEsperaPacientePrioritarioEndocrinologia, listaEsperaPacienteComumOrtopedia, \
               listaEsperaPacientePrioritarioOrtopedia


def PularPaciente(dados_Pacientes, excluir_Paciente, listaEspera):

    del dados_Pacientes[excluir_Paciente]
    for i in range (len(listaEspera)):
        for x in range (len(listaEspera[i])):
            if(listaEspera[i]==excluir_Paciente):
                listaEspera[i].pop(x)
    return dados_Pacientes, listaEspera
def EncerrarConsulta(paciente_em_antendimento_Dermatologia, paciente_em_antendimento_Endocrinologia,
                    paciente_em_antendimento_Ortopedia, listaPacienteComumAtendidoDermatologia,
                    listaPacienteComumAtendidoEndocrinologia, listaPacienteComumAtendidoOrtopedia,
                    listaPacientePrioritarioAtendidoDermatologia, listaPacientePrioritarioAtendidoEndocrinologia,
                    listaPacientePrioritarioAtendidoOrtopedia, dados_Pacientes):
    opcao="0"
    while(opcao!="4"):
        print("################################################################")
        print("#                           MENU                               #")
        print("################################################################")
        print("#  [1] - Encerrar consulta do consultório de Dermatologia      #")
        print("#  [2] - Encerrar consulta do consultório de Endocrinologia    #")
        print("#  [3] - Encerrar consulta do consultório de Ortopedia         #")
        print("#  [4] - SAIR                                                  #")
        print("################################################################")
        opcao=input("Escolha uma opção: \n")
        hora=0
        minuto=0
        senha=""
        if(opcao=="1"):
            senha=paciente_em_antendimento_Dermatologia[5]
            if(paciente_em_antendimento_Dermatologia[5][0]=="c" or paciente_em_antendimento_Dermatologia[5][0]=="C"):
                listaPacienteComumAtendidoDermatologia.append(paciente_em_antendimento_Dermatologia)
                paciente_em_antendimento_Dermatologia.pop(0)
                hora=SolicitarHora()
                minuto=SolicitarMinuto()
                tamLista=len(listaPacienteComumAtendidoDermatologia)
                listaPacienteComumAtendidoDermatologia[tamLista-1].append(hora)
                listaPacienteComumAtendidoDermatologia[tamLista-1].append(minuto)
            else:
                listaPacientePrioritarioAtendidoDermatologia.append(paciente_em_antendimento_Dermatologia)
                paciente_em_antendimento_Dermatologia.pop(0)
                hora=SolicitarHora()
                minuto=SolicitarMinuto()
                tamLista=len(listaPacienteComumAtendidoDermatologia)
                listaPacientePrioritarioAtendidoDermatologia[tamLista-1].append(hora)
                listaPacientePrioritarioAtendidoDermatologia[tamLista-1].append(minuto)
        elif(opcao=="2"):
            senha=paciente_em_antendimento_Endocrinologia
            if(paciente_em_antendimento_Endocrinologia[5][0]=="c" or paciente_em_antendimento_Endocrinologia[5][0]=="C"):
                listaPacienteComumAtendidoEndocrinologia.append(paciente_em_antendimento_Endocrinologia)
                paciente_em_antendimento_Endocrinologia.pop(0)
                hora=SolicitarHora()
                minuto=SolicitarMinuto()
                tamLista=len(listaPacienteComumAtendidoEndocrinologia)
                listaPacienteComumAtendidoEndocrinologia[tamLista-1].append(hora)
                listaPacienteComumAtendidoEndocrinologia[tamLista-1].append(minuto)
            else:
                listaPacientePrioritarioAtendidoEndocrinologia.append(paciente_em_antendimento_Endocrinologia)
                paciente_em_antendimento_Endocrinologia.pop(0)
                hora=SolicitarHora()
                minuto=SolicitarMinuto()
                tamLista=len(listaPacientePrioritarioAtendidoEndocrinologia)
                listaPacientePrioritarioAtendidoEndocrinologia[tamLista-1].append(hora)
                listaPacientePrioritarioAtendidoEndocrinologia[tamLista-1].append(minuto)
        elif(opcao=="3"):
            senha=paciente_em_antendimento_Ortopedia
            if(paciente_em_antendimento_Ortopedia[5][0]=="c" or paciente_em_antendimento_Ortopedia[5][0]=="C"):
                listaPacienteComumAtendidoOrtopedia.append(paciente_em_antendimento_Ortopedia)
                paciente_em_antendimento_Ortopedia.pop(0)
                hora=SolicitarHora()
                minuto=SolicitarMinuto()
                tamLista=len(listaPacienteComumAtendidoOrtopedia)
                listaPacienteComumAtendidoOrtopedia[tamLista-1].append(hora)
                listaPacienteComumAtendidoOrtopedia[tamLista-1].append(minuto)
            else:
                listaPacientePrioritarioAtendidoOrtopedia.append(paciente_em_antendimento_Ortopedia)
                paciente_em_antendimento_Ortopedia.pop(0)
                hora=SolicitarHora()
                minuto=SolicitarMinuto()
                tamLista=len(listaPacientePrioritarioAtendidoOrtopedia)
                listaPacientePrioritarioAtendidoOrtopedia[tamLista-1].append(hora)
                listaPacientePrioritarioAtendidoOrtopedia[tamLista-1].append(minuto)
        dados_Pacientes[senha].append(hora)
        dados_Pacientes[senha].append(minuto)

        return paciente_em_antendimento_Dermatologia, paciente_em_antendimento_Endocrinologia,\
               paciente_em_antendimento_Ortopedia, listaPacienteComumAtendidoDermatologia,\
               listaPacienteComumAtendidoEndocrinologia, listaPacienteComumAtendidoOrtopedia,\
               listaPacientePrioritarioAtendidoDermatologia, listaPacientePrioritarioAtendidoEndocrinologia,\
               listaPacientePrioritarioAtendidoOrtopedia, dados_Pacientes


    print("Esta função serve para encerrar uma consulta")

def ExibirFilaDeEspera():
    print("Esta função serve para exibir as filas de espera do ambulatorio")

def ExibirPacientesAtendidosNoDia():
    print("Esta função serve para exibir pacientes atendidos no dia")

def ExibirTempoMedioDeEsperaDosPacientes():
    print("Esta funções serve para exibir o tempo medio de espera dos pacientes")

def ExibirTempoMedioDeAtendimentoDosPacientes():
    print("Esta função serve para exibir tempo médio de atendimento dos pacientes")
