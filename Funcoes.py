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

def VariacaoDeTempo(hora_inicio, minuto_inicio, hora_final, minuto_final):
    minuto_inicio=minuto_inicio+(hora_inicio*60)
    minuto_final=minuto_final+(hora_final*60)
    variacao=0
    if(minuto_final>minuto_inicio):
        variacao=minuto_final-minuto_inicio
    else:
        variacao=(24*60-minuto_inicio)+minuto_final
    hora_total=variacao//60
    minuto_total=(variacao%60)
    return hora_total, minuto_total

def Gerar_Tabela_Pacientes_Em_Espera(tabela, lista_Pacientes_Espera, hora, minuto):
    for i in range(len(lista_Pacientes_Espera)):
        hora_espera_na_fila, minuto_espera_na_fila=VariacaoDeTempo(lista_Pacientes_Espera[i][2], lista_Pacientes_Espera[i][3],
                                                   hora, minuto)
        tempo_espera_na_fila=str(hora_espera_na_fila)+" h : "+str(minuto_espera_na_fila)+" min"
        if(lista_Pacientes_Espera[i][4]=="d" or lista_Pacientes_Espera[i][4]=="D"):
            tabela.add_row([lista_Pacientes_Espera[i][5], lista_Pacientes_Espera[i][1], "Dermatologia", "Em espera", tempo_espera_na_fila])
        elif(lista_Pacientes_Espera[i][4]=="e" or lista_Pacientes_Espera[i][4]=="E"):
            tabela.add_row([lista_Pacientes_Espera[i][5], lista_Pacientes_Espera[i][1], "Endocrinologia", "Em espera", tempo_espera_na_fila])
        else:
            tabela.add_row([lista_Pacientes_Espera[i][5], lista_Pacientes_Espera[i][1], "Ortopedia", "Em espera", tempo_espera_na_fila])

    return tabela

def Gerar_Tabela_Pacientes_Atendidos(tabela, lista_Pacientes_Atendidos):
    for i in range(len(lista_Pacientes_Atendidos)):
        hora_espera_na_fila, minuto_espera_na_fila=VariacaoDeTempo(lista_Pacientes_Atendidos[i][2], lista_Pacientes_Atendidos[i][3],
                                             lista_Pacientes_Atendidos[i][6], lista_Pacientes_Atendidos[i][7])
        tempo_espera_na_fila=str(hora_espera_na_fila)+" h : "+str(minuto_espera_na_fila)+" min"
        hora_atendimento, minuto_atendimento=VariacaoDeTempo(lista_Pacientes_Atendidos[i][6], lista_Pacientes_Atendidos[i][7],
                                          lista_Pacientes_Atendidos[i][8], lista_Pacientes_Atendidos[i][9])
        tempo_atendimento=str(hora_atendimento)+" h : "+str(minuto_atendimento)+" min"
        if(lista_Pacientes_Atendidos[i][4]=="d" or lista_Pacientes_Atendidos[i][4]=="D"):
            tabela.add_row([lista_Pacientes_Atendidos[i][1], tempo_espera_na_fila, tempo_atendimento, "Dermatologia", "Dra. Silvia Melo"])
        elif(lista_Pacientes_Atendidos[i][4]=="e" or lista_Pacientes_Atendidos[i][4]=="E"):
            tabela.add_row([lista_Pacientes_Atendidos[i][1], tempo_espera_na_fila, tempo_atendimento, "Endocrinologia", "Dr. Fernando Santos"])
        else:
            tabela.add_row([lista_Pacientes_Atendidos[i][1], tempo_espera_na_fila, tempo_atendimento, "Ortopedia", "Dra. Maria do Carmo Silva"])

    return tabela

def Gerar_Tabela_Pacientes_Em_Atendimento(tabela, lista_Pacientes_Atendimento):
    if(lista_Pacientes_Atendimento):
        hora_espera_na_fila, minuto_espera_na_fila=VariacaoDeTempo(lista_Pacientes_Atendimento[2], lista_Pacientes_Atendimento[3],
                                                   lista_Pacientes_Atendimento[6], lista_Pacientes_Atendimento[7])
        tempo_espera_na_fila=str(hora_espera_na_fila)+" h : "+str(minuto_espera_na_fila)+" min"

        if(lista_Pacientes_Atendimento[4]=="d" or lista_Pacientes_Atendimento[4]=="D"):
            tabela.add_row([lista_Pacientes_Atendimento[5], lista_Pacientes_Atendimento[1], "Dermatologia", "Em atendimento", tempo_espera_na_fila])
        elif(lista_Pacientes_Atendimento[4]=="e" or lista_Pacientes_Atendimento[4]=="E"):
            tabela.add_row([lista_Pacientes_Atendimento[5], lista_Pacientes_Atendimento[1], "Endocrinologia", "Em atendimento", tempo_espera_na_fila])
        else:
            tabela.add_row([lista_Pacientes_Atendimento[5], lista_Pacientes_Atendimento[1], "Ortopedia", "Em atendimento", tempo_espera_na_fila])

    return tabela

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
                                  tamPrioritarioOrtopediaAtendido, dados_Pacientes):

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
            while(comparecimento=="n" or comparecimento=="N"):
                if(not paciente_em_antendimento_Dermatologia and
                        (listaEsperaPacientePrioritarioDermatologia or listaEsperaPacienteComumDermatologia)):

                    if((tamComumDermatologiaAtendido>=tamPrioritarioDermatologiaAtendido and listaEsperaPacientePrioritarioDermatologia) or not listaEsperaPacienteComumDermatologia):
                        print("Próxima senha do consultório de DERMATOLOGIA:")
                        print(listaEsperaPacientePrioritarioDermatologia[0][5], "-", listaEsperaPacientePrioritarioDermatologia[0][1],
                              "- Consultório de Dermatologia")
                        comparecimento=input("O paciente compareceu? Digite 'N' para pular o paciente e chamar o proximo. "
                                    "Digite 'S' para continuar com o atendimento")
                        if(comparecimento=="S" or comparecimento=="s"):
                            paciente_em_antendimento_Dermatologia=listaEsperaPacientePrioritarioDermatologia[0]
                            hora_atendimento_Dermatologia=SolicitarHora()
                            minuto_atendimento_Dermatologia=SolicitarMinuto()
                            paciente_em_antendimento_Dermatologia.append(hora_atendimento_Dermatologia)
                            paciente_em_antendimento_Dermatologia.append(minuto_atendimento_Dermatologia)
                            listaEsperaPacientePrioritarioDermatologia.pop(0)
                        else:
                            dados_Pacientes, listaEsperaPacientePrioritarioDermatologia=\
                                PularPaciente(dados_Pacientes, listaEsperaPacientePrioritarioDermatologia[0][5],
                                              listaEsperaPacientePrioritarioDermatologia)

                    elif(listaEsperaPacienteComumDermatologia):
                        print("Próxima senha do consultório de DERMATOLOGIA:")
                        print(listaEsperaPacienteComumDermatologia[0][5], "-", listaEsperaPacienteComumDermatologia[0][1],
                              "- Consultório de Dermatologia")
                        comparecimento=input("O paciente compareceu? Digite 'N' para pular o paciente e chamar o próximo. "
                                    "Digite 'S' para continuar com o atendimento")
                        if(comparecimento=="S" or comparecimento=="s"):
                            paciente_em_antendimento_Dermatologia=listaEsperaPacienteComumDermatologia[0]
                            hora_atendimento_Dermatologia=SolicitarHora()
                            minuto_atendimento_Dermatologia=SolicitarMinuto()
                            paciente_em_antendimento_Dermatologia.append(hora_atendimento_Dermatologia)
                            paciente_em_antendimento_Dermatologia.append(minuto_atendimento_Dermatologia)
                            listaEsperaPacienteComumDermatologia.pop(0)
                        else:
                            dados_Pacientes, listaEsperaPacienteComumDermatologia=\
                                PularPaciente(dados_Pacientes,listaEsperaPacienteComumDermatologia[0][5],
                                              listaEsperaPacienteComumDermatologia)
                else:
                    print("Não há pacientes na lista de espera de dermatologia, ou já possui um paciente sendo atendido")
                    break
        elif(opcao=="2"):
            while(comparecimento=="n" or comparecimento=="N"):
                if(not paciente_em_antendimento_Endocrinologia and (listaEsperaPacienteComumEndocrinologia or
                        listaEsperaPacientePrioritarioEndocrinologia)):

                    if((tamComumEndocrinologiaAtendido>=tamPrioritarioEndocrinologiaAtendido and listaEsperaPacientePrioritarioEndocrinologia)
                            or not listaEsperaPacienteComumEndocrinologia):
                        print("Próxima senha do consultório de ENDOCRINOLOGIA:")
                        print(listaEsperaPacientePrioritarioEndocrinologia[0][5], "-" , listaEsperaPacientePrioritarioEndocrinologia[0][1],
                              "- Consultório de Endocrinologia")
                        comparecimento=input("O paciente compareceu? Digite 'N' para pular o paciente e chamar o próximo. "
                                    "Digite 'S' para continuar com o atendimento")
                        if(comparecimento=="S" or comparecimento=="s"):
                            paciente_em_antendimento_Endocrinologia=listaEsperaPacientePrioritarioEndocrinologia[0]
                            hora_atendimento_Endocrinologia=SolicitarHora()
                            minuto_atendimento_Endocrinologia=SolicitarMinuto()
                            paciente_em_antendimento_Endocrinologia.append(hora_atendimento_Endocrinologia)
                            paciente_em_antendimento_Endocrinologia.append(minuto_atendimento_Endocrinologia)
                            listaEsperaPacientePrioritarioEndocrinologia.pop(0)
                        else:
                            dados_Pacientes, listaEsperaPacientePrioritarioEndocrinologia=\
                                PularPaciente(dados_Pacientes, listaEsperaPacientePrioritarioEndocrinologia[0][5],
                                              listaEsperaPacientePrioritarioEndocrinologia)
                    elif(listaEsperaPacienteComumEndocrinologia):
                        print("Próxima senha do consultório de ENDOCRINOLOGIA:")
                        print(listaEsperaPacienteComumEndocrinologia[0][5], "-", listaEsperaPacienteComumEndocrinologia[0][1],
                              "- Consultório de Endocrinologia")
                        comparecimento=input("O paciente compareceu? Digite 'N' para pular o paciente e chamar o próximo. "
                                    "Digite 'S' para continuar com o atendimento")
                        if(comparecimento=="S" or comparecimento=="s"):
                            paciente_em_antendimento_Endocrinologia=listaEsperaPacienteComumEndocrinologia[0]
                            hora_atendimento_Endocrinologia=SolicitarHora()
                            minuto_atendimento_Endocrinologia=SolicitarMinuto()
                            paciente_em_antendimento_Endocrinologia.append(hora_atendimento_Endocrinologia)
                            paciente_em_antendimento_Endocrinologia.append(minuto_atendimento_Endocrinologia)
                            listaEsperaPacienteComumEndocrinologia.pop(0)
                        else:
                            dados_Pacientes, listaEsperaPacienteComumEndocrinologia=\
                                PularPaciente(dados_Pacientes, listaEsperaPacienteComumEndocrinologia[0][5],
                                              listaEsperaPacienteComumEndocrinologia)
                else:
                    print("Não há pacientes na lista de espera de endocrinologia, ou já possui um paciente sendo atendido")
                    break
        elif(opcao=="3"):
            while(comparecimento=="n" or comparecimento=="N"):
                if(not paciente_em_antendimento_Ortopedia and (listaEsperaPacienteComumOrtopedia
                        or listaEsperaPacientePrioritarioOrtopedia)):

                    if((tamComumOrtopediaAtendido>=tamPrioritarioOrtopediaAtendido and listaEsperaPacientePrioritarioOrtopedia) or not listaEsperaPacienteComumOrtopedia):
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
                            dados_Pacientes, listaEsperaPacientePrioritarioOrtopedia=\
                                PularPaciente(dados_Pacientes, listaEsperaPacientePrioritarioOrtopedia[0][5],
                                              listaEsperaPacientePrioritarioOrtopedia)
                    elif(listaEsperaPacienteComumOrtopedia):
                        print("Próxima senha do consultório de ORTOPEDIA:")
                        print(listaEsperaPacienteComumOrtopedia[0][5], "-", listaEsperaPacienteComumOrtopedia[0][1],
                              "- Consultório de Ortopedia")
                        comparecimento=input("O paciente compareceu? Digite 'N' para voltar ao menu e pular paciente. "
                                    "Digite 'S' para continuar com o atendimento")
                        if(comparecimento=="S" or comparecimento=="s"):
                            paciente_em_antendimento_Ortopedia=listaEsperaPacienteComumOrtopedia[0]
                            hora_atendimento_Ortopedia=SolicitarHora()
                            minuto_atendimento_Ortopedia=SolicitarMinuto()
                            paciente_em_antendimento_Ortopedia.append(hora_atendimento_Ortopedia)
                            paciente_em_antendimento_Ortopedia.append(minuto_atendimento_Ortopedia)
                            listaEsperaPacienteComumOrtopedia.pop(0)
                        else:
                            dados_Pacientes, listaEsperaPacienteComumOrtopedia=\
                                PularPaciente(dados_Pacientes, listaEsperaPacienteComumOrtopedia[0][5],
                                              listaEsperaPacienteComumOrtopedia)
                else:
                    print("Não há pacientes na lista de espera de ortopedia, ou já possui um paciente sendo atendido")
                    break
        return paciente_em_antendimento_Ortopedia, paciente_em_antendimento_Endocrinologia, \
               paciente_em_antendimento_Dermatologia, hora_atendimento_Dermatologia, \
               minuto_atendimento_Dermatologia, hora_atendimento_Endocrinologia, \
               minuto_atendimento_Endocrinologia, hora_atendimento_Ortopedia, \
               minuto_atendimento_Ortopedia, listaEsperaPacienteComumDermatologia, \
               listaEsperaPacientePrioritarioDermatologia, listaEsperaPacienteComumEndocrinologia, \
               listaEsperaPacientePrioritarioEndocrinologia, listaEsperaPacienteComumOrtopedia, \
               listaEsperaPacientePrioritarioOrtopedia, dados_Pacientes


def PularPaciente(dados_Pacientes, excluir_Paciente, listaEspera):

    del dados_Pacientes[excluir_Paciente]
    for i in range (len(listaEspera)):
        if(listaEspera[i][5]==excluir_Paciente):
            listaEspera.pop(i)
            break
    print("Paciente excluido do banco de dados")
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

        if(opcao=="1"):
            if(paciente_em_antendimento_Dermatologia):
                if(paciente_em_antendimento_Dermatologia[0]=="c" or paciente_em_antendimento_Dermatologia[0]=="C"):
                    listaPacienteComumAtendidoDermatologia.append(paciente_em_antendimento_Dermatologia)
                    paciente_em_antendimento_Dermatologia=[]
                    hora=SolicitarHora()
                    minuto=SolicitarMinuto()
                    tamLista=len(listaPacienteComumAtendidoDermatologia)
                    listaPacienteComumAtendidoDermatologia[tamLista-1].append(hora)
                    listaPacienteComumAtendidoDermatologia[tamLista-1].append(minuto)
                else:
                    listaPacientePrioritarioAtendidoDermatologia.append(paciente_em_antendimento_Dermatologia)
                    paciente_em_antendimento_Dermatologia=[]
                    hora=SolicitarHora()
                    minuto=SolicitarMinuto()
                    tamLista=len(listaPacienteComumAtendidoDermatologia)
                    listaPacientePrioritarioAtendidoDermatologia[tamLista-1].append(hora)
                    listaPacientePrioritarioAtendidoDermatologia[tamLista-1].append(minuto)
            break
        elif(opcao=="2"):
            if(paciente_em_antendimento_Endocrinologia):
                if(paciente_em_antendimento_Endocrinologia[5]=="c" or paciente_em_antendimento_Endocrinologia[5]=="C"):
                    Paciente_Encerrar=paciente_em_antendimento_Endocrinologia
                    listaPacienteComumAtendidoEndocrinologia.append(Paciente_Encerrar)
                    paciente_em_antendimento_Endocrinologia=[]
                    hora=SolicitarHora()
                    minuto=SolicitarMinuto()
                    tamLista=len(listaPacienteComumAtendidoEndocrinologia)
                    listaPacienteComumAtendidoEndocrinologia[tamLista-1].append(hora)
                    listaPacienteComumAtendidoEndocrinologia[tamLista-1].append(minuto)
                else:
                    Paciente_Encerrar=paciente_em_antendimento_Endocrinologia
                    listaPacientePrioritarioAtendidoEndocrinologia.append(Paciente_Encerrar)
                    paciente_em_antendimento_Endocrinologia=[]
                    hora=SolicitarHora()
                    minuto=SolicitarMinuto()
                    tamLista=len(listaPacientePrioritarioAtendidoEndocrinologia)
                    listaPacientePrioritarioAtendidoEndocrinologia[tamLista-1].append(hora)
                    listaPacientePrioritarioAtendidoEndocrinologia[tamLista-1].append(minuto)
            break
        elif(opcao=="3"):
            if(paciente_em_antendimento_Ortopedia):
                if(paciente_em_antendimento_Ortopedia[5]=="c" or paciente_em_antendimento_Ortopedia[5]=="C"):
                    Paciente_Encerrar=paciente_em_antendimento_Ortopedia
                    listaPacienteComumAtendidoOrtopedia.append(Paciente_Encerrar)
                    paciente_em_antendimento_Ortopedia=[]
                    hora=SolicitarHora()
                    minuto=SolicitarMinuto()
                    tamLista=len(listaPacienteComumAtendidoOrtopedia)
                    listaPacienteComumAtendidoOrtopedia[tamLista-1].append(hora)
                    listaPacienteComumAtendidoOrtopedia[tamLista-1].append(minuto)
                else:
                    Paciente_Encerrar=paciente_em_antendimento_Ortopedia
                    listaPacientePrioritarioAtendidoOrtopedia.append(Paciente_Encerrar)
                    paciente_em_antendimento_Ortopedia=[]
                    hora=SolicitarHora()
                    minuto=SolicitarMinuto()
                    tamLista=len(listaPacientePrioritarioAtendidoOrtopedia)
                    listaPacientePrioritarioAtendidoOrtopedia[tamLista-1].append(hora)
                    listaPacientePrioritarioAtendidoOrtopedia[tamLista-1].append(minuto)
            break

    return paciente_em_antendimento_Dermatologia, paciente_em_antendimento_Endocrinologia,\
           paciente_em_antendimento_Ortopedia, listaPacienteComumAtendidoDermatologia,\
           listaPacienteComumAtendidoEndocrinologia, listaPacienteComumAtendidoOrtopedia,\
           listaPacientePrioritarioAtendidoDermatologia, listaPacientePrioritarioAtendidoEndocrinologia,\
           listaPacientePrioritarioAtendidoOrtopedia, dados_Pacientes



def ExibirFilaDeEspera(paciente_em_atendimento_Dermatologia, paciente_em_antendimento_Endocrinologia,
                        paciente_em_antendimento_Ortopedia, listaEsperaPacienteComumDermatologia,
                        listaEsperaPacientePrioritarioDermatologia, listaEsperaPacienteComumEndocrinologia,
                        listaEsperaPacientePrioritarioEndocrinologia, listaEsperaPacienteComumOrtopedia,
                        listaEsperaPacientePrioritarioOrtopedia):
    hora=SolicitarHora()
    minuto=SolicitarMinuto()
    from prettytable import PrettyTable
    x = PrettyTable(["Senha", "Nome do paciente", "Consultório", "Situação", "Tempo de espera"])

    # Alinha as colunas
    x.align["Senha"] = "l"
    x.align["Nome do paciente"] = "l"
    x.align["Consultório"]="r"
    x.align["Situação"] = "r"
    x.align["Tempo de espera"] = "r"

    # Deixa um espaço entre a borda das colunas e o conteúdo (default)
    x.padding_width = 1
    '''
    #Inserindo na tabela listas de espera de dermatologia
    if(paciente_em_atendimento_Dermatologia):
        hora_total, minuto_total=VariacaoDeTempo(paciente_em_atendimento_Dermatologia[2], paciente_em_atendimento_Dermatologia[3],
                                                 paciente_em_atendimento_Dermatologia[6], paciente_em_atendimento_Dermatologia[7])
        horaFormatada=str(hora_total)+" h : "+str(minuto_total)+" min"

        x.add_row([paciente_em_atendimento_Dermatologia[5], paciente_em_atendimento_Dermatologia[1], "Dermatologia", "Em atendimento", horaFormatada])
    for i in range(len(listaEsperaPacientePrioritarioDermatologia)):
        hora_total, minuto_total=VariacaoDeTempo(listaEsperaPacientePrioritarioDermatologia[i][2], listaEsperaPacientePrioritarioDermatologia[i][3],
                                                 hora, minuto)
        horaFormatada=str(hora_total)+" h : "+str(minuto_total)+" min"
        x.add_row([listaEsperaPacientePrioritarioDermatologia[i][5], listaEsperaPacientePrioritarioDermatologia[i][1], "Dermatologia", "Em espera", horaFormatada])
    for i in range(len(listaEsperaPacienteComumDermatologia)):
        hora_total, minuto_total=VariacaoDeTempo(listaEsperaPacienteComumDermatologia[i][2], listaEsperaPacienteComumDermatologia[i][3],
                                                 hora, minuto)
        horaFormatada=str(hora_total)+" h : "+str(minuto_total)+" min"
        x.add_row([listaEsperaPacienteComumDermatologia[i][5], listaEsperaPacienteComumDermatologia[i][1], "Dermatologia", "Em espera", horaFormatada])

    #Inserindo na tabela listas de espera de Endocrinologia
    if(paciente_em_antendimento_Endocrinologia):
        hora_total, minuto_total=VariacaoDeTempo(paciente_em_antendimento_Endocrinologia[2], paciente_em_antendimento_Endocrinologia[3],
                                                 paciente_em_antendimento_Endocrinologia[6], paciente_em_antendimento_Endocrinologia[7])
        horaFormatada=str(hora_total)+" h : "+str(minuto_total)+" min"

        x.add_row([paciente_em_antendimento_Endocrinologia[5], paciente_em_antendimento_Endocrinologia[1], "Endocrinologia", "Em atendimento", horaFormatada])
    for i in range(len(listaEsperaPacientePrioritarioEndocrinologia)):
        hora_total, minuto_total=VariacaoDeTempo(listaEsperaPacientePrioritarioEndocrinologia[i][2], listaEsperaPacientePrioritarioEndocrinologia[i][3],
                                                 hora, minuto)
        horaFormatada=str(hora_total)+" h : "+str(minuto_total)+" min"
        x.add_row([listaEsperaPacientePrioritarioEndocrinologia[i][5], listaEsperaPacientePrioritarioEndocrinologia[i][1], "Endocrinologia", "Em espera", horaFormatada])
    for i in range(len(listaEsperaPacienteComumEndocrinologia)):
        hora_total, minuto_total=VariacaoDeTempo(listaEsperaPacienteComumEndocrinologia[i][2], listaEsperaPacienteComumEndocrinologia[i][3],
                                                 hora, minuto)
        horaFormatada=str(hora_total)+" h : "+str(minuto_total)+" min"
        x.add_row([listaEsperaPacienteComumEndocrinologia[i][5], listaEsperaPacienteComumEndocrinologia[i][1], "Endocrinologia", "Em espera", horaFormatada])

    #Inserindo na tabela listas de espera de Ortopedia
    if(paciente_em_antendimento_Ortopedia):
        hora_total, minuto_total=VariacaoDeTempo(paciente_em_antendimento_Ortopedia[2], paciente_em_antendimento_Ortopedia[3],
                                                 paciente_em_antendimento_Ortopedia[6], paciente_em_antendimento_Ortopedia[7])
        horaFormatada=str(hora_total)+" h : "+str(minuto_total)+" min"

        x.add_row([paciente_em_antendimento_Ortopedia[5], paciente_em_antendimento_Ortopedia[1], "Ortopedia", "Em atendimento", horaFormatada])
    for i in range(len(listaEsperaPacientePrioritarioOrtopedia)):
        hora_total, minuto_total=VariacaoDeTempo(listaEsperaPacientePrioritarioOrtopedia[i][2], listaEsperaPacientePrioritarioOrtopedia[i][3],
                                                 hora, minuto)
        horaFormatada=str(hora_total)+" h : "+str(minuto_total)+" min"
        x.add_row([listaEsperaPacientePrioritarioOrtopedia[i][5], listaEsperaPacientePrioritarioOrtopedia[i][1], "Ortopedia", "Em espera", horaFormatada])
    for i in range(len(listaEsperaPacienteComumOrtopedia)):
        hora_total, minuto_total=VariacaoDeTempo(listaEsperaPacienteComumOrtopedia[i][2], listaEsperaPacienteComumOrtopedia[i][3],
                                                 hora, minuto)
        horaFormatada=str(hora_total)+" h : "+str(minuto_total)+" min"
        x.add_row([listaEsperaPacienteComumOrtopedia[i][5], listaEsperaPacienteComumOrtopedia[i][1], "Ortopedia", "Em espera", horaFormatada])
        '''
    x=Gerar_Tabela_Pacientes_Em_Atendimento(x, paciente_em_atendimento_Dermatologia)
    x=Gerar_Tabela_Pacientes_Em_Espera(x, listaEsperaPacienteComumDermatologia, hora, minuto)
    x=Gerar_Tabela_Pacientes_Em_Espera(x, listaEsperaPacientePrioritarioDermatologia, hora, minuto)
    x=Gerar_Tabela_Pacientes_Em_Atendimento(x, paciente_em_antendimento_Endocrinologia)
    x=Gerar_Tabela_Pacientes_Em_Espera(x, listaEsperaPacienteComumEndocrinologia, hora, minuto)
    x=Gerar_Tabela_Pacientes_Em_Espera(x, listaEsperaPacientePrioritarioEndocrinologia, hora, minuto)
    x=Gerar_Tabela_Pacientes_Em_Atendimento(x, paciente_em_antendimento_Ortopedia)
    x=Gerar_Tabela_Pacientes_Em_Espera(x, listaEsperaPacienteComumOrtopedia, hora, minuto)
    x=Gerar_Tabela_Pacientes_Em_Espera(x, listaEsperaPacientePrioritarioOrtopedia, hora, minuto)
    print(x)
def ExibirPacientesAtendidosNoDia(listaPacienteComumAtendidoDermatologia, listaPacienteComumAtendidoEndocrinologia,
                                  listaPacienteComumAtendidoOrtopedia, listaPacientePrioritarioAtendidoDermatologia,
                                  listaPacientePrioritarioAtendidoEndocrinologia, listaPacientePrioritarioAtendidoOrtopedia):
    from prettytable import PrettyTable
    x = PrettyTable(["Nome do paciente", "Tempo de espera na fila", "Tempo de Atendimento", "Consultório", "Médico do Consultório"])

    # Alinha as colunas
    x.align["Nome do paciente"] = "l"
    x.align["Tempo de espera na fila"] = "l"
    x.align["Tempo de Atendimento"]="r"
    x.align["Consultório"] = "r"
    x.align["Médico do Consultório"] = "r"
    #Inserindo na tabela os pacientes comuns do consultorio de dermatologia
    for i in range(len(listaPacienteComumAtendidoDermatologia)):
        hora_espera_na_fila, minuto_espera_na_fila=VariacaoDeTempo(listaPacienteComumAtendidoDermatologia[i][2], listaPacienteComumAtendidoDermatologia[i][3],
                                             listaPacienteComumAtendidoDermatologia[i][6], listaPacienteComumAtendidoDermatologia[i][7])
        tempo_espera_na_fila=str(hora_espera_na_fila)+" h : "+str(minuto_espera_na_fila)+" min"
        hora_atendimento, minuto_atendimento=VariacaoDeTempo(listaPacienteComumAtendidoDermatologia[i][6], listaPacienteComumAtendidoDermatologia[i][7],
                                          listaPacienteComumAtendidoDermatologia[i][8], listaPacienteComumAtendidoDermatologia[i][9])
        tempo_atendimento=str(hora_atendimento)+" h : "+str(minuto_atendimento)+" min"
        x.add_row([listaPacienteComumAtendidoDermatologia[i][1], tempo_espera_na_fila, tempo_atendimento, "Dermatologia", "Dra. Silvia Melo"])

    #Inserindo na tabela os pacientes comuns do consultorio de dermatologia
    for i in range(len(listaPacientePrioritarioAtendidoDermatologia)):
        hora_espera_na_fila, minuto_espera_na_fila=VariacaoDeTempo(listaPacientePrioritarioAtendidoDermatologia[i][2], listaPacientePrioritarioAtendidoDermatologia[i][3],
                                             listaPacientePrioritarioAtendidoDermatologia[i][6], listaPacientePrioritarioAtendidoDermatologia[i][7])
        tempo_espera_na_fila=str(hora_espera_na_fila)+" h : "+str(minuto_espera_na_fila)+" min"
        hora_atendimento, minuto_atendimento=VariacaoDeTempo(listaPacientePrioritarioAtendidoDermatologia[i][6], listaPacientePrioritarioAtendidoDermatologia[i][7],
                                          listaPacientePrioritarioAtendidoDermatologia[i][8], listaPacientePrioritarioAtendidoDermatologia[i][9])
        tempo_atendimento=str(hora_atendimento)+" h : "+str(minuto_atendimento)+" min"
        x.add_row([listaPacientePrioritarioAtendidoDermatologia[i][1], tempo_espera_na_fila, tempo_atendimento, "Dermatologia", "Dra. Silvia Melo"])

    #Inserindo na tabela os pacientes comuns do consultorio de endocrinologia
    for i in range(len(listaPacienteComumAtendidoEndocrinologia)):
        tempo_espera_na_fila=VariacaoDeTempo(listaPacienteComumAtendidoEndocrinologia[i][2], listaPacienteComumAtendidoEndocrinologia[i][3],
                                             listaPacienteComumAtendidoEndocrinologia[i][6], listaPacienteComumAtendidoEndocrinologia[i][7])
        tempo_atendimento=VariacaoDeTempo(listaPacienteComumAtendidoEndocrinologia[i][6], listaPacienteComumAtendidoEndocrinologia[i][7],
                                          listaPacienteComumAtendidoEndocrinologia[i][8], listaPacienteComumAtendidoEndocrinologia[i][9])
        x.add_row([listaPacienteComumAtendidoEndocrinologia[i][1], tempo_espera_na_fila, tempo_atendimento, "Endocrinologia", "Dr. Fernando Santos"])

    #Inserindo na tabela os pacientes comuns do consultorio de endocrinologia
    for i in range(len(listaPacientePrioritarioAtendidoEndocrinologia)):
        hora_espera_na_fila, minuto_espera_na_fila=VariacaoDeTempo(listaPacientePrioritarioAtendidoEndocrinologia[i][2], listaPacientePrioritarioAtendidoEndocrinologia[i][3],
                                             listaPacientePrioritarioAtendidoEndocrinologia[i][6], listaPacientePrioritarioAtendidoEndocrinologia[i][7])
        tempo_espera_na_fila=str(hora_espera_na_fila)+" h : "+str(minuto_espera_na_fila)+" min"
        hora_atendimento, minuto_atendimento=VariacaoDeTempo(listaPacientePrioritarioAtendidoEndocrinologia[i][6], listaPacientePrioritarioAtendidoEndocrinologia[i][7],
                                          listaPacientePrioritarioAtendidoEndocrinologia[i][8], listaPacientePrioritarioAtendidoEndocrinologia[i][9])
        tempo_atendimento=str(hora_atendimento)+" h : "+str(minuto_atendimento)+" min"
        x.add_row([listaPacientePrioritarioAtendidoEndocrinologia[i][1], tempo_espera_na_fila, tempo_atendimento, "Endocrinologia", "Dr. Fernando Santos"])

    #Inserindo na tabela os pacientes comuns do consultorio de ortopedia
    for i in range(len(listaPacienteComumAtendidoOrtopedia)):
        tempo_espera_na_fila=VariacaoDeTempo(listaPacienteComumAtendidoOrtopedia[i][2], listaPacienteComumAtendidoOrtopedia[i][3],
                                             listaPacienteComumAtendidoOrtopedia[i][6], listaPacienteComumAtendidoOrtopedia[i][7])
        tempo_atendimento=VariacaoDeTempo(listaPacienteComumAtendidoOrtopedia[i][6], listaPacienteComumAtendidoOrtopedia[i][7],
                                          listaPacienteComumAtendidoOrtopedia[i][8], listaPacienteComumAtendidoOrtopedia[i][9])
        x.add_row([listaPacienteComumAtendidoOrtopedia[i][1], tempo_espera_na_fila, tempo_atendimento, "Ortopedia", "Dra. Maria do Carmo Silva"])

    #Inserindo na tabela os pacientes comuns do consultorio de ortopedia
    for i in range(len(listaPacientePrioritarioAtendidoOrtopedia)):
        hora_espera_na_fila, minuto_espera_na_fila=VariacaoDeTempo(listaPacientePrioritarioAtendidoOrtopedia[i][2], listaPacientePrioritarioAtendidoOrtopedia[i][3],
                                             listaPacientePrioritarioAtendidoOrtopedia[i][6], listaPacientePrioritarioAtendidoOrtopedia[i][7])
        tempo_espera_na_fila=str(hora_espera_na_fila)+" h : "+str(minuto_espera_na_fila)+" min"
        hora_atendimento, minuto_atendimento=VariacaoDeTempo(listaPacientePrioritarioAtendidoOrtopedia[i][6], listaPacientePrioritarioAtendidoOrtopedia[i][7],
                                          listaPacientePrioritarioAtendidoOrtopedia[i][8], listaPacientePrioritarioAtendidoOrtopedia[i][9])
        tempo_atendimento=str(hora_atendimento)+" h : "+str(minuto_atendimento)+" min"
        x.add_row([listaPacientePrioritarioAtendidoOrtopedia[i][1], tempo_espera_na_fila, tempo_atendimento, "Ortopedia", "Dra. Maria do Carmo Silva"])

    print(x)
def ExibirTempoMedioDeEsperaDosPacientes():
    print("Esta funções serve para exibir o tempo medio de espera dos pacientes")

def ExibirTempoMedioDeAtendimentoDosPacientes():
    print("Esta função serve para exibir tempo médio de atendimento dos pacientes")
